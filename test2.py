import asyncio
import aiohttp

sites = ['https://chelseafc.3ddigitalvenue.com/login']

async def fetch(site):
    print('Fetching: ' + site)

    async with aiohttp.ClientSession() as session, \
            session.get(site) as response:
        return await response.text()

async def main():
    t = []

    for site in sites:
        task = asyncio.create_task(fetch(site))
        t.append(task)
    await asyncio.gather(*t)