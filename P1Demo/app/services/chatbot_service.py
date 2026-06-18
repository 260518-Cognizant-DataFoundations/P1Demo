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