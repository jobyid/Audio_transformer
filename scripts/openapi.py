import os
import openai
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import json


def query_open_ai(prompt, words):
    global d
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get("OPENKEY")
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=words)
    d = response.to_dict()
    return d, response



