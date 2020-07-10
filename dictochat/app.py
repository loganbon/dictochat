from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

import os, redis
import util, scrape

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Dictochat Home Page</h1><br><a href='https://github.com/loganbon/dictochat'>Source Code</a>"

@app.route('/response', methods=['GET','POST'])
def reply():
    body = str(request.values.get('Body', None))
    resp = MessagingResponse()

    error = "Command Error \n\nText 'help' for options."

    if (body.lower() == 'help'):
        resp.message('Dictochat Usage Guide\n\nAdd [word]\nRemove [word]\nAudio [True/False]\n(toggles audio file inclusion)\n\nVersion 0.0.1')

    command = body.split(' ')[0].lower()
    text = ' '. join(body.split(' ')[1:])

    if (command == 'add'):
        result = scrape.getWordData(text)
        if (result != -1):
            # add to database if not in database
            # set response text
            pass
        else:
            resp.message("Error (02):\n\nWord not found.")

    elif (command == 'remove'):
        if (util.validateWord('text')):
            ##
        else:
            resp.message("Error (03):\n\nWord not in database. Text 'help' for options.")
        # remove from database if in database

    elif (command == 'audio'):
        # toggle audio

    else:
        resp.message("Error (00):\n\nCommand not found. Text 'help' for options.")


    dbase = redis.from_url(os.getenv('REDIS_URL'))


    return str(resp)



if __name__=='__main__':
    app.run(port=5000, debug=True, use_reloader=False)