#Luxe Clinic Main Application Server
from flask import Flask, render_template, request, redirect, url_for
from models import ClinicQueue

app = Flask(__name__)
luxe_clinic = ClinicQueue()

# [span_5](start_span)Requirement: Route 1 - Home Page[span_5](end_span)
@app.route('/')
#ROUTE TO RENDER THE HOME DASHBOARD
def home():
    return render_template('home.html', 
                           patients=luxe_clinic.queue, 
                           total=luxe_clinic.total_seen)

# [span_6](start_span)Requirement: Route 2 - Registration Page[span_6](end_span)
@app.route('/add', methods=['GET', 'POST'])
#ROUTE TO HANDLE NEW PATIENT POST DATA
def add_patient():
    if request.method == 'POST':
        name = request.form.get('p_name')
        issue = request.form.get('p_issue')
        if name and issue:
            luxe_clinic.add_patient(name, issue)
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/call_next')
def call_next():
    luxe_clinic.treat_next()
    return redirect(url_for('home'))

@app.route('/undo')
def undo():
    luxe_clinic.undo_action()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)