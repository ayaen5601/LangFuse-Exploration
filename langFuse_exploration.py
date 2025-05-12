# Import Langfuse SDK
import os
from langfuse import Langfuse

langfuse = Langfuse(
  
  host="http://localhost:3000"
)

# print(f"Langfuse Auth Check : {langfuse.auth_check()}")

# # Log a sample trace
# trace = langfuse.trace(
#     name="Sample Trace",
#     input={"question": "What is Langfuse?"},
#     output={"answer": "Langfuse is an observability tool for LLMs."},
#     metadata={"example": True}
# )

# print("Langfuse trace logged successfully!")

from langfuse.decorators import observe
from langfuse.openai import openai # OpenAI integration
 

client = openai.OpenAI(
)
