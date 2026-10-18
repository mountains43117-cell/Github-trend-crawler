import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"}
response = requests.get("https://github.com/trending",headers)
content = response.text
soup = BeautifulSoup(content,"html.parser")

biggesttotalstars = 0
bga = ""
secondbiggesttotalstars = 0
sga = ""
thridbiggesttotalstars = 0
tga = ""
allart = soup.findAll("article",attrs = {"class":"Box-row"})
for a in allart:
    totalstars = (a.find("a",attrs = {"class":"tmp-mr-3 Link Link--muted d-inline-block"})).text
    de = 0
    for i in totalstars:
        if i == "n" or i == "\\" or i == " ":
            de += 1
    totalstars = totalstars.replace(",","")
    store = int(totalstars[de+3:])
    h2 = a.find("h2")
    atag = h2.find("a")
    artname = atag["href"]
    if store > biggesttotalstars:
        biggesttotalstars = store
        bga = artname
    elif store > secondbiggesttotalstars:
        secondbiggesttotalstars = store
        sga = artname
    elif store > thridbiggesttotalstars:
        thridbiggesttotalstars = store
        tga = artname
btodaystars = 0
bgta = ""
stodaystars = 0
sgta = ""
ttodaystars = 0
tgta = ""
for a in allart:
    todaysstars = a.find("span",attrs = {"class":"d-inline-block float-sm-right"}).text
    todaysstars = todaysstars.replace(" stars today","")
    todaysstars = todaysstars.replace(" ","")
    todaysstars = todaysstars.replace(",","")
    todaysstars = int(todaysstars)
    h2 = a.find("h2")
    atag = h2.find("a")
    artname = atag["href"]
    if todaysstars > btodaystars:
        btodaystars = todaysstars
        bgta = artname
    elif todaysstars > stodaystars:
        stodaystars = todaysstars
        sgta = artname
    elif todaysstars > ttodaystars:
        ttodaystars = todaysstars
        tgta = artname
def send_to_discord(webhook_url):
    data = {"content": "Most Stars:\n"+str(biggesttotalstars)+"stars\n"+"The username and project name:"+bga+"\n"+str(secondbiggesttotalstars)+"stars\n"+"The username and project name:"+sga+"\n"+str(thridbiggesttotalstars)+"stars"+"\nThe username and project name:"+tga+"\n"+"-"*20+"\nMost Stars Today:\n"+str(btodaystars)+"stars\n"+"The username and project name:"+bgta+"\n"+str(stodaystars)+"stars\n"+"The username and project name:"+sgta+"\n"+str(ttodaystars)+"stars"+"\nThe username and project name:"+ tgta}
    requests.post(webhook_url,json=data)
print("Most Stars:")
print(str(biggesttotalstars),"stars")
print("The username and project name:",bga)
print(str(secondbiggesttotalstars),"stars")
print("The username and project name:",sga)
print(str(thridbiggesttotalstars),"stars")
print("The username and project name:",tga)
print("-"*20)
print("Most Stars Today:")
print(str(btodaystars),"stars")
print("The username and project name:",bgta)
print(str(stodaystars),"stars")
print("The username and project name:",sgta)
print(str(ttodaystars),"stars")
print("The username and project name:",tgta)
send_to_discord("https://discord.com/api/webhooks/1561323716476936293/KKNnumgruuJhqnGeNpwftsMoVUUZlm2Dvn2Fa7-HVPwb0bXc_mX-zLEJWTh7sEboYOYn")#type your webhook url here