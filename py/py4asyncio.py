import asyncio
import aiohttp

URL = 'https://commons.wikimedia.org/wiki/Special:Random/File'
URLS = [URL] * 100


async def coro(url):
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url)
        print("[{}] {}".format(resp.status, resp.url))

loop = asyncio.get_event_loop()
loop.run_until_complete(coro(URL))

for url in URLS:
    loop.create_task(coro(url))

pending = asyncio.Task.all_tasks()
loop.run_until_complete(asyncio.gather(*pending))
