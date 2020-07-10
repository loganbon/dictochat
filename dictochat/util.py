import os, redis

def connectDBase():
    return redis.from_url(os.getenv('REDIS_URL'))

def addWord(word, mapping, dbase):
    if validateWord(word, dbase):
        return False
    # add word

def validateWord(word, dbase):
    if (word in dbase):
        return True
    return False

def readVars():
    env = dict()
    with open('./config.txt', 'r') as config:
        env = {k:v for k, v in [line.strip().split("=") for line in config]}
    return env

def getAudio():
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