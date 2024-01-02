import sqlite3
    
    #modual.method()
conn = sqlite3.connect("./mydatabase.sqlite")

#calling
cursor=conn.cursor()

qurey="""
         CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL
         ); 
     """
cursor.execute(qurey) #qurey is actual argument

conn.commit()

qurey="INSERT INTO employes(name,position,salary) VALUES(?,?,?);"

#Ceo.method(aa1,aa2)
cursor.execute(qurey,("RAJVIR", 'CEO', 70000.00))
cursor.execute(qurey,("ROHIT", 'DIRECTOR', 66000.00))

conn.commit()
