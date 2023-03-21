import aiohttp


async def get_currency():
    url = 'http://nbu.uz/exchange-rates/json/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(await response.json())




