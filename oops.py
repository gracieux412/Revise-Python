#--------------------------------------------------------
# without class
import requests


name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    response = ""
    #process the propmt
    return response

#--------------------------------------------------------
# with a class

class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def generate_response(self, prompt):
        # Process the prompt
        response = ""
        return response

###########################################################

# use function to illustrate use of OpenAI API response

def setup_api(key):
    return {"key": key, "base_url":"https://api.openai.com"}

def generate_response(api_config, prompt):
    
    # Make an API call
    return generate_response

api = setup_api("sk-............")
result = generate_response(api, "Explain python")