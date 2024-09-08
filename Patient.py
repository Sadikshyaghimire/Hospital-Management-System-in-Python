# class Patient:
#     """Patient class"""

#     def __init__(self, username, surname, age, mobile, password):
#         """
#         Args:
#             first_name (string): First name
#             surname (string): Surname
#             age (int): Age
#             mobile (string): the mobile number
#             address (string): address
#         """

#         self.__p_username = username
#         self.__p_surname = surname
#         self.__age = age
#         self.__mobile = mobile
#         self.__password = password
#         self.__doctor = 'None'
#        # Open a file for writing patient details in append mode
#         with open('patients.txt', 'a') as f:
#              f.write(f'{self.__p_username}|{self.__p_surname}|{self.__age}|{self.__mobile}|{self.__password}|{self.__doctor}\n')
       
#     def full_name(self) :
#         """full name is first_name and surname"""
#         return self.__p_username+ self.__p_surname

#     def get_doctor(self) :
        
#         return self.__doctor

#     def link(self, doctor):
#         """Args: doctor(string): the doctor full name"""
#         self.__doctor = doctor

#     def print_symptoms(self):
#         """prints all the symptoms"""
#         symptoms = input("Please enter your symptoms.")
#         print(symptoms)

#     def __str__(self):
#         return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__password:^10}'

import os
class Patient:
    """Patient class"""

    def __init__(self, username, surname, age, mobile, password):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """

        self.__p_username = username
        self.__p_surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__password = password
        self.__doctor = 'None'

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """

        print("-----Login-----")
        #Get the details of the admin

        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # check if the username and password match the registered ones
        if(self.__p_username == username) & (self.__password == password):
            return True
        else:
            print("Invalid username and password.")
       
    def full_name(self) :
        """full name is first_name and surname"""
        return self.__p_username+ self.__p_surname

    def get_doctor(self) :
        
        return self.__doctor

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        symptoms = input("Please enter your symptoms.")
        print(symptoms)

    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__password:^10}'
    
    #write details in file 
    def write_details(self):
        with open('patients.txt', 'r') as f:
            if f.read() == '':
        # file is empty, so write headers
                with open('patients.txt', 'a') as f:
                    f.write('Firstname\tSurname\t\tAge\t\tMobile\t\tDoctor\n\n')

        with open('patients.txt', 'r') as f:
            if self.__p_username not in f.read():
                # patient details don't exist, so append to file
                with open('patients.txt', 'a') as f:
                    f.write(f'{self.__p_username}\t\t{self.__p_surname}\t\t\t{self.__age}\t\t{self.__mobile}\t\t{self.__doctor}\n')
                    



