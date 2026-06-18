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

# Make a prompt + chain that answers questions about Animals in our DB-----
# This is an example of RAG - giving the LLM access to data that it may not have been trained on
# In this case, the data is our animal database

# First, let's get the animals from the repo
import app.repositories.animal_repository as repo
animals = repo.get_all_animals()

# Now define a new prompt that uses our animal data
prompt2 = ChatPromptTemplate.from_messages([
    ("system", """You are a zoo employee with knowledge about the animals you work with
    You have access to a database of animals and their information.
    You ONLY respond to questions about the data, and don't make up answers.
    
    Here's your data:
    {animals}
    """),
    ("human", "{input}")
])

# Make a new chain that behaves differently from the basic chain
def get_rag_chain():
    # Make a chain that gives the LLM access to our animal data
    # partial() lets us pre-fill the animals variable in the prompt with our animal data
    chain = prompt2.partial(animals=animals) | llm
    return chain