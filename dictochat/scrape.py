from bs4 import BeautifulSoup
import requests
import re

def getWordData(word):

    url = 'https://www.dictionary.com/browse/' + word

    page = requests.get(url)

    if (int(page.status_code/100) != 2):
        return -1

    info = dict()

    soup = BeautifulSoup(page.content, 'html.parser')

    phonetic = soup.find('span', class_='pron-spell-content css-z3mf2 evh0tcl2').contents
    phonetic = [c.string if type(c) != str else c for c in phonetic]
    phonetic = ''.join(phonetic)
    info['phonetic'] = phonetic

    word_type = soup.find('span', class_='luna-pos').contents
    word_type = '/'.join(word_type)
    info['type'] = word_type

    defs = []
    meaning = soup.find('div', class_='css-1o58fj8 e1hk9ate4').find_all('div')
    for phrase in meaning:
        phrase.find_all('span')
        [defs.append(p.get_text()) for p in phrase]
    info['defs'] = defs

    return info

def getWordAudio():
    return None


if __name__=='__main__':
    print(getWordData('tome'))