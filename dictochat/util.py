import os, redis

def readVars():
    env = dict()
    with open('./config.txt', 'r') as config:
        env = {k:v for k, v in [line.strip().split("=") for line in config]}
    return env

def checkAudio():
    env = readVars()

    if (env['AUDIO'] == 'True'):
        return True
    return False

def setAudio(state):
    with open('./config.txt', 'w') as config:
        if state:
            config.write('AUDIO=True')
        else:
            config.write('AUDIO=False')

def validateWord(word):
    dbase = redis.from_url(os.getenv('REDIS_URL'))

    if (word in dbase):
        return True
    return False