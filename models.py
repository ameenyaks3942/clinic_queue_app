#Patient Class For OOP
# from datetime import datetime

class Patient:
    def __init__(self, name, ailment):
        self.name = name
        self.ailment = ailment
        self.arrival_time = datetime.now().strftime("%I:%M %p") 

    def get_details(self):
        return f"{self.name} | Issue: {self.ailment} | Arrived: {self.arrival_time}"

class ClinicQueue:
    def __init__(self):
        self.queue = [] 
        self.history_stack = [] 
        self.total_seen = 0

    def add_patient(self, name, ailment):
        new_patient = Patient(name, ailment)
        self.queue.append(new_patient)

    def treat_next(self):
        if self.queue:
            patient = self.queue.pop(0)
            self.history_stack.append(patient)
            self.total_seen += 1
            return patient
        return None

    def undo_action(self):
        if self.history_stack:
            last_patient = self.history_stack.pop()
            self.queue.insert(0, last_patient)
            self.total_seen -= 1
            return last_patient
        return None