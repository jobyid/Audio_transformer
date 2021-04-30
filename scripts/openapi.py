import os
import openai
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import json
from scripts import eaxmples as ex


def query_open_ai(prompt, words):
    global d
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get("OPENKEY")
    response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=words, temperature=0.5)
    d = response.to_dict()
    return d, response

def classfiy(prompt, classifications):
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get("OPENKEY")

    lab = classifications
    response = openai.Classification.create(model="davinci",
                                            query=prompt,
                                            labels=lab,
                                            search_model="ada",
                                            examples=ex.examples)
    d = response.to_dict()
    return d, response

