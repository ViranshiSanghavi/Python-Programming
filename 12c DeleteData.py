import mysql.connector

# Create a database connection
db = mysql.connector.connect(user='root', passwd='Viranshi@2004', host='localhost', database='your_database_name')

# Create a cursor object
cursor = db.cursor()

# Prepare SQL query to DELETE required records using parameterized query
sql = "DELETE FROM EMPLOYEE WHERE AGE < %s"

# Define the value as a tuple
age_threshold = (20,)

try:
    # Execute the SQL command with the value
    cursor.execute(sql, age_threshold)
    
    # Print a success message
    print("Data Deleted Successfully...!")
    
    # Commit your changes in the database
    db.commit()
except Exception as e:
    # Rollback in case there is any error
    print("Error:", e)
    db.rollback()

# Disconnect from the server
db.close()
