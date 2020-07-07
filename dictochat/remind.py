from twilio.rest import Client
from dotenv import load_dotenv
import random, os
import redis

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)


dbase = redis.from_url(os.getenv('REDIS_URL'))


message = client.messages.create(
                body='Hi there!',
                from_='+15017122661',
                to='+15558675310'
            )