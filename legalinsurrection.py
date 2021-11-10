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
share="IDONTKNOW"

#############   OMG THIS SHIT   range (1,15)   I AM SOO LAZY but fuk it

for aaa in range (1,20):
    
    #day1
    #URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2911033984355166890/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counterLimit)+"&origin=https%253A%252F%252Flegalinsurrection.com"
    
    #day2
    #URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2911778297784733795/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counterLimit)+"&origin=https%253A%252F%252Flegalinsurrection.com"
    
    #day3  some mess in legai insur... says day 3 or 4
    #URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2912512992021483619/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counterLimit)+"&origin=https%253A%252F%252Flegalinsurrection.com"
    
    #day4 says day 4-2   some stupid charmap err
    #URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2913251050483116694/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counterLimit)+"&origin=https%253A%252F%252Flegalinsurrection.com"
    
    #day5
    URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2915432986346688614/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counterLimit)+"&origin=https%253A%252F%252Flegalinsurrection.com"
    
    #day6
    URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2916125192049037403/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counterLimit)+"&origin=https%253A%252F%252Flegalinsurrection.com"
    
    
    
    response = requests.get(URLO)
    parsed_json = json.loads(response.text)
    
    if parsed_json['err_code']==100:
        currentListSize=len(parsed_json['data']['news'])
        share=last_nid=parsed_json['data']['news'][0]['share']
        for i in range(0, currentListSize-1):
            longLista[parsed_json['data']['news'][i]['created']]=parsed_json['data']['news'][i]['newstitle']+"<br>"+parsed_json['data']['news'][i]['contents']
            last_nid=parsed_json['data']['news'][i]['nid']


print (len(longLista))

fout= open("transcript.html","w+")
fout.write('<html><body>')  
fout.write(share)
fout.write("<BR>")
   

for key in sorted(longLista):
    fout.write(datetime.datetime.utcfromtimestamp(key).strftime('%Y-%m-%dT%H:%M:%SZ'))
    fout.write(longLista[key])
    fout.write('\n')

fout.write('</body></html>')
fout.close()