import os
import psycopg2

try:

    conn = psycopg2.connect(
        database="postgres", 
        user='postgres', 
        password='1234',
        host='127.0.0.1'        
    )

except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
    exit(1)

conn.autocommit = True

cursor = conn.cursor()

db_name = os.environ.get("DB_NAME")

#Preparing query to create a database
sql = '''CREATE database "TheDatabase10"'''

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection
conn.close()