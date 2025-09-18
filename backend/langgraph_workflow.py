import os
import requests
from dotenv import load_dotenv

# Load environment variables (if using a .env file)
load_dotenv()

# Get the Hugging Face API key
HF_API_KEY = "put your api key here, preferably hugging face"
# URL of the model endpoint — you can swap this out for other models
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": HF_API_KEY  # This must include "Bearer" at the start
}

def build_workflow():
    def ai_response(user_input):
        payload = {"inputs": user_input}
        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            print("Status code:", response.status_code)
            print("Raw text:", response.text)

            # Attempt to parse response
            result = response.json()

            if isinstance(result, list) and "generated_text" in result[0]:
                return result[0]["generated_text"]

            elif isinstance(result, dict) and "error" in result:
                return f"⚠️ Hugging Face error: {result['error']}"

            else:
                return str(result)

        except Exception as e:
            return f"⚠️ API call failed: {e}"

    return ai_response
