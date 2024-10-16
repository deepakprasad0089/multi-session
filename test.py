import aiohttp 
import asyncio 
 
proxies_list = open("rotating_proxies_list.txt", "r").read().strip().split("\n") 
timeout = aiohttp.ClientTimeout(total=30) 
 
async def get(url, session, proxy): 
	try: 
		async with session.get(url, proxy=f"http://{proxy}", timeout=timeout) as response: 
			print(response.status, await response.text()) 
	except Exception as e: 
		print(e) 
 
async def check_proxies(): 
	proxy = proxies_list.pop() 
	async with aiohttp.ClientSession() as session: 
		await get("http://ident.me/", session, proxy=proxy) 
 
asyncio.run(check_proxies())