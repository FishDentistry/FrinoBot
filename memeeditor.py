from PIL import Image, ImageDraw, ImageFont
import os
import requests
import json

#First value is number of args, other values are positions of those args
templatedict = {"spiderman":[1,80,40],"drake":[2,300,40,300,300],"girlfriend":[3,140,530,650,350,900,200],"dipper":[2,550,400,550,1150]}

def response(givenArgs):
    templatechoice = givenArgs.split(",")[0]
    captions = givenArgs.split(",")
    captions.pop(0)

    if templatechoice not in templatedict:
        return "Error, not a valid template"
    else:
        if len(captions) < templatedict[templatechoice][0] or len(captions) > templatedict[templatechoice][0]:
            return "Wrong number of captions"
        else:
            image = Image.open("images/"+templatechoice+".jpg")
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype("Roboto-Black.ttf", size=45)

            pos1 = 1
            pos2 = 2
            for item in captions:
                message = item
                (x,y) = (templatedict[templatechoice][pos1],templatedict[templatechoice][pos2])
                color = 'rgb(0, 0, 0)'
                draw.text((x,y),message,fill=color,font=font)
                pos1 += 2
                pos2 += 2
            image.save('edited_photo.jpeg')
            data = open("edited_photo.jpeg","rb").read()
            res = requests.post(url='https://image.groupme.com/pictures',data=data,headers={'Content-Type':'image/jpeg',"X-Access-Token":'Access token goes here!'})
            res = res.json()
            print(res["payload"]["picture_url"])
            return res["payload"]["picture_url"]


#command = input("Please select desired template and provide captions")
#templatechoice =  command.split(",")[0]
#captions = command.split(",")[1:]


#if templatechoice not in templatedict:
    #print("Invalid key")
#else:
    #if len(captions) < templatedict[templatechoice][0] or len(captions) > templatedict[templatechoice][0]:
        #print ("Wrong number of captions")
    #else:
        #image = Image.open("images/"+templatechoice+".jpg")
        #draw = ImageDraw.Draw(image)
        #font = ImageFont.truetype("Roboto-Black.ttf", size=45)

        #pos1 = 1
        #pos2 = 2
        #for item in captions:
            #message = item
            #(x,y) = (templatedict[templatechoice][pos1],templatedict[templatechoice][pos2])
            #color = 'rgb(0, 0, 0)'
            #draw.text((x,y),message,fill=color,font=font)
            #pos1 += 2
            #pos2 += 2

        #image.save('edited_photo.png')

        #os.remove("edited_photo.png")
