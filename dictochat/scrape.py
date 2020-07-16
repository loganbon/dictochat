from bs4 import BeautifulSoup
import requests
import re

def getWordData(word, preview = False):

    url = 'https://www.dictionary.com/browse/' + word

    page = requests.get(url)

    if (int(page.status_code/100) != 2):
        return -1

    info = dict()

    soup = BeautifulSoup(page.content, 'html.parser')

    defs = []
    meaning = soup.find('div', class_='css-1o58fj8 e1hk9ate4').find_all('div')
    for phrase in meaning:
        phrase = phrase.find_all('span')
        [defs.append(p.get_text()) for p in phrase]
        defs = [d for d in defs if len(d) > 12]
    info['defs'] = defs

    if preview:
        return info

    phonetic = soup.find('span', class_='pron-spell-content css-z3mf2 evh0tcl2').contents
    phonetic = [c.string if type(c) != str else c for c in phonetic]
    phonetic = ''.join(phonetic)
    info['phonetic'] = phonetic

    word_type = soup.find('span', class_='luna-pos').contents
    info['type'] = word_type[0]
    
    return info

if __name__=='__main__':
    # testing...
    print(getWordData('ontology'))