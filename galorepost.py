#to use this program you need to have doubanrobot library with image uploading function
#the one im using was edited so i guess you need to make your own module to get it work.

import requests
from random import randint
import doubanrobot
import time

images = open("links.txt", 'r', encoding="UTF-8").readlines()

def get_image():
    num = randint(0, len(images)-1)
    url = images[num].replace('\n', '')
    r = requests.get(url)
    with open("galore.gif", 'wb') as f:
        f.write(r.content)
    return url

def post():
    url = get_image()
    app = doubanrobot.DoubanRobot("email", "dou_password")
    files = {"image":open("galore.gif","rb") }
    app.upload_pic(files, url)
    print("Posted successfully! Now sleeping for 1 hour.")

def main():
    while True:
        try:
            post()
            time.sleep(3600)
        except:
            print("ERROR.")
            time.sleep(60)

main()
