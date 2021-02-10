from twilio.rest import Client
from flask import Flask, request, abort
import requests
import json

from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
from pyngrok import ngrok
import time

account_sid = "ACef20baf110bb81da947fa1f862f59e19"
auth_token = "75e82d30a92ac9d6ccb2458315ecb2f4"
client = Client(account_sid, auth_token)

report_names = ["Alameda", "Santa Clara", "Contra Costa", "San Francisco", "San Mateo", "Marin", "Solano", "Sonoma",
					"Napa", "Bay Area"]

message = client.messages \
    .create(
         body="State which county you are part of from the following list: Alameda, Santa Clara, Contra Costa, San Francisco, San Mateo, Marin, Solano, Sonoma, Napa, Bay Area",
         to='+14088056887',
         from_='+19084482862'
     )

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a receipt SMS."""
    # Start our response
    resp = MessagingResponse()
# Add a message
    resp.message("Thank you for your response! We are confirming your message.")
return str(resp)

if __name__ == "__main__":
    app.run(debug=True)