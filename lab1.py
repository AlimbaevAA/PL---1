import requests
import re

allMails =[]
urls = ['http://www.mosigra.ru/']
deep=0

main = 'http://www.mosigra.ru/'

def  findEmails (pUrl):
    print (pUrl)
    global urls
    global deep
    deep +=1
    str = requests.get(pUrl)
    if str.status_code == 200: 
        resUrl = re.findall('href="(.*?)"',str.text)
        resEmail = re.findall (r"[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",str.text)
        NewUrls = list(set(resUrl))
        NewEmails = list(set(resEmail))
        for mail in NewEmails:
            allMails.append(mail)
        if len(NewUrls) >0:
            for u in NewUrls:
                if u.find('mail') !=-1:
                    u = u[7:]
                    if u not in urls :
                        urls.append(u)
                elif len(u)>0  and u[0]=='#':
                    u='http://www.mosigra.ru/'+u
                    if u not in urls :
                        urls.append(u)
                elif u.find('pdf')!=-1 and u.find('jpg')!=-1:
                    if len(u)>0 and u[0] == '/':
                        u='http://www.mosigra.ru/'+u
                    if u not in urls :
                        urls.append(u)
                else:
                    if len(u)>0 and u[0] == '/':
                        u='http://www.mosigra.ru'+u     
                    if u not in urls:
                        urls.append(u)
                        if u[:18]=='http://www.mosigra' and deep<=3 and u.find('mode')==-1:
                            findEmails (u)
                            deep -=1
findEmails (main)
print(' ')

allMails= set(allMails)
for i in allMails:
    print (i)

