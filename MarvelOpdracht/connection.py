import requests
import time
import unicodedata
public_key= '4064284226f9e256089157d38a1a1958'
private_key= '17d325bb6bf9e0b9e67e6685276ba8ccd295e5b5'
maxchar = 1500

import hashlib
m = hashlib.md5()
import base64


# TimeStamp = TimeStamp + 1



GoingToBeHased = str(time.time()) + private_key + public_key


ByteGoingToBeHased = str.encode(GoingToBeHased)
type(ByteGoingToBeHased)
#GoingToBeHased.encode('utf-8')
# GoingToBeHased = base64.b64encode(GoingToBeHased)
print(GoingToBeHased,"bovenste")
print(ByteGoingToBeHased,"onderste")
m.update(GoingToBeHased.encode('utf-8'))
print(m.hexdigest(),"test")




api_url = ('https://gateway.marvel.com:443/v1/public/characters?limit=1&offset=1&apikey=',public_key)
hash = m.hexdigest()
#
# Params = {
#   "apikey": "17d325bb6bf9e0b9e67e6685276ba8ccd295e5b5",
#   "ts": time.time(),
#   "hash": str(time.time()) + '4064284226f9e256089157d38a1a1958' + '17d325bb6bf9e0b9e67e6685276ba8ccd295e5b5'
# }
#auth_details = ('Jouw API-gebruikersnaam', 'Jouw API-wachtwoord')
# response = requests.get(api_url)
# print(response.text)


#Request Url: http://gateway.marvel.com/v1/public/comics
#Request Method: GET
#Params: {
#  "apikey": "your api key",
#  "ts": "a timestamp",
#  "hash": "your hash"
#}
#Headers: {
#  Accept: */*
#}
#
#
#Request: GET http://gateway.marvel.com/v1/public/comics?apikey=yourAPIKEY
#Response:
#{
#  "code": 200,
#  "status": "Ok",
#  "etag": "f0fbae65eb2f8f28bdeea0a29be8749a4e67acb3",
#  "data": {
#  … [other data points]
#}
