import sqlite3 
 
con = sqlite3.connect('QWP.db')
cur = con.cursor()
cur.execute()
con.commit
cur.close
con.close