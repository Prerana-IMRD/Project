from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
print(f"API Key exists: {bool(api_key)}")

client = genai.Client(api_key=api_key)

try:
    print("Attempting to list models...")
    for m in client.models.list_models():
        print(f"Model: {m.name}")
except Exception as e:
    print(f"Error: {e}")
