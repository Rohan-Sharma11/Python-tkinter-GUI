'''This Python SQLite tutorial aims to demonstrate how to develop Python database applications with 
the SQLite database. You will learn how to perform SQLite database operations from Python.

As you all know, SQLite is a C-language library that implements a SQL database engine that is relatively
 quick, serverless, and self-contained, high-reliable. SQLite is the most commonly used database engine in 
 the test environment (Refer to SQLite Home page).

SQLite comes built-in with most computers and mobile devices, and browsers.
Python’s official sqlite3 module helps us to work with the SQLite database.'''



import sqlite3

conn_obj = sqlite3.connect("CS.DB")
print("Connection object created") #for checking the error 

cursor_obj = conn_obj.cursor()
print("Cursor object created") #for checking the error 

conn_obj.execute('drop table if exists computer')
conn_obj.execute('''Create table computer(Roll_NO Primary Key Not NULL,Name char(10),Class char(10))''')

cursor_obj.execute("INSERT INTO computer(Roll_no, Name, Class) VALUES (2506, 'Rohan', 'FYBSC CS')")

cursor_obj = conn_obj.execute("SELECT Roll_no, Name, Class FROM computer WHERE Roll_NO=2506")
for row in cursor_obj:
    print("Roll_NO=", row[0], "Name=", row[1], "Class=", row[2])
