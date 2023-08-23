import requests
from requests import RequestException


# Writes the Post request as Unanet
def send_slack_message(message):
    payload = str({"text": {message}})
    try:
        response = requests.post('https://hooks.slack.com/services/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',
                                 data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.text)
    except RequestException as e:
        print("An error occurred:", e)


# This is setting the message to be "Hello World!". Once Unanet credentials are given this will
# become an API request for personnel on PTO
if __name__ == "__main__":
    message = "Hello, World!"
    send_slack_message(message)
