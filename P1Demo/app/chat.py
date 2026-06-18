# This is a short file that sends queries to our basic Langchain chatbot

# Get the chain from the service
from app.services.chatbot_service import get_basic_chain, get_rag_chain

chain = get_basic_chain()

# Invoke the chain with some user input
# print(chain.invoke("How are you?").content)

# Get the RAG chain from the service and ask it about the Animals
rag_chain = get_rag_chain()

print(rag_chain.invoke("Tell me about a couple of the animals").content)