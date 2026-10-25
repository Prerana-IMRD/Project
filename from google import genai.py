from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    # List all available models
    models = client.models.list_models()
    if not models:
        print("No models found.")
    for m in models:
        print(f"Model Name: {m.name}, Supported Methods: {m.supported_methods}")
except Exception as e:
    print(f"An error occurred: {e}")