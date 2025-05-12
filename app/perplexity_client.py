import os
import requests

class PerplexityClient:
    def __init__(self, api_key=None):
        if api_key is None:
            api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            raise ValueError("Perplexity API key is missing.")
        self.api_key = api_key
        self.base_url = "https://api.perplexity.ai"

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

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # will raise error if request fails
        return response.json()
