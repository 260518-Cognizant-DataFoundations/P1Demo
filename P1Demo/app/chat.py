# This is a short file that sends queries to our basic Langchain chatbot

# Get the chain from the service
from app.services.chatbot_service import get_basic_chain, get_rag_chain

chain = get_basic_chain()

# Invoke the chain with some user input
# print(chain.invoke("How can I make my enemies walk the plank?").content)

# Get the RAG chain and as it about our animals
rag_chain = get_rag_chain()

print(rag_chain.invoke("What are some of the highest rated animals?").content)