# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:41:28 2021

LEGALINSURRECTION PARSER

legalinsurrection creates TEXT translations from court
they use some kind of blogging plugin  24liveplus

THAT SHIT IS UPSIDE DOWN AND UNREADABLE!!!
FUK!!

I AM DOING THIS PARSER TO PRODUCE NORMAL TEXTS/
oh shit it has HTML formatted blocks...
ok i am going to produce HTML



tech details:
    
    i do http get to URL
  https://data.24liveplus.com/v1/retrieve_server/x/event/2916125192049037403/news/?limit=1000&origin=https%253A%252F%252Flegalinsurrection.com

i receive JSON

i produce HTML

oh fuk  

I HATE FUKING PYTHON

@author: saaaaaaa
"""

import requests
import json
import datetime 




#counter=parsed_json['data']['count']


"""
first?
https://data.24liveplus.com/v1/retrieve_server/x/event/2916125192049037403/news/?inverted_order=1&last_nid=&limit=10&origin=https%253A%252F%252Flegalinsurrection.com


second?
https://data.24liveplus.com/v1/retrieve_server/x/event/2916125192049037403/news/?inverted_order=1&last_nid=2916401707872447131&limit=10&origin=https%253A%252F%252Flegalinsurrection.com
that NID is from [9]  of first page

looks like inverted_order is useless?

"""


longLista={}
counterLimit =40
last_nid=""


#############   OMG THIS SHIT   range (1,50)   I AM SOO LAZY but fuk it

for aaa in range (1,50):
    
    URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2916125192049037403/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counterLimit)+"&origin=https%253A%252F%252Flegalinsurrection.com"
    response = requests.get(URLO)
    parsed_json = json.loads(response.text)
    currentListSize=len(parsed_json['data']['news'])
    
       
    if parsed_json['err_code']==100:
        for i in range(0, currentListSize-1):
            longLista[parsed_json['data']['news'][i]['created']]=parsed_json['data']['news'][i]['contents']
            last_nid=parsed_json['data']['news'][i]['nid']
            print("dict size")
            print(len(longLista))

fout= open("transcript.html","w+")
fout.write('<html><body>')    
   
for key in sorted(longLista):
    fout.write(datetime.datetime.utcfromtimestamp(key).strftime('%Y-%m-%dT%H:%M:%SZ'))
    fout.write(longLista[key])
    fout.write('\n')

fout.write('</body></html>')
fout.close()