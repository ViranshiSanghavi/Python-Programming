import mysql.connector

# Connect to MySQL server and specify the database
db = mysql.connector.connect(user='root', passwd='Viranshi@2004', host='localhost', database='your_database_name')

# Check if the connection was successful
if db.is_connected():
    print("Connected to MySQL successfully")

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exists using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT
)"""
cursor.execute(sql)

print("Table Created Successfully")

# Disconnect from the server
db.close()
