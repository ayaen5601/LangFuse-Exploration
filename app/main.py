from llm_client import ask_llm

if __name__ == "__main__":
    question = "What is the role of Langfuse in AI observability?"
    answer = ask_llm(question)
    print(f"Answer: {answer}") 
