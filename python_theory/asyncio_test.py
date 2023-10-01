import requests
import asyncio
from typing import Callable

## good article https://medium.com/@mecha-mind/think-twice-before-using-asyncio-in-python-7683472cb7a3

async def get_wiki_page_existence(wiki_page_url, timeout=2):
    response = requests.get(url=wiki_page_url, timeout=timeout)

    page_status = "unknown"
    if response.status_code == 200:
        page_status = "exists"
    elif response.status_code == 404:
        page_status = "does not exist"

    return wiki_page_url + " - " + page_status


async def async_get_wiki_page_existence(func:Callable, url:str):
    return await func(url)

async def geather():
    return asyncio.gather(*[async_get_wiki_page_existence(get_wiki_page_existence, url) for url in wiki_page_urls])

if __name__ == "__main__":
    wiki_page_urls = ["https://en.wikipedia.org/wiki/" + str(i) for i in range(50)]
    results = asyncio.run(geather())
    print(results)




# import aiohttp
# import asyncio


# loop = asyncio.get_event_loop()
# async def main():
#     urls = ["http://example.com/page1", "http://example.com/page2"]
#     tasks = [fetch_page(url) for url in urls]
    
#     pages = await asyncio.gather(*tasks)
    
#     for page in pages:
#         # Perform your data transformations here
#         pass
    
#     with open('output.txt', 'w') as f:
#         for page in pages:
#             f.write(f"{page}\n")

# if __name__ == "__main__":
#     loop.run_until_complete(main())