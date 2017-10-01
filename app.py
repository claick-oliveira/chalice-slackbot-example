from chalicelib import (
    app, BOT_TOKEN, VERIFICATION_TOKEN, logger, slack_client, bot_utils
)

# Add new route / with only method POST.
@app.route('/',methods=['POST'])
def index():

    # Grab the request data.
    event = app.current_request

    # Validate the App's Token.
    if event.json_body["token"] != VERIFICATION_TOKEN:
        return bot_utils.sendStatus(403, 'application/json', {"msg":"Forbidden"})
    # Validate the Slack's challenge to register Bot Event. (need in fisrt time)
    elif "challenge" in event.json_body:
        return bot_utils.sendStatus(200, 'application/json', {"challenge":event.json_body['challenge']})
    else:
        # Grab the Sclack event data.
        slack_event = event.json_body['event']

    # Ignore the Bot's messages.
    if "bot_id" in slack_event:
        logger.warn("Ignore bot event")
        return bot_utils.sendStatus(401 ,'application/json', {"msg":"Unauthorized. Ignore bot event"})
    else:
        # Get the text of the message the user sent to the bot,
        # and reverse it.
        text = slack_event["text"]
        reversed_text = text[::-1]

        # Get the ID of the channel where the message was posted.
        channel_id = slack_event["channel"]

        # We need this informations:
        #     1. The reversed text (text)
        #     2. The channel id of the private, direct chat (channel)
        slack_client.api_call(
            "chat.postMessage",
            channel=channel_id,
            text=reversed_text,
            attachments=[]
        )

    # Everything went fine.
    return bot_utils.sendStatus(200, 'application/json', {"msg":"OK"})