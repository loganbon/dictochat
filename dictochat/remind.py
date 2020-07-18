from twilio.rest import Client
from dotenv import load_dotenv
import random, os, redis
import util

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
send_num = os.getenv('FROM_NUMBER')
receive_num = os.getenv('TO_NUMBER')

client = Client(account_sid, auth_token)

dbase = util.connectDBase()

keys = dbase.keys()

if keys:

    word = keys[random.randint(0,len(keys)-1)].decode('UTF-8')
    mapping = dbase.hgetall(word)

    if mapping:
        phonetic = mapping[b'phonetic'].decode('UTF-8')
        word_type = mapping[b'type'].decode('UTF-8')
        defs = mapping[b'defs'].decode('UTF-8')
        defs_str = ''.join(['- ' + line + '\n' for line in defs.split('#')])

        util.removeWord(word, dbase)
        if (mapping[b'count'] != 1):
            #mapping[b'count'] -= 1
            util.addWord(word, mapping, dbase)
            
        daily = word[0].upper() + word[1:] + ' ' + phonetic + '\n' + word_type + '\n' + defs_str

        message = client.messages.create(
                        body=daily,
                        from_=send_num,
                        to=receive_num
                    )
        print(message.sid)