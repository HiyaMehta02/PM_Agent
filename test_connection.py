import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Using the top model from your list
response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents="Tell me one thing a Senior Dev would say to a Junior Dev about using AI."
)

print(f"Gemini says: {response.text}")