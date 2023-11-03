import os
import time
import json
import requests
from pystyle import *
import aiohttp
import asyncio
import datetime

from utils.console import console
from utils.spam_webhook import spam_webhook
from utils.config import config

console.fear_startup(options=True)
optioninput = input(Colorate.Horizontal(Colors.blue_to_cyan, f"                                                       -> "))



if optioninput == "1":
    console.fear_startup(options=False)
    print(Colorate.Horizontal(Colors.purple_to_blue, "\n                                           - Options-Selected - [Spam-Webhook] -"))
    time.sleep(0.5)
    print(Colorate.Horizontal(Colors.blue_to_purple, f"\n                                               Process Started - [{datetime.datetime.now().strftime('%H:%M:%S')}]"))
    try:
        asyncio.run(spam_webhook.main())
    except aiohttp.ClientError as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, e))



elif optioninput == "2":
    console.fear_startup(options=False)
    print(Colorate.Horizontal(Colors.purple_to_blue, "\n                                         - Options-Selected - [Delete-Webhook] -"))
    requests.delete(config.read()['webhook'])
    check = requests.get(config.read()['webhook'])

    if check.status_code == 404:
        print(Colorate.Horizontal(Colors.green_to_cyan, "                                               Webhook Succesfully Deleted"))
        time.sleep(5)
        os._exit(0)

    elif check.status_code == 200:
        print(Colorate.Horizontal(Colors.red_to_yellow, "                                               Failed To Delete Webhook"))
        time.sleep(5)
        os._exit(0)



else:
    console.fear_startup(options=False)
    print(Colorate.Horizontal(Colors.red_to_yellow, "                                           Invalid option, exiting in 5 seconds"))
    time.sleep(5)
    os._exit(0)