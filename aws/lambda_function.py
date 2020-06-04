import json
import requests
import os
import base64
import urllib.parse

# Read in the outgoing webhook and authentication token
outgoingWebhook = os.environ["SLACK_OUTGOING_WEBHOOK"]
incomingToken = os.environ["SLACK_INCOMING_TOKEN"]

# The name of the channel we are posting too
# this is only used to tell the user where the text was sent, and will not actually change where
# the text goes, the webhook handles that
outgoingChannel = "#channel-goes-here"

def lambda_handler(event, context):

    # Parse the event values into proper fields
    # We have to use urllib to convert %21 -> ! and so on
    # The unquote_plus function also preserves spaces properly (instead of replacing them with +)
    fields = urllib.parse.unquote_plus(base64.b64decode(event["body"]).decode('utf-8')).split('&')
    keys = ['' for i in range(len(fields))]
    values = ['' for i in range(len(fields))]
    
    for i in range(len(fields)):
        keys[i], values[i] = fields[i].split('=')

    fields = dict(zip(keys, values))

    # Now print stuff for the log
    for k, v in fields.items():
        print(f'{k}: {v}')

    # Make sure the token is correct
    if not fields["token"] == incomingToken:
        print(f'Request has invalid token, returning 401 (token = {fields["token"]})')
        return {
            'statusCode': 401,
            'body': json.dumps('Invalid credentials')
        }

    # Now send the users text to the channel with a request
    # we don't want to have to wait for the request to fully go through, so we set a shorter timeout
    try:
        r = requests.post(outgoingWebhook, data=json.dumps({"text": fields["text"]}), timeout=1.)
        print(r.status_code)
    except:
        print('Request timeout (this is expected)')

    return {
        'statusCode': 200,
        'body': f'Sent message `{fields["text"]}` to {outgoingChannel}!'
    }
