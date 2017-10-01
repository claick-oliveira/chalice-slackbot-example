import os
import logging

from slackclient import SlackClient
from chalice import Chalice, Response

# Grab the Bot OAuth token from the environment.
BOT_TOKEN = os.environ["BOT_TOKEN"]

# Grab the Verification token from the environment.
VERIFICATION_TOKEN = os.environ["VERIFICATION_TOKEN"]

# Create Chalice's app.
app = Chalice(app_name='chalice-slackbot-example')

# Initializes the Slack's client.
slack_client = SlackClient(BOT_TOKEN)

# Define logging and Response
logger = logging
response = Response