import mysql.connector

user = "root"
host = "localhost"
password = "Ideapad"

# establish connection
conn = mysql.connector.connect(user=user, password=password, host=host, database='MyDatabase')

# Creating cursor object
cursor = conn.cursor()

# drop already existing database with name MyDatabase
cursor.execute("DROP database IF EXISTS MyDatabase")

# create database query
cursor.execute("CREATE database MyDatabase")

# printing list of databases
print("List of databases")
cursor.execute("SHOW DATABASES")
db = cursor.fetchall()
for x in db:
    print(x)

#Dropping PATIENT table if already exists.
cursor.execute("DROP TABLE IF EXISTS PATIENT")

# Query to create table 
sql = '''CREATE TABLE PATIENT(
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    FEES FLOAT
    )'''
cursor.execute(sql)

# Query to insert values 
sql = '''INSERT INTO PATIENT(
   FIRST_NAME, LAST_NAME, AGE, SEX, FEES)
   VALUES (%s, %s, %s, %s, %s)'''

data = [('Misa', 'Bush', 23, 'F', 1000),('Satish', 'Sood', 45, 'M', 4000)]
try:
   # Executing the SQL command
   cursor.executemany(sql, data)

   # Commit your changes in the database
   conn.commit()

except:
   # Rolling back in case of error
   conn.rollback()

# Retrieving data 
sql = '''SELECT * from PATIENT'''
cursor.execute(sql)
result = cursor.fetchone()  #fetches 1 row
print(result)
result = cursor.fetchmany(size = 2)  #fetches size number of rows
print(result)

# where clause 
cursor.execute("SELECT * from PATIENT WHERE AGE >23")
print(cursor.fetchall())            #fetches all rows or remaining rows

# close connection
conn.close()