from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

import os

app = Flask(__name__)

@app.route("/response", methods=['GET','POST'])
def incoming_sms():
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    resp = MessagingResponse()

    if body == 'hello':
        resp.message("Hi!")
    else:
        resp.message("Goodbye")

    return str(resp)


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__=="__main__":
    app.run(port=5000, debug=True, use_reloader=False)