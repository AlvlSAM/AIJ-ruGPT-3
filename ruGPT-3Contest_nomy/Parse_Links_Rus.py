# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:34:22 2020

@author: Alvl_SAM
"""

from requests import request
import os
import time


PATH = "./Dataset/"

LINKS = PATH + "Links"

NOW_PERCENT = 0
MAX_PERCENT = 0


files = os.listdir(LINKS)


for file in files:
    with open(PATH + 'Links/' + file, "r", encoding='utf-8') as file:
        contents = file.readlines()  
        MAX_PERCENT = len(contents)
    for link in contents:
        t = request('GET', 'https://www.капканы-егэ.рф' + link).text
        with open(PATH + 
                  'Downloads/Rus/' + 
                  link.split('/')[4][:len(link.split('/')[4])-1] + 
                  '.txt',
                  'w', 
                  encoding='utf-8') as f:
            f.write(t)
        f.close()
        time.sleep(0.1)
        NOW_PERCENT += 1
        print(NOW_PERCENT/MAX_PERCENT * 100, link)
        