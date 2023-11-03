import aiohttp
import asyncio
import json
from pystyle import *

from utils.config import config

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

data = {
    "content": config.read()['content'],
    "embeds": [
        {
            "color": config.read()['color'],
            "fields": config.read()['fields'],
            "author": {
                "name": config.read()['author']
            },
            "footer": {
                "text": config.read()['footer']['text'],
                "icon_url": config.read()['footer']['icon_url']
            }
        }
    ],
    "username": config.read()['username'],
    "avatar_url": config.read()['avatar_url'],
    "attachments": config.read()['attachments']
}

class spam_webhook():
    async def LoadUrl(session, webhook, data=None, headers=None, proxy=None):
        try:
            if headers != '':
                async with session.post(webhook, data=data, headers=headers, proxy=proxy) as r:
                    return await r.text(), r.status
            else:
                async with session.post(webhook, data=data, proxy=proxy) as r:
                    return await r.text(), r.status
        except aiohttp.ClientError as e:
            return str(e), None
        except AttributeError:
            return "Transport object not available", None
        
    async def main():
        proxy_url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=30000&country=all&simplified=true'

        while True:
            async with aiohttp.ClientSession() as session:
                proxy_response = await session.get(proxy_url)
                if proxy_response.status == 200:
                    proxies = await proxy_response.text()
                    proxies = proxies.split('\n')

                    tasks = []
                    for proxy in proxies:
                        if proxy.strip():
                            proxy_str = 'http://' + proxy.strip()
                            task = asyncio.create_task(
                                spam_webhook.LoadUrl(session, config.read()['webhook'], data=json.dumps(data), headers=headers,
                                        proxy=proxy_str))
                            tasks.append(task)

                    responses = await asyncio.gather(*tasks)

                else:
                    print(Colorate.Horizontal(Colors.red_to_yellow, "Failed to retrieve proxies"))

            await asyncio.sleep(5)  # Wait for 5 seconds before sending the next batch of requests