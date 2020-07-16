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

    if (body.lower() == 'docs'):
        resp.message('Dictochat Usage Guide\n\nAdd [word]\nRemove [word]\nDef [word] (gets definition)\nAudio [True/False]\n(sets audio file inclusion)\n\nVersion 0.0.1')

    command = body.split(' ')[0].lower()
    text = ' '. join(body.split(' ')[1:]).lower()

    dbase = util.connectDBase()

    if (command == 'add'):
        result = scrape.getWordData(text)
        if (result != -1):
            if util.addWord(text, {}, dbase):
                preview = scrape.getWordData(text, preview=True)
                resp.message('Word successfully added.\n' + text + '\n' + preview['defs'][0])

            else:
                resp.message("Error (03):\n\nWord already exists. Text 'docs' for options.")
        else:
            resp.message("Error (02):\n\nWord not found.")

    elif (command == 'remove'):
        if (util.validateWord(text, dbase)):
            util.removeWord(text, dbase)
        else:
            resp.message("Error (03):\n\nWord not in database. Text 'docs' for options.")

    elif (command == 'audio'):
        if text in ('true', 'false'):
            util.setAudio(text)
        else:
            resp.message("Error (04):\n\nInvalid command for audio state. Text 'docs' for options.")

    else:
        resp.message("Error (00):\n\nCommand not found. Text 'docs' for options.")

    return str(resp)

if __name__=='__main__':
    app.run(port=5000, debug=True, use_reloader=False)