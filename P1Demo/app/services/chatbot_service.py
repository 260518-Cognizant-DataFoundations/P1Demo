# This service will contain the logic for our LLM interactions with Langchain
# This is where our chatbot functionality lives!
# This could arguably be a util instead, but I plan to hit the DB from here
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# define the LLM - Large Language Model - basically "what chatbot are you using"
llm = ChatOllama(
    model="llama3.2:3b" # The name of the model we're using
)

# Prompt Engineering - we're telling our chatbot how to speak and what to say or not say
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful chatbot and you sound like a pirate"),
    ("human", "{input}")
])

# Make a basic chain that lets us talk to the LLM
def get_basic_chain():
    chain = prompt | llm
    return chain


# =======================================

"""
This time, we're doing to accomplish RAG (Retrieval Augmented Generation)

RAG is the practice of supplying extra data to the LLM to improve its response
Llama3.2 is powerful but it knows nothing about our Animal data unless we supply it

So, let's supply it with data so it's better equipped to answer questions about our app
"""

# First, import and select the animals from the repo
import app.repositories.animal_repository as repo
animals = repo.get_all_animals()

# Now, a new prompt that supplies the animal data to the LLM
prompt2 = ChatPromptTemplate.from_messages([
    ("system", """
    You are a helpful zookeeper with knowledge about the animals in a SQL table.
    You are a little TOO enthusiastic about animals
    
    You are helpful, but concise and you don't answer questions that aren't about the data
    
    Here is your data: {animals}
    """),
    ("human", "{input}")
])

# Make a new chain with the new prompt
def get_rag_chain():
    # partial() lets us input values for the prompt variables
    chain = prompt2.partial(animals=animals) | llm
    return chain