import os
from dotenv import load_dotenv
import requests

load_dotenv()

class CerebrasClient:
    def __init__(self):
        self.base_url = "https://api.cerebras.ai/v1" 
        self.api_key = os.getenv("CEREBRAS_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_text(self, prompt):
        payload = {
            "model": "qwen-3-32b",
            "prompt": prompt,
            "max_tokens": 500,
            "stop": ["\n\n", "Code:", "###"],
            "temperature": 0.3 
        }
        try:
            response = requests.post(
                f"{self.base_url}/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()  # Raises HTTPError for bad responses
            result = response.json()
            
            # Debug: Print full response
            print("DEBUG API RESPONSE:", result)  # Remove after debugging
            
            if 'choices' not in result:
                return {"error": f"Unexpected response format: {result}"}
            return result
            
        except Exception as e:
            return {"error": str(e)}
