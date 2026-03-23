import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Trello uses a simple Web API (REST)
# We need your Key and Token from the .env
key = os.getenv("TRELLO_API_KEY")
token = os.getenv("TRELLO_TOKEN")

url = f"https://api.trello.com/1/members/me/boards?fields=name,id&key={key}&token={token}"

response = requests.get(url)

if response.status_code == 200:
    boards = response.json()
    print("--- Your Trello Boards ---")
    for board in boards:
        print(f"Name: {board['name']} | ID: {board['id']}")
else:
    print(f"Failed to get boards. Status code: {response.status_code}")
    print(response.text)