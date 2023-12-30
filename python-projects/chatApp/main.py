from langchain import OpenAI, SQLDatabase
from langchain.chains import SQLDatabaseSequentialChain

username = "admin" 
password = "admin" 
host = "localhost" 
port = "5432"
mydatabase = "postgres"

pg_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{mydatabase}"
db = SQLDatabase.from_uri(pg_uri)

OPENAI_API_KEY = "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"
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo')

question = "List all known pharmacy names?" 

PROMPT = """ 
Given an input question, first create a syntactically correct postgresql query to run,  
then look at the results of the query and return the answer.  
The question: {question}
"""

db_chain = SQLDatabaseSequentialChain(llm=llm, database=db, verbose=True, top_k=3)


# use db_chain.run(question) instead if you don't have a prompt
db_chain.run(PROMPT.format(question=question))