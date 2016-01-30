import random
import os
import urllib.request
import urllib.parse


class CookieMod:

    def __init__(self, client, message):
        self.client = client
        self.message = message
        self.folder = 'cookies'
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        self.img_number = len(os.listdir(self.folder))

    async def py_cookie(self):
        a = random.randint(1, self.img_number + 1)
        path = self.folder + '/' + str(a) + '.png'
        await self.client.send_file(self.message.channel, fp=path)
        
    async def py_add_cookie(self, img_url):
        try:
            filename = os.listdir(self.folder)
            last_name = filename[-1].replace('.png', '')
            new_name = str(int(last_name) + 1) + '.png'
        except IndexError:
            new_name = '1.png'
        urllib.request.urlretrieve(img_url, 'cookies/' + new_name)
