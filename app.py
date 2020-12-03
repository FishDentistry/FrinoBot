
import os
import json
import random
import requests
import nasa
import lmgtfy
import betarave
import memeeditor
import catfact

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

#A list for storing humorous fun facts for the bot to say. A "rick roll" example is provided here.
frinofacts = ["Frino says: Visit this link- https://youtu.be/dQw4w9WgXcQ"]

#The trigger words for the fun facts.
trigger_words = ["Frino","frino","Fronk","fronk","Evolve","evolve","Sophomore","sophomore",
"Sophomores","sophomores","House","house","Chapter","chapter"]




prefix = "/FrinoBot"

groupID = 'Group ID goes here!' 
token = 'Access token goes here!'
userID = 'User ID goes here!'

authorized_users = ["Christian Fronk"]


app = Flask(__name__)
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  choice = random.randint(0,(len(frinofacts)-1))

  # We don't want to reply to ourselves! 
  if data['name'] != 'FrinoBot': 
    	parseMessage(data['name'],data['text'],choice,data['user_id'])
    	

  return "ok", 200
def send_message(msg):
  url = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'), 
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()

def parseMessage(name,message,choice,userid):
	if  (name == "Jordan Sigal"):
		msg = "Reminder- Sigal is no longer top 100 in smash!"
		send_message(msg)
	elif message.startswith(prefix):
		commandProtocol(message,name,userid)
	elif any(trigger_word in message for trigger_word in trigger_words):
		msg = "Frino fact! Did you know? " + frinofacts[choice]
		send_message(msg)
	elif "#notbusiness" in message:
		send_message("Business schmizness")

def commandProtocol(message,name,userid):
	if "kill" in message and (userid == userID): 
		msg = "Kill activated"
		target = message.split("#")[1]
		send_message(msg)
		membership_id = getMemberID(target)
		killProtocol(membership_id)
	elif "cat fact" in message:
		msg = catfact.response()
		send_message(msg)
	elif "nasa" in message:
		target = message.split(" ")[2]
		msg,msg2,msg3,msg4= nasa.response(target)
		send_message(msg)
		send_message(msg2)
		send_message(msg3)
		send_message(msg4)
	elif "lmgtfy" in message:
		target = message.split("#")[1]
		link = lmgtfy.response(target)
		send_message(link)
	elif "betarave" in message:
		target = message.split("#")[1]
		ravemessage = betarave.response(target)
		send_message(ravemessage)
	elif "meme" in message:
		target = message.split("#")[1]
		mememessage = memeeditor.response(target)
		send_message(mememessage)
def killProtocol(member):
	url = 'https://api.groupme.com/v3/groups/'+groupID+'/members/'+member+'/remove?token='+token
	requests.post(url)

def getMemberID(name):
	memberID = 0
	url = 'https://api.groupme.com/v3/groups/'+groupID+'?token='+token 
	r = requests.get(url=url)
	data = r.json()
	for item in data['response']['members']:
		if item['name'] == name:
			memberID = item['id']
	if memberID != 0:
		return memberID
	else:
		send_message('Error- Invalid name!')








		




