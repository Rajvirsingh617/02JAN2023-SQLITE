import sqlite3
    
# module.method()
conn = sqlite3.connect("./mydatabase.sqlite")

# calling
cursor = conn.cursor()

query = """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL
        ); 
    """
cursor.execute(query)  # query is the actual argument

conn.commit()

query = "INSERT INTO employees(name, position, salary) VALUES(?,?,?)"

# CEO.method(aa1, aa2)
cursor.execute(query, ("RAJVIR", 'CEO', 70000.00))
cursor.execute(query, ("ROHIT", 'DIRECTOR', 66000.00))

conn.commit()
