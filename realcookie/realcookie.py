import random
import os
import urllib.request
import shutil


class cookie:

    def __init__(self):
        self.folder = 'cookies'
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        self.img_number = len(os.listdir(self.folder))

    # returns the path to a random cookie in the cookies folder
    def gib(self):
        a = random.randint(1, self.img_number + 1)
        path = self.folder + '/' + str(a) + '.png'
        return path

    # dowloads a cookie from image url to the cookies file    
    def add(self, img_url):
        try:
            filename = os.listdir(self.folder)
            last_name = filename[-1].replace('.png', '')
            new_name = str(int(last_name) + 1) + '.png'
        except IndexError:
            new_name = '1.png'
        urllib.request.urlretrieve(img_url, self.folder + '/' + new_name)

    # returns the number of cookie images in the folder
    def count(self):
        return self.img_number

    # deletes all the images and the folder. usefull for resets
    def rm(self):
        shutil.rmtree(self.folder)
