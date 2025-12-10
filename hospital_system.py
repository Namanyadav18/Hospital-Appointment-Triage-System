class HospitalSystem:
    def __init__(self):
        self.doctors = {}
        self.patients = PatientIndex()
        self.routineQ = CircularQueue(10)
        self.emergency = EmergencyTriage()
        self.undo = UndoStack()

    def registerDoctor(self, id):
        self.doctors[id] = DoctorSchedule(id)

    def addPatient(self, pid, name, age, severity):
        self.patients.add({"id": pid, "name": name, "age": age, "severity": severity})

    def bookRoutine(self, token):
        if self.routineQ.enqueue(token):
            self.undo.push(("book", token))
            print("Routine booking done")

    def emergencyIn(self, pid, severity):
        self.emergency.insert(pid, severity)
        self.undo.push(("emergency", pid))
        print("Emergency patient added")

    def serveNext(self):
        if self.emergency.heap:
            sev, p = self.emergency.pop()
            print(f"Emergency served: {p}")
            return

        token = self.routineQ.dequeue()
        if token:
            print(f"Routine served: {token}")
        else:
            print("No patients in queue")
