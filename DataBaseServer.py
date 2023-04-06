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
conn_obj.execute('''Create table computer(Roll_NO Primary Key Not NULL,Name char(10),Class char(10),Address char(15))''')

cursor_obj.execute("INSERT INTO computer(Roll_NO, Name, Class, Address) VALUES (2506, 'Rohan', 'FYBSC CS','Goregaon')")
cursor_obj.execute("INSERT INTO computer(Roll_NO, Name, Class, Address) VALUES (2444, 'Varun', 'FYBSC CS','Malad')")
cursor_obj.execute("INSERT INTO computer(Roll_NO, Name, Class, Address) VALUES (2515, 'jatin', 'FYBSC CS','Kandivali')")
cursor_obj.execute("INSERT INTO computer(Roll_NO, Name, Class, Address) VALUES (2416, 'Divyansh', 'FYBSC CS','Kandivali')")
cursor_obj.execute("INSERT INTO computer(Roll_NO, Name, Class, Address) VALUES (2450, 'Rishi', 'FYBSC CS','Goregaon')")
cursor_obj.execute("INSERT INTO computer(Roll_NO, Name, Class, Address) VALUES (2404, 'prashant', 'FYBSC CS','Malad')")

cursor_obj = conn_obj.execute("SELECT * from computer")
#cursor_obj=conn_obj.execute("SELECT * from computer Where Address='Goregaon' ") # this is for filtering the data
for row in cursor_obj:
    print("Roll_NO=", row[0], "Name=", row[1], "Class=", row[2], "Address=",row[3])
