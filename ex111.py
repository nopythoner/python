#! /usr/bin/python

import requests
from bs4 import BeautifulSoup
import os
import datetime

dt = datetime.datetime.now()
cd = str(dt.year)+'0'+str(dt.month)+str(dt.day)
os.makedirs('Bing',exist_ok=Ture)
url = 'http://bingwallpaper.com/' 
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')
image = soup.select('.cursor_zoom img')
image_url = image[0].get('src')
res = requests.get(image_url)
with open(os.path.join('Bing',cd+'.jpg'),'wb') as file:
   file.write(res.content) 
os.system('gsettings set org.gnome.desktop.background picture-uri http://file:///home/radioactive/Bing/'+cd+'.jpg')