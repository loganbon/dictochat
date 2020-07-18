import os, redis

def connectDBase():
    return redis.from_url(os.getenv('REDIS_URL'))

def addWord(word, mapping, dbase):
    if validateWord(word, dbase):
        return False
    
    dbase.hmset(word, mapping)
    return True

def removeWord(word, dbase):
    dbase.delete(word)

def validateWord(word, dbase):
    if (word in dbase):
        return True
    return False