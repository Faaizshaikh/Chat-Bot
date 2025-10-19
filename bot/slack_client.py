import os
from slack_sdk.web import WebClient


SLACK_BOT_TOKEN = os.environ.get('SLACK_BOT_TOKEN')
client = WebClient(token=SLACK_BOT_TOKEN)




def post_message(channel, text):
client.chat_postMessage(channel=channel, text=text)




def ephemeral_response(channel, user, text):
return {
"response_type": "ephemeral",
"text": text
}




def public_response(text):
return {
"response_type": "in_channel",
"text": text
}
