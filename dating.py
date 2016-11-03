import requests
import json

TOKEN = 'c6472b388a029564c0702d72f4730594'
URL = "http://challenge.code2040.org/api/dating"
VALIDATION = 'http://challenge.code2040.org/api/dating/validate'

r = requests.post(URL, json={'token':TOKEN }, headers={'Content-Type':'application/json'})

dictionary = json.loads(r.text)
print( dictionary )

datestamp = dictionary['datestamp']
interval = dictionary['interval']

#converting interval to (days hours minutes seconds)
mins = int(interval/60)
secs = interval - ( mins * 60 )
hrs = int(mins/60)
mins = mins - ( hrs * 60 )
days = int(hrs/24)
hrs = hrs - ( days * 24 )

print( days )
print( hrs )
print( mins )
print( secs )
