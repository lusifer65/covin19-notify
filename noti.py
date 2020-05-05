from bs4 import *
import requests
import time
from plyer import notification
def notification_sys(title,message):
    notification.notify(
                        title=title,  #title for notification
                        message=message, #message
                        timeout=10#time out in sec
                        )
def data(url):
    r=requests.get(url)
    return r.text
while(True):
    fetch_data=data("https://www.mohfw.gov.in/")
    soup=BeautifulSoup(fetch_data,'html.parser')
    st=""
    for tr in soup.find_all('tbody')[0].find_all('tr'):
        st+=tr.get_text()
    st=st[1:]
    ilist=st.split("\n\n")
    state=['Uttar Pradesh','Delhi',] #add state 
    for item in ilist[:33]:
        x=item.split('\n')
        if(x[1] in state):
            notification_sys("covin_19 cases in "+x[1],f"\n cases:{x[2]} Cured:{x[3]} dead:{x[4]}")
    time.sleep(120) #chage time in sec 
