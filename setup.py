# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 06:10:09 2021

@author: TCT
"""


def pop():
    import requests
    import json

    response = requests.get("https://ps2.fisu.pw/api/population/?world=13")
    
    nc = response.json()["result"][0]['nc']
    tr = response.json()["result"][0]['tr']
    vs = response.json()["result"][0]['vs']
    ns = response.json()["result"][0]['ns']
    
    total = nc + vs + tr + ns
    
    #print ('Sur Cobalt, il y a {} NC, {} TR, {} VS et {} NS soit {} personnes  !'.format(nc , tr , vs, ns , total))
    
    return [nc, tr, vs, ns, total]

#bot.py
import os

import time

from boto.s3.connection import S3Connection

print(os.environ)

clef = os.environ['TOKEN']

import discord



client = discord.Client()

noticeme = 'notice me senpai'

@client.event
async def on_message(message):
    author = message.author.mention
    authorid = message.author.id
    print ("@{} user sent a message. (id: {})".format(author, authorid))

    if message.content == noticeme:
        print ('I noticed you {}!'.format(authorid))
        await message.channel.send( 'I noticed you @{} !'.format(author))
        
        
    if message.content == 'pop':
        [nc , tr , vs, ns , total] = pop()
        print ('I noticed you {}!'.format(authorid))
        await message.channel.send( '{} Sur Cobalt, il y a {} NC, {} TR, {} VS et {} NS soit {} personnes  !'.format(author, nc , tr , vs, ns , total)) 
        
        while True :
            time.sleep(300)
            [nc , tr , vs, ns , total] = pop()
            print(message.channel)
            print ('I noticed you {}!'.format(authorid))
            await message.channel.send( 'Sur Cobalt, il y a {} NC, {} TR, {} VS et {} NS soit {} personnes  !'.format( nc , tr , vs, ns , total))
        
client.run(clef)

#   https://ps2.fisu.pw/api/population/?world=13

# COBALT Population#8723 is connected to the following guild:
# La Taverne skaven du complot !(id: 800818170779795486)
