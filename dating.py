import requests
import json

TOKEN = 'c6472b388a029564c0702d72f4730594'
URL = "http://challenge.code2040.org/api/dating"
VALIDATION = 'http://challenge.code2040.org/api/dating/validate'

r = requests.post(URL, data={'token':TOKEN })

dictionary = json.loads(r.text)
print( dictionary )
