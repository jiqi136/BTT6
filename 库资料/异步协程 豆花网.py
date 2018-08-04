

import aiohttp
import asyncio
import async_timeout
from bs4 import BeautifulSoup


#信号量，控制协程数，防止爬的过快
sema = asyncio.Semaphore(3)

#解析html,获取小说书名
async def parse_html(text):
    soup = BeautifulSoup(text, 'lxml')
    items = soup.select('.subject-list .subject-item .info')
    titles = [item.find('a')['title'] for item in items]
    print(titles)

#获取html页面
async def get_html(url):
    async with aiohttp.ClientSession() as sess:
        with async_timeout.timeout(10):#设置请求的最长时间为10s
            async with sess.get(url, proxy="http://54.222.232.0:3128") as res:
                text = await res.text()
                return text


async def crawl_douban(url):
    with(await sema):
        text = await get_html(url)
        await parse_html(text)

def crawl():
    # 豆瓣小说首页
    start_url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4'
    tasks = [crawl_douban(start_url)]
    # 第2到20页的url，加入到tasks中
    for i in range(1, 20):
        url = '{}?start={}&type=T'.format(start_url, i * 20)
        tasks.append(crawl_douban(url))

    loop = asyncio.get_event_loop()
    #loop.run_until_complete(asyncio.gather(*tasks))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__ == '__main__':
    crawl()
