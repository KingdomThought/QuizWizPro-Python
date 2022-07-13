import mysql.connector
mydb = mysql.connector.connect(host='127.0.0.1',  user ='megga', passwd ='meggaman')
mycursor=mydb.cursor()
mycursor.execute("show databses")