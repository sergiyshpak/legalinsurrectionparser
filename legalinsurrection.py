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


#  shit it paged by 50 entries????  and that web page gets them by 10
counter =40

last_nid=""




#retenhouse day 6
URLO="https://data.24liveplus.com/v1/retrieve_server/x/event/2916125192049037403/news/?inverted_order=1&last_nid="+last_nid+"&limit="+str(counter)+"&origin=https%253A%252F%252Flegalinsurrection.com"

response = requests.get(URLO)
parsed_json = json.loads(response.text)

#print(parsed_json)

# {"err_code": 100, "err_msg": "Success", "data": {"news": [{"nid": "2916406705150782110", "newstitle": "Court Recesses for the Day", "contents": "<p><br><\/p>", 

#print(parsed_json['data']['news'][3])








print (counter)
print ("-----------------------------")
print(parsed_json['data']['news'][counter-i]['nid'])
print ("-----------------------------")

for i in range(1, counter+1):
    
    #print(counter-i)
    
    #print(parsed_json['data']['news'][counter-i])
    """
    {'nid': '2916406618640257128', 'newstitle': '', 
    'contents': '<p><span style="background-color: rgba(0, 0, 0, 0.03); color: rgb(15, 20, 25);">That\'s it for defense witness Zanin.</span></p><p><br></p><p><span style="background-color: rgba(0, 0, 0, 0.03); color: rgb(15, 20, 25);">Court recesses for the day.</span></p>', 
    'created': 1636497735, 'lastupdate': 0, 'uid': '2748969211805265551', 
    'editorname': 1, 'uname': 'andrew', 'avatar': 'avatar/2748969211805265551/20210329135608_015360.png',
    'avatar_url': 'https://24liveblog.tradingfront.cn/avatar/2748969211805265551/20210329135608_015360.png', 
    'news_type': 0, 'likes': 0, 'cmts_all_count': 0, 
    'share': 'https://legalinsurrection.com/2021/11/live-rittenhouse-trial-day-6/', 'duration': 0, 
    'liveid': '', 
    'background': '', 
    'action_info': {}, 
    'interval': 5, 'options': [], 
    'voting_count': 0, 'comments_count': 0, 'comments': [], 
    'admin_level': 1, 'widget': {}}
    """
    
   ##### print(datetime.datetime.utcfromtimestamp(parsed_json['data']['news'][counter-i]['created']).strftime('%Y-%m-%dT%H:%M:%SZ'))
    #print(datetime.utcfromtimestamp(parsed_json['data']['news'][counter-i]['created']).strftime('%Y-%m-%d %H:%M:%S'))
    ####  print(parsed_json['data']['news'][counter-i]['contents'])
    
    
    longLista[parsed_json['data']['news'][counter-i]['created']]=parsed_json['data']['news'][counter-i]['contents']

    
 

fout= open("transcript.html","w+")
fout.write('<html><body>')    
   
for key in sorted(longLista):
    fout.write(datetime.datetime.utcfromtimestamp(key).strftime('%Y-%m-%dT%H:%M:%SZ'))
    fout.write(longLista[key])
    fout.write('\n')

fout.write('</body></html>')
fout.close()