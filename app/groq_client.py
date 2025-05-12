import os
import requests
import time

class GroqClient:
    def __init__(self, api_key=None, max_retries=1):
        if api_key is None:
            api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("Groq API key is missing.")
        self.api_key = api_key
        self.base_url = "https://api.groq.com/openai/v1"
        self.max_retries = max_retries

    def chat(self, model: str, messages: list, temperature: float = 0.7, max_tokens: int = 512):
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        retries = 0
        while retries <= self.max_retries:
            try:
                start_time = time.time()
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status()
                latency = time.time() - start_time
                return response.json(), latency
            except requests.RequestException as e:
                if retries < self.max_retries:
                    retries += 1
                    print(f"Retrying Groq API call... attempt {retries}")
                    time.sleep(1)  # wait 1 second before retry
                else:
                    raise e
