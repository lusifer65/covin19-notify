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
    # print("enter the no of state")
    # for item in ilist[:32]:
    #     x = item.split('\n')
    #     print(f"{x[0]} {x[1]}")
    # i=input()
    state=['Uttar Pradesh','Delhi',]
    for item in ilist[:33]:
        x=item.split('\n')
        # print(x[1]+"\tcase:-"+x[2]+"\tdead:-"+x[4])
        if(x[1]=='Uttar Pradesh'):
            notification_sys("covin_19 cases in "+x[1],f"\n cases:{x[2]} Cured:{x[3]} dead:{x[4]}")
            # notification_sys("covin_19 cases in "+x[1],x[1]+"\tcase:-"+x[2]+"\tCured"+x[3]+"\tdead:-"+x[4])
        # if (x[0] == 'Total number of confirmed cases in India'):
        #     notification_sys("covin_19 cases in " + x[1], f"\n cases:{x[2]} Cured:{x[3]} dead:{x[4]}")
    time.sleep(2)