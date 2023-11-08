from local import *
from data import *
from entries import *
from sqlalchemy import delete

def main():
    pList = []
    localDoctors = {"Maria"}

    choice = 0
    while choice != 4:
        print(" *** Welcome To Salama ***")
        print("1) Find available doctors: ")
        print("2) Current patients list: ")
        print("3) Make new appointment: ")
        print("4) Quit Program!")
        choice = int(input())

        if choice == 1:
            d_record = session.query(Hospitals, Doctors).join(Doctors).filter(Hospitals.h_id == Doctors.workplace).all()

            for i in d_record:
                print (i)

        elif choice == 2:
            

            p_record = session.query(Appointments).all()
            discharge = str(input("Want to discharge a patient? "))
            
            if discharge == "no":
                for i in p_record:
                    print (i)
            else:
                patient_column = input("Enter name for column deletion: ")
                patient_value = input("Enter name of patient: ")

                # connection = engine.connect()
                deletion = delete(Appointments).where((Appointments, patient_column) == patient_value)
                # connection.execute(deletion)
                session.commit()
                

                print("!!! Patient Discharged !!!")

        
        elif choice == 3:
            p_name = str(input("Patients name: "))
            ailment = str(input("What diagnosis was made? "))
            doctor = int(input("Doctor id: "))
            hospital = int(input("Hospital id: "))


            
            record = Appointments(
                patient = p_name,
                ailment = ailment,
                doctor = doctor,
                hospital = hospital
            )
            
                
                
            session.add(record)
            session.commit()

            print("Record updated successfully")
            



        else:
            print("Terminating program ...")
    print("Session ended!")


if __name__ == "__main__":
    main()

