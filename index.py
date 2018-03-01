"""
get items from sustc download page
"""
from bs4 import BeautifulSoup
import requests
import json

html = requests.get('http://sustc.edu.cn/communication_4_4_3').text
soup = BeautifulSoup(html, 'lxml')

target = soup.find_all("div", "block")

for (index, item)in enumerate(target):
    imgurl = "http://sustc.edu.cn" + item.find('img').get('src')
    name = item.find("div", "name").find("a").get_text()
    url = item.find("div", "name").find("a").get("href")
    if url[0] == '/':
        url = "http://sustc.edu.cn" + url
    pos = item.find("div", "typ").get_text().strip().replace("\t", "").split("\r\n\r\n")
    contact = item.find("div", "oth").get_text().strip().replace("\t", "").split("\r\n\r\n\r\n")
    tel = ''
    email = contact[-1]
    if len(contact) == 2:
        tel = contact[0]
    
    position = ''
    department = pos[-1]
    if len(pos) == 2:
        position = pos[0]

    params = {
        'name': name,
        'url': url,
        'src': imgurl,
        'tel': tel,
        'email': email,
        'dep': department,
        'pos': position
    }
    print(json.dumps(params))
