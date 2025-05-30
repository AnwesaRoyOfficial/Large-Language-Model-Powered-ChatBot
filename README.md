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

