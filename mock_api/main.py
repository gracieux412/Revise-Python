from api_util import api_setup
from client import OpenAIClient


api = api_setup("sk-.............")
client = OpenAIClient("sk-...........")

response = client.generate("Explain Python")