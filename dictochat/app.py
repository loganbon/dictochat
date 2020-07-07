from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

import os, scrape, redis

load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Dictochat Home Page</h1><br><a href='https://github.com/loganbon/dictochat'>Source Code</a>"

@app.route('/response', methods=['GET','POST'])
def reply():
    body = request.values.get('Body', None)
    resp = MessagingResponse()

    if (str(body).lower() == 'help'):
        resp.message('Dictochat Usage Guide\n\nAdd [word]\nRemove [word]\nAudio [True/False]\n(toggles audio file inclusion)\n\nVersion 0.0.1')

    if (str(body).lower() == 'audio'):
        dbase = redis.from_url(os.getenv('REDIS_URL'))


    ## TODO
    # scrape dicts
    # check if word in database
    # help functionality



    return str(resp)

def validateWord(word):

    dbase = redis.from_url(os.getenv('REDIS_URL'))

    if (word in dbase):
        return True
    
    return False

if __name__=='__main__':
    app.run(port=5000, debug=True, use_reloader=False)