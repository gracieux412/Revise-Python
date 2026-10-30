import requests

class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com"

    def generate(self, prompt):
        #all logic encapsulated here
        data = requests.get()
        response = data.json()
        return response