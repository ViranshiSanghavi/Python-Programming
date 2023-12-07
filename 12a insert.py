import mysql.connector

# Create a database connection
db = mysql.connector.connect(user='root', passwd='Viranshi@2004', host='localhost', database='your_database_name')

# Create a cursor object
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database
sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
VALUES ('Nitesh', 'Shukla', 23, 'M', 20000)"""

try:
    # Execute the SQL command
    cursor.execute(sql)
    
    # Print a success message
    print("Data Inserted Successfully...!")
    
    # Commit your changes in the database
    db.commit()
except Exception as e:
    # Rollback in case there is any error
    print("Error:", e)
    db.rollback()

# Disconnect from the server
db.close()
