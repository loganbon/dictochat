def checkAudio():
    with open('./config.txt', 'r') as config:
        env = {k:v for k, v in [line.strip().split("=") for line in config]}

    if (env['AUDIO'] == 'True'):
        return True
    return False

def setAudio(state):
    with open('./config.txt', 'w') as config:
        if state:
            config.write('AUDIO=True')
        else:
            config.write('AUDIO=False')