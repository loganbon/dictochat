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

word = keys[random.randint(0,len(keys)-1)].decode('UTF-8')
mapping = dbase.hgetall(word)

if mapping:
    phonetic = mapping['phonetic'].decode('UTF-8')
    word_type = mapping['type'].decode('UTF-8')
    defs = mapping['defs'].decode('UTF-8')
    defs_str = ''.join(['- ' + line + '\n' for line in defs])

    daily = word + ' ' + phonetic + '\n' + word_type + '\n' + defs_str

    message = client.messages.create(
                    body=daily,
                    from_=send_num,
                    to=receive_num
                )

    print(message.sid)