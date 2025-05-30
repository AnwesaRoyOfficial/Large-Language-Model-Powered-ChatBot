import os
import pandas as pd
from fastapi import FastAPI  # For building the API
from langchain.prompts import ChatPromptTemplate  # For creating chat prompts
from langchain_openai import ChatOpenAI  # For OpenAI chat functionality
from langchain_groq import ChatGroq  # For Groq chat functionality
from langchain_community.llms import Ollama  # For Ollama LLM
from langserve import add_routes  # For adding routes to the API
import uvicorn  # For running the API
import os  # For loading environment variables
from dotenv import load_dotenv  # For loading environment variables
from sqlalchemy import create_engine, text
from langchain.utilities import SQLDatabase
from langchain_openai import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate  # For creating chat prompts
from langchain.schema.runnable import RunnableLambda


load_dotenv()

#Set environment variables
os.environ['OPEN_API_KEY'] = os.getenv("OPENAI_API_KEY")

api_key = os.environ.get("OPENAI_API_KEY")
groq_api_key = os.environ.get("GROQ_API_KEY")

#Database Environment Variables
db_name = os.environ.get("DB_NAME")
db_password = os.environ.get("DB_PASS") 

#Initialize Groq Langchain chat object 

groq_chat2 = ChatGroq(
    groq_api_key=os.environ.get("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)


#Initialize FastAPI 
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)


#Initialize LLMs
llm_groq=groq_chat2 #model 2 (groq cloud - collection of different open source model known for its speed)

db_uri = "postgresql://postgres:" + db_password + "@localhost:5432/" + db_name

#Create sqlalchemy engine
engine = create_engine(db_uri)
conn = engine.connect()

#Create Table by executing transactions
create_table = text('''
CREATE TABLE IF NOT EXISTS "DatabaseTable10"(
customer_id INTEGER PRIMARY KEY,
name VARCHAR,
gender VARCHAR,
location VARCHAR
)
''')

#Execute the query
with engine.begin() as conn:
    conn.execute(create_table)

query1 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (1,  'Issac Newton',     'Male',    'England');''')
with engine.begin() as conn:
    conn.execute(query1)

query2 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (2,  'Marie Curie',      'Female',  'Poland');''')
with engine.begin() as conn:
    conn.execute(query2)

query3 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (3,  'Michael Faraday',  'Male',    'USA');''')
with engine.begin() as conn:
    conn.execute(query3)
query4 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (4,  'Nicholas Tesla',   'Male',    'USA');''')
with engine.begin() as conn:
    conn.execute(query4)
query5 = text('''INSERT INTO "DatabaseTable10" ("customer_id", "name", "gender", "location") VALUES (5,  'Galileo Galilei',  'Male',    'Italy');''')
with engine.begin() as conn:
    conn.execute(query5)

#Close the cursor and the database connection
conn.close()

def run_query(query, db_uri):
    #Create Engine object
    engine = create_engine(db_uri)

    #Manage connection
    with engine.connect() as conn:
        #Execute the query
        results = conn.execute(text(query)).fetchall()
        for rows in results:
            print(rows)
        conn.close()

query = 'SELECT * FROM "DatabaseTable10" LIMIT 50;'
run_query(query, db_uri)

db_connect = SQLDatabase.from_uri(db_uri)
database_chain = SQLDatabaseChain.from_llm(llm=llm_groq, db=db_connect, verbose=True, return_direct=True)


natural_results=database_chain.run("How many entries are there in the database?")
print(natural_results)

@app.post("/essay")
def generate_essay(request: dict):
    topic = request.get("topic", "")
    print("Topic1"+topic)
    return {"response": database_chain.run(topic)}

@app.post("/poem")
def generate_poem(request: dict):
    topic = request.get("topic", "")
    return {"response": database_chain.run(topic)}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

