from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyme(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:/Users/Dell/icon.ico",
        timeout = 15
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__=="__main__":
    while True:
        #notifyme("Aditya", "Let's stop the spread of this virus together")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        #print (soup.prettify())
        myDataStr = ""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Maharashtra','West Bengal','Delhi']
        for item in itemList[0:32]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print (dataList)
                nTitle = 'Cases of Covid-19'
                nText = f"State: {dataList[1]}\nTotal : {dataList[2]}\n Cured : {dataList[3]}\n Deaths : {dataList[4]}"
                notifyme(nTitle,nText)
                time.sleep(2)
        time.sleep(10)            








