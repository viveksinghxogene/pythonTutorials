import mysql.connector
#this is going to connect to the database connection that I have.
connection=mysql.connector.connect(host="localhost",database="emp_db",user="root",password="Vivek123@")
if connection.is_connected():
    print('Connection to the MYSQL Database is done successfully.')
else:
    print('Connection to the database is failed due to unforeseen reasons that I am still figuring out how.')
#always close the connection
connection.close()