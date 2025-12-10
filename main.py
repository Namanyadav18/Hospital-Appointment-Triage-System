from hospital_system import HospitalSystem

def demo():
    hs = HospitalSystem(routine_queue_size=10)

    # Add doctor & slots
    hs.addDoctor(1, 'Dr. A')
    hs.addSlotToDoctor(1, 101, '09:00', '09:15')

    # Register patients
    hs.registerPatient(1, 'Alice', 30, severity=50)
    hs.registerPatient(2, 'Bob', 45, severity=20)

    # Routine booking
    ok, token = hs.bookRoutine(1, 1, 101)
    print("Routine booking:", ok, token)

    # Emergency case
    hs.triageInsert(2, 10)

    # Serve next
    print('Serving (should serve emergency first):', hs.serveNext())

    # Report summary
    print('Report summary:', hs.report())

if __name__ == '__main__':
    demo()
