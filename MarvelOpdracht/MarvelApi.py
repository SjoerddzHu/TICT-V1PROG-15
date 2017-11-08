import requests
import time
import datetime
import hashlib
import datetime
import random
import datetime
import json
from pprint import pprint
import urllib.parse
import urllib.request

public_key= '4064284226f9e256089157d38a1a1958'
private_key= '17d325bb6bf9e0b9e67e6685276ba8ccd295e5b5'

characterAPI = 'http://gateway.marvel.com/v1/public/characters?%s'

# Functie om de data van de api op te halen
def apiHandeler_Json(APIurl):
    st = datetime.datetime.now().strftime("%Y-%m-%d%H:%M:%S")

    paramameter = {}
    paramameter['ts'] = str(time.time())
    paramameter['apikey'] = public_key
    privateKey = private_key
    paramameter['hash'] = hashlib.md5(bytes(paramameter['ts'] + privateKey + paramameter['apikey'], 'utf-8')).hexdigest()
    # q['name'] = 'Spider-Man'

    if 'characters' in APIurl:
        paramameter['offset'] = random.randrange(1492)
        paramameter['limit'] = 1

    params = urllib.parse.urlencode(paramameter)
    url = APIurl % params
    with urllib.request.urlopen(url) as f:
        data = json.load(f)
        return data

# def apiHandler_Img(APIurl):
#     return APIurl

# Hier begint de loop om een personage op te halen
check = False

    # marvelResponse = f.readlines()
while check == False:
    data = apiHandeler_Json(characterAPI)
    results = data['data']['results']
    name = results[0]['name']
    description = results[0]['description']
    thumbnailURL = results[0]['thumbnail']['path']
    imgUrl = thumbnailURL + '/portrait_xlarge.jpg'
    characterItemsLen = len(data['data']['results'][0]['events']['items'])
    characterItems = []
    try:
        characterItems = data['data']['results'][0]['events']['items'][random.randrange(characterItemsLen)]['name']
    except ValueError:
        characterItemsLen = 0
    print(name, description, imgUrl,'and appears in: ', characterItems)
    if 'image_not_available' not in imgUrl and description != '' and name != '' and characterItems != []:
        check = True



#
#
#
#
#
#
    # pprint( data)
# pprint(data['data']['results'])
# pprint(data['data']['results'][0]['events']['items'])
#
# characterItemsLen = len(data['data']['results'][0]['events']['items'])
# characterItems = data['data']['results'][0]['events']['items'][random.randrange(characterItemsLen)]['name']
# print(characterItems)
