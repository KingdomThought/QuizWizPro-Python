from datetime import date 
import numpy as np
import sqlite3
question = []


def create_Quiz():
    quizAuthor = input("What is your email adress\n")
    #verify_Quiz_Author(quizAuthor)
    typeOfQuiz = input("What type of Quiz is this\n")
    grade_Level = input("What Grade level is this quiz\n")
    nameOfQuiz = input("Please Give this Quiz a Title Name\n")



def verify_Quiz_Author(quiz_A):
    quiz_Author = quiz_A
    con = sqlite3.connect('DataBase-QuizWizPro.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users
            (id integer PRIMARY KEY, fName text, lname text, email text, username text, password text, userType text, date_Created date, time_Created time
            );''')

    cur.execute("""   SELECT id, fname, Lname, FROM users  WHERE email = '?';  """, (quiz_Author) )
    records = cur.fetchall
    print (records)
    con.commit()


#def add_Quiz_Author_Info():
    #pass 

#def add_Quiz_To_DB():
    #pass


        
      
       

#This Function tekes the inputs needed to create the quiz Questions
def create_Questions():
    date_Created=date.today()
    print(date_Created)
    num_Ques=input("How many question does this quiz contain?")
    print("This Quiz will contain" + num_Ques)
    count=1
    
    while count < int(num_Ques): 
        quiz_Question = input("Please enter Question # " + str(count))
        quiz_Answer = input("Please answer Question")
        print("You will now enter the alternate INCORRECT answer choices")
        quiz_Alt1 = input("Please enter alt Answer 1 ")
        quiz_Alt2 = input("Please enter alt Answer 2 ")
        quiz_Alt3 = input("Please enter alt Answer 3 ")
        
        count = count+1
        
        question.append(quiz_Question)
        question.append(quiz_Answer)
        question.append(quiz_Alt1)
        question.append(quiz_Alt2)
        question.append(quiz_Alt3)

        addquestion(question)
       
        
        
       
        
        

def addquestion(ques_Array):
    countarray = 1
    array=[]
    array=ques_Array
    allArrays=np.array([ques_Array])
    
    print(allArrays)
    


def create_Quiz ():
    pass 


create_Questions()
