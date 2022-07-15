
#This is the Main Menu Where the program begines
import os
import sqlite3
import User
from turtle import clear, clearscreen
validate_entry =""

def main_Menu():
    # Try block is use to ensure that the user enters a valid input
    try:
        main_Menu_Selection = input(
        "WELCOME TO QUIZWIZ PRO\n"
        "1. If you are a Student Press 1\n" 
        "2 .If your are an Instructor Press 2\n""3. Exit Program\n" )
    #If the user enters an input that is not valid they will be asked to rey again
        if main_Menu_Selection == "" or int(main_Menu_Selection) > 2 or int(main_Menu_Selection) < 1:
            print("You did not enter a valid selection. Please Try Again\n")
            main_Menu()
        elif main_Menu_Selection == "1" :
            print ("STUDENT MENU")
            student_Menu()
        elif main_Menu_Selection == "2" :
            print ("INSTRUCTOR/TEACHER MENU")
            instructor_Menu()

    except: 
        print("You did not enter a valid selection 1. pleasee try again")
        main_Menu()

#Student Login Menu
def student_Menu ():
    #student_Login_Method =''
    try: 
        student_Login = input (
        "1.Press 1 To Login\n"
        "2.Press 2 to create a Student Account\n"
        "3.Press 3 to Go Back\n""4.Press 4 to Exit Program\n")
        if (student_Login) == '1':      
            student_Login_Method()
        elif (student_Login) == '2':
            User.create_User()
            print(student_Login_Method)
    except:
        print("You did not enter a valid selection")

def instructor_Menu():
    student_Login = input (
    "1.Press 1 To Login\n"
    "2.Press 2 to create an Instructor Account\n"
    "3.Press 3 to Go Back\n""4.Press 4 to Exit Program\n")

def student_Login_Method():
    print("Student Login")
    student_Email = input("Please Enter your Email Address\n")
    student_Password = input("Please Enter your password\n")
    valid_S_login = validate_Password (student_Email, student_Password)
    if valid_S_login == True:
        print("correct Email addy")
    else:
        print ("Incorrect login")

def validate_Password(u_Name, p_word):
    pass_W = u_Name
    pw_word = p_word
    con = sqlite3.connect('DataBase-QuizWizPro.db')
    cur = con.cursor()
    cur.execute(""" SELECT password FROM users WHERE email=? """, [pass_W])
    p_result = cur.fetchone()
    print(p_result)
    print(pw_word)
    pw_Result = p_result[0]
    if pw_Result== pw_word :
        return True
    else :
       return False 

    #con.commit()


#Driver
main_Menu()

#validate_Password ('MeggaDon@gmail.com','MEGGAdon890')

