import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', 
    default="https://statapud-3030.theiadockernext-1-labs-prod-theiak8s-4-tor01"
            ".proxy.cognitiveclass.ai"
)
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url', 
    default="https://sentianalyzer.1mrruttf5bdy.us-south.codeengine"
            ".appdomain.cloud/"
)


# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += key + "=" + value + "&"
    request_url = backend_url + endpoint + "?" + params
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Error: {e}")


# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# Add code for posting review
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Error: {e}")
