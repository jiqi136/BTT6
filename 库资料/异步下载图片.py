
import asyncio
import json

import aiohttp

import motor.motor_asyncio


class Unsplash(object):
    def __init__(self):
        self.bash_url = 'https://api.unsplash.com/photos/?client_id={key}&page={page}&per_page=30'
        self.key = 'fa60305aa82e74134cabc7093ef54c8e2c370c47e73152f72371c828daedfcd7'
        self.max_page = 700
        client = motor.motor_asyncio.AsyncIOMotorClient('localhost',27017)
        db = client['unsplash']
        self.collection = db['images']

    async def get_img_info(self):
        async with aiohttp.ClientSession() as session :
            for page in range(1,self.max_page):
                async with session.get(self.bash_url.format(key = self.key,page =page )) as response:
                    await self.parse(await response.text())

    async def parse(self,response):
        json_data = json.loads(response)
        for data in json_data:
            await self.do_insert(data)

    async def do_insert(self,document):
        try:
            result = await self.collection.insert_one(document)
        except BaseException as e:
            print('error%s'%e)
        else:
            print('result %s' % repr(result.inserted_id))

    def run(self):
        loop = asyncio.get_event_loop()
        tasks = [self.get_img_info()]
        loop.run_until_complete(asyncio.wait(tasks))

if __name__ == '__main__':
    us = Unsplash()
    us.run()
