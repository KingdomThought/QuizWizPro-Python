
from ast import If
import mysql.connector 
from datetime import date 
from datetime import datetime
import re
import sqlite3

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#Regular Expression --- Validation for menu entries
regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
regex2= re.compile("^(?=[a-zA-Z0-9._]{8,20}$)(?!.*[_.]{2})[^_.].*[^_.]$")
regex3= re.compile("[A-Za-z]{2,25}||\s[A-Za-z]{2,25}")
regex4= re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$")
#***************************************************************************************************************
valid_Email=False
valid_UserName=False
valid_Password=False
email_Address=None
global type_Of_User
type_Of_User =""
global main_Email_Add 
#*************************************************************************************************************
def create_User():
    #valid_Email= isValid(input_Email)
    email_Address
    date_Created=date.today()
    time_Created=datetime.now()
    u_Type = ''
    
    #Start of Create User Menu
    #Name
   
    fName=input("What is your first name?\n")
    while fName == "" or fName_Valid(fName)==False:
        print ("That Response was invalid.")
        print("Numbers and special characters are not allowed")
        fName=input("Please enter your First Name\n")
            
   
        
    lName=input("what is your Last name?\n")
    while lName == "" or fName_Valid(lName)==False:
        print ("That Response was invalid.")
        print("Numbers and special characters are not allowed")
        lName=input("Please enter your Last Name\n")
            
    
    #Email
    input_Email=input("What is your Email Address\n")
    valid_Email= isValid(input_Email)
    while valid_Email==False:
        print ("You Must enter a Valid input_Email Address")
        input_Email=input("What is your Email Address\n")
        valid_Email= isValid(input_Email)
       
    
    #UserType
    userType=input("""1.If you are a Student Press S \n"
                "2.If you are a Instructor/Teacher press T\n""")
    user_type_ =""
    type_Of_User=''
   
    if userType == 'S' :
        
        type_Of_User = 'S'
        userType="Student"
    elif userType=='S':
        
        type_Of_User= 'T'
        userType="Teacher"
    
    #UserName
    user_Name=input("Please choose a User Name\n")
    valid_UserName= username_IsValid(user_Name)
    while valid_UserName==False:
        print ("You Must choose a username between 8-20 characters")
        user_Name=input("please choose a valid usernamed\n")
        valid_UserName= username_IsValid(user_Name)
   
    #password
    password=input("please select a password\n")
    valid_Password = password_Valid(password)
    while valid_Password==False:
        print("Password must have: ")
        print("1) At least six characters long")
        print("2)contain a lowercase letter")
        print("3)contain an uppercase letter ")
        print("4)contains a number")
        password=input("please choose a valid password\n")
        valid_Password= password_Valid(password)


    confirm_Password=print("Please re-enter your passwprd to confirm they match\n")
    
    
    #UserArray Storage in Memory
    user_Array=[]
    user_Array.append(fName)
    user_Array.append(lName)
    user_Array.append(input_Email)
    user_Array.append(password)
    user_Array.append(user_Name)
    user_Array.append(date_Created)
    print(user_Array)
   
    #Verify Inputs
    print("Please Verify that the information you have entered is correct")
    print("You are a: " + userType)
    print("First Name: " + fName )
    print("Last Name: " + lName)
    print("Email: " + input_Email) 
    print("Username: "+ user_Name)
    print("Account Created on " + str(date_Created))
    print("Time Created " + str(current_time) + "\n")
    
    #if the entrie are correct user can slect to add their info to database
    correct_Info = input("is this information correct? Press 1 for yes and N for No. ")
    if correct_Info == '1':
        add_User_To_Database(fName,lName,input_Email,user_Name, 
        password, userType, date_Created, current_time)
    else: 
        create_User()
    
#*************************************************************************************************************

def add_User_To_Database(first_name, last_name, email_address, user_name,
 password, userType, date_created, time_Created):
   
    con = sqlite3.connect('DataBase-QuizWizPro.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
            (id integer PRIMARY KEY, fName text, lname text, email text, username text, password text, userType text, date_Created date, time_Created time
            );''')

    cur.execute("""INSERT INTO users 
    (fName,lname,email, username, password, userType, date_Created, time_Created)
     VALUES (?,?,?,?,?,?,?,?)""",(first_name, last_name, email_address, user_name, 
     password,userType, date_created, time_Created) )
    con.commit()




def validate_Email_Structure(email):
    input_Email = email
    valid_Email= isValid(input_Email)
    print(isValid(input_Email))
    print(valid_Email)
    
    while valid_Email==False:
        
        print ("You Must enter a Valid input_Email Address")
        input_Email=input("What is your Email Address\n")
        valid_Email= isValid(input_Email)
        main_Email_Add = input_Email
       

#input_Email Validation
def fName_Valid(first_Name):
    if re.fullmatch(regex3, first_Name):
        valid_Email=True
        return True
    else:
        print("False")
        valid_Email=False
        return False

def password_Valid(pass_Word):
    if re.fullmatch(regex4, pass_Word):
        valid_Email=True
        return True
    else:
        print("False")
        valid_Email=False
        return False

#input_Email Validation
def isValid(input_Email):
    if re.fullmatch(regex, input_Email):
        valid_Email=True
        return True
    else:
        valid_Email=False
        return False

def username_IsValid(user_name):
    if re.fullmatch(regex2, user_name):
        valid_UserName=True
        return True
    else:
        valid_UserName=False
        return False


#create_User()
#add_User_To_Database()





