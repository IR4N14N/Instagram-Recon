from colorama import Fore
import requests
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print(Fore.MAGENTA+"""
 _____           _        _____
|_   _|         | |      |  __ \                     
  | |  _ __  ___| |_ __ _| |__) |___  ___ ___  _ __  
  | | | '_ \/ __| __/ _` |  _  // _ \/ __/ _ \| '_ \ 
 _| |_| | | \__ \ || (_| | | \ \  __/ (_| (_) | | | |
|_____|_| |_|___/\__\__,_|_|  \_\___|\___\___/|_| |_|
                                   """+Fore.GREEN+""" by IR4N14N   v1.1\n""")
    username = input(Fore.LIGHTCYAN_EX+"\n > "+Fore.WHITE+"Enter Username : ")
    r = requests.Session()
    res = r.get(url="https://www.instagram.com/{}/?__a=1&__d=dis".format(username))
    json = res.json()
    ReconList = ["username","fbid","edge_followed_by","edge_follow","id","full_name","biography","is_verified","is_private","is_joined_recently","is_business_account","business_category_name","business_email","business_phone_number","hide_like_and_view_counts","profile_pic_url","profile_pic_url_hd"]
    count = 1
    for i in ReconList:
        if i == "edge_followed_by":
            print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"0{}".format(count)+Fore.WHITE+"]"+Fore.LIGHTCYAN_EX+" {} : ".format("Followers")+Fore.LIGHTGREEN_EX+"{}".format(json["graphql"]['user'][f"{i}"]["count"]))
            time.sleep(0.15)
            count +=1
        elif i == "edge_follow":
            print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"0{}".format(count)+Fore.WHITE+"]"+Fore.LIGHTCYAN_EX+" {} : ".format("Following")+Fore.LIGHTGREEN_EX+"{}".format(json["graphql"]['user'][f"{i}"]["count"]))
            time.sleep(0.15)
            count +=1
        elif count<10:
            print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"0{}".format(count)+Fore.WHITE+"]"+Fore.LIGHTCYAN_EX+" {} : ".format(i)+Fore.LIGHTGREEN_EX+"{}".format(json["graphql"]['user'][f"{i}"]))
            time.sleep(0.15)
            count +=1
        elif count>=10:
            print(Fore.WHITE+"["+Fore.LIGHTYELLOW_EX+"{}".format(count)+Fore.WHITE+"]"+Fore.LIGHTCYAN_EX+" {} : ".format(i)+Fore.LIGHTGREEN_EX+"{}".format(json["graphql"]['user'][f"{i}"]))
            time.sleep(0.15)
            count +=1
try : 
    main()
except KeyboardInterrupt:
    ex = input(Fore.CYAN+"\n Press any key to Close the program ... ")
except:
    print(Fore.WHITE+"\n["+Fore.RED+"Error"+Fore.WHITE+"]"+Fore.YELLOW+" Something went wrong! Please try again after some time.")
    print(Fore.WHITE+"["+Fore.RED+"Error"+Fore.WHITE+"]"+Fore.YELLOW+" If you are using VPN, try to turn off your vpn.\n")
    ex = input(Fore.CYAN+"Press any key to Close the program ... ")
