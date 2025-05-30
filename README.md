# Problem Statement: LLM-Powered Chatbot with FastAPI and SQL Integration

1. Tech Stack
● Backend: FastAPI
● Frontend: Streamlit
● Database: PostgreSQL
● LLM Endpoint: Groq (free tier) using llama-3.1-8b-instant

2. Database Schema
You must create a basic customer database with the following fields:
● customer_id (Primary Key)
● name (Text)
● gender (Text)
● location (Text)

The database name is "TheDatabase15"

Following are the entries to the database:

query1 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (1,  'Issac Newton',     'Male',    'England');''')
query2 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (2,  'Marie Curie',      'Female',  'Poland');''')
query3 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (3,  'Michael Faraday',  'Male',    'USA');''')
query4 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (4,  'Nicholas Tesla',   'Male',    'USA');''')
query5 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (5,  'Galileo Galilei',  'Male',    'Italy');''')

3. Functionality

The user inputs a natural language query via the UI.
The backend (FastAPI) sends the query to the LLM via the Groq endpoint.
The LLM interprets the query and generates a corresponding SQL query.
The backend should execute the SQL query, retrieve the results, and return them to
the user.
The frontend displays the formatted results.

4. Required Steps

python createdatabase.py
python app.py
python -m streamlit run client.py

![image](https://github.com/user-attachments/assets/b558d574-f984-4da9-bdb2-a59cdcb8f134)

![image](https://github.com/user-attachments/assets/14066f5a-30dc-44f5-ac50-932c0e0a582f)

![image](https://github.com/user-attachments/assets/f396439c-6719-442f-bd76-dc1823698693)

![image](https://github.com/user-attachments/assets/837b6031-54cc-4e1a-ae2e-defb64073a0c)

![image](https://github.com/user-attachments/assets/6d6fbd74-191c-49ed-8e47-5f925ae68b22)







