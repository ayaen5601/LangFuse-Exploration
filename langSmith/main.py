import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq  # Import the Groq integration
from langchain_core.messages import HumanMessage  # Import message type

load_dotenv()  # Load environment variables from .env if it exists

# Get API key from environment variable
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
LANGSMITH_TRACING = os.environ.get("LANGSMITH_TRACING")
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY")
LANGSMITH_PROJECT = os.environ.get("LANGSMITH_PROJECT")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set. Please set it as an environment variable or in a .env file.")
if not LANGSMITH_TRACING:
    raise ValueError("LANGSMITH_TRACING is not set. Please set it as an environment variable or in a .env file.")
if not LANGSMITH_API_KEY:
    raise ValueError("LANGSMITH_API_KEY is not set. Please set it as an environment variable or in a .env file.")
if not LANGSMITH_PROJECT:
    raise ValueError("LANGSMITH_PROJECT is not set. Please set it as an environment variable or in a .env file.")
# Initialize the Groq chat model
llm = ChatGroq(
    model_name="llama3-70b-8192",  # Specify the LLaMA3 model
    groq_api_key=GROQ_API_KEY,  # Pass the API key
)

# Construct a list of messages.  Groq chat models expect a list of messages.
messages = [
    HumanMessage(content="What is the capital of France?")
]

# Invoke the Groq model with the messages
response = llm.invoke(messages)

# Print the response.  The response is a BaseMessage object.
print(f"Response content: {response.content}")
print(f"Response type: {type(response)}")
