
import requests

TOKEN = 'c6472b388a029564c0702d72f4730594'
URL = 'http://challenge.code2040.org/api/reverse'
VALIDATION = 'http://challenge.code2040.org/api/reverse/validate'

r = requests.get(URL)
r = requests.post(URL, data={'token':TOKEN} )

string = r.text

new_string = ''

for i in range(0, len(string) ):
    new_string = new_string + string[ len(string) - 1 - i ]

r2 = requests.get( VALIDATION )
r2 = requests.post( VALIDATION, data={'token':TOKEN,'string':new_string} )
