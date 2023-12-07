import mysql.connector

# Create a database connection
db = mysql.connector.connect(user='root', passwd='Viranshi@2004', host='localhost', database='your_database_name')

# Create a cursor object
cursor = db.cursor()

# Prepare SQL query to UPDATE records based on a condition
sql = "UPDATE EMPLOYEE SET INCOME = %s WHERE AGE < %s"

# Define the values to update and the condition as a tuple
update_values = (25000, 25)

try:
    # Execute the SQL command with the values
    cursor.execute(sql, update_values)

    # Print a success message
    print("Data Updated Successfully...!")

    # Commit your changes in the database
    db.commit()
except Exception as e:
    # Rollback in case there is any error
    print("Error:", e)
    db.rollback()

# Disconnect from the server
db.close()
