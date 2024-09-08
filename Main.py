
from Admin import Admin
from Doctor import Doctor
from Patient import Patient


def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('sadikshya', '12345', 'kalanki')  # username is 'sadikshay', password is '12345'
    doctors = Doctor('David', 'Smith', 'Opthamologist','hello')
    patients = Patient('avash', 'rai', 21, '9860', '2003')
    discharged_patients = []

    # keep trying to login tell the login details are correct
    while True:
        print('Login as: ')
        print('1- Admin')
        print('2- Doctor')
        print('3- Patient')
        login_choice = input('Enter your choice: ')
        
        if login_choice == '1':
            if admin.login():
                running = True  # allow program to run
                break
            else:
                print('Incorrect username or password.')

        elif login_choice == '2':
            if doctors.login():
                running = True
                break
            else:
                print('Incorrect username or password.')

        elif login_choice == '3':
            if patients.login():
                running = True  # allow program to run
                break
            else:
                print('Incorrect username or password.')

        else:
            print('Invalid choice. Try again.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- rellocation of the patient')
        print(' 7- Write patient`s details')
        print(' 8- View patient`s details')
        print(' 9- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
            admin.doctor_management(doctors)

        elif op == '2': 
            print("-----Patients-----")

            print('ID | Full Name | Doctor`s Full Name  | Age | Mobile | Postcode ')
            admin.view_patient(patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')

        elif op == '3':
                    # 3 - view discharged patients
                    admin.view_discharge(discharged_patients)

        elif op == '4':
                # 4- Assign doctor to a patient
                admin.assign_doctor_to_patient(patients, doctors)

        elif op == '5':
                # 5- Update admin detais
                admin.update_details()
        elif op == '6':
                #6 = rellocation of the patient
                admin.rellocate_patients(doctors,patients)
        elif op == '7':
                #7 = write patient`s details
                patients.write_details()
        elif op == '8':
                #8 = view patient`s details
                admin.view_patient(patients)
        elif op == '9':
                # 9- Quit
                running = False
        else:
                # the user did not enter an option that exists in the menu
                print('Invalid option. Try again')

if __name__ == '__main__':
    main()