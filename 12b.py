import mysql.connector

# Create a database connection
db = mysql.connector.connect(user='root', passwd='Viranshi@2004', host='localhost', database='your_database_name')

# Create a cursor object
cursor = db.cursor()

# Define the SQL query to select rows with income greater than 1000
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s"

try:
    # Execute the SQL command with a tuple parameter
    cursor.execute(sql, (1000,))

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()

    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]

        # Print fetched result
        print("Fname=%s, Lname=%s, Age=%d, Sex=%s, Income=%d" % (fname, lname, age, sex, income))
except Exception as e:
    print("Error:", e)

# Disconnect from the server
db.close()
