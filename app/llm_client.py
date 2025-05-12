'''OpenAi code'''

# from openai import OpenAI
# import os
# from observability import langfuse

# # Initialize OpenAI Client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def ask_llm(question: str):
#     # Start a Langfuse trace
#     trace = langfuse.trace(name="simple-llm-call", user_id="demo-user")

#     # Log the user question as a span
#     trace.span(name="user-question", input=question)

#     # Call the OpenAI LLM
#     response = client.chat.completions.create(
#         model="gpt-4.1",
#         messages=[{"role": "user", "content": question}]
#     )

#     reply = response.choices[0].message.content

#     # Log the LLM response as a span
#     trace.span(name="llm-response", output=reply)

#     return reply


'''Perplexity Mixstral code'''

# import os
# from perplexity_client import PerplexityClient
# from observability import langfuse

# # Initialize Perplexity Client
# client = PerplexityClient()

# def ask_llm(question: str):
#     # Start a Langfuse trace
#     trace = langfuse.trace(name="simple-llm-call", user_id="demo-user")

#     # Log the user question as a span
#     trace.span(name="user-question", input=question)

#     # Call the Perplexity LLM API
#     response = client.chat(
#         model="mixtral-8x7b-instruct",  # you can also try "llama-3-8b-instruct" or "llama-3-70b-instruct"
#         messages=[{"role": "user", "content": question}],
#         temperature=0.7,
#         max_tokens=512,
#     )

#     reply = response["choices"][0]["message"]["content"]

#     # Log the LLM response as a span
#     trace.span(name="llm-response", output=reply)

#     return reply



'''Groq code'''
from groq_client import GroqClient
from observability import langfuse

# Initialize Groq Client
client = GroqClient()

def ask_llm(question: str):
    # Start a Langfuse trace
    trace = langfuse.trace(name="simple-llm-call", user_id="demo-user")

    try:
        # Log the user question as a span
        trace.span(name="user-question", input=question)

        model_name = "llama3-8b-8192"

        # Call the Groq LLM API
        response, latency = client.chat(
            model=model_name,
            messages=[{"role": "user", "content": question}],
            temperature=0.7,
            max_tokens=512,
        )

        reply = response["choices"][0]["message"]["content"]

        # Log the LLM response as a span
        trace.span(name="llm-response", output=reply)

        # Extract token usage if available
        token_usage = response.get("usage", {})
        prompt_tokens = token_usage.get("prompt_tokens", None)
        completion_tokens = token_usage.get("completion_tokens", None)
        total_tokens = token_usage.get("total_tokens", None)

        # Update trace with Metadata
        trace.update(
            metadata={
                "model": model_name,
                "temperature": 0.7,
                "max_tokens": 512,
                "latency_seconds": round(latency, 2),
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens,
            }
        )

        # Log a dummy score (example: coherence or quality 1.0)
        trace.score(
            name="dummy-quality",
            value=1.0,
            comment="Auto-assigned 100% quality (replace later with real eval)"
        )

        return reply

    except Exception as e:
        # Mark trace as error if anything fails
        trace.update(status="error")
        trace.event(name="exception", input=str(e))
        print(f"Error occurred: {e}")
        raise
