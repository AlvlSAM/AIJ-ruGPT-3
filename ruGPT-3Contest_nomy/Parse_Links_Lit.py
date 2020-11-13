# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 02:52:23 2020

@author: Alvl_SAM
"""

from requests import request
import time


PATH = "./Dataset/Links/Literature_links.txt"



NOW_PERCENT = 0
MAX_PERCENT = 0


with open(PATH, "r", encoding='utf-8') as file:
    contents = file.readlines()  
    MAX_PERCENT = len(contents)
for link in contents:
    t = request('GET', 'https://www.капканы-егэ.рф' + link).text
    with open('./Dataset/Downloads/Lit/' + 
              link.split('/')[5][:len(link.split('/')[5])-50] + 
              '.txt',
              'w', 
              encoding='utf-8') as f:
        f.write(t)
    f.close()
    time.sleep(0.1)
    NOW_PERCENT += 1
    print(NOW_PERCENT/MAX_PERCENT * 100, link)
        