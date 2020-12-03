import os
import requests
from datetime import datetime

def response(givenDate):
	api_key = 'API key goes here!' #Change this to config var
	url_apod = "https://api.nasa.gov/planetary/apod"
	if givenDate == "today":
		date = datetime.today().strftime('%Y-%m-%d')
	else:
		date = givenDate
	params = {'api_key':api_key,'date':date,'hd':'True'}
	response = requests.get(url_apod,params=params).json()
	explanation = response["explanation"]
	firstpart = explanation[0:450]
	secondpart = explanation[450:len(explanation)-1]
	return "Nasa Image of the Day:",response["hdurl"],firstpart,secondpart

