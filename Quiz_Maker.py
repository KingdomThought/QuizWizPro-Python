import sqlite3
from numpy import record

def create_Quiz():
    quizAuthor = input("What is your email adress\n")
    verify_Quiz_Author(quizAuthor)
    school_Level = input("What Grade level is this quiz\n""1.Elementary School\n"
                        "2.Junior HIgh School\n""3.High School\n""4.College\n")

    grade_Level = input("What Grade level is this quiz\n""1.Freshman\n"
                        "2.Sophmore\n""3.Junior\n""4.Senior\n") 

    typeOfQuiz = input( "What type of Quiz is this\n""1.Math\n"
                        "2.Science\n""3.History\n""4.Language Arts\n"
                        "5.Geography\n""6.Social Studies\n")   

    nameOfQuiz = input("Please Give this Quiz a Title Name\n")



def verify_Quiz_Author(quiz_A):
    quiz_A
    con = sqlite3.connect('DataBase-QuizWizPro.db')
    cur = con.cursor() 
    cur.execute("""   SELECT id, fname, lname FROM users  WHERE email = (?)  """,  (quiz_A,) )
    records = cur.fetchone()
    print("Records Read")
    print (cur.rowcount)
    print(records[0])
    print(records[1])
    print(records[2])
    #userinfo = [records]
    return records
    
    #con.commit()

create_Quiz()