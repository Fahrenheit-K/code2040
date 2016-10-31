import requests
import json

TOKEN = 'c6472b388a029564c0702d72f4730594'
URL = 'http://challenge.code2040.org/api/haystack'
VALIDATION = 'http://challenge.code2040.org/api/haystack/validate'

r = requests.post(URL, data={'token':TOKEN})
dictionary = json.loads(r.text)

needle = dictionary['needle']
haystack = dictionary['haystack']


index = -1

for i in range( 0, len(haystack) ):

    word = haystack[ i ]

    if needle == word:
        index = i
        break

r2 = requests.post(VALIDATION, data={'token':TOKEN, 'needle':index})
