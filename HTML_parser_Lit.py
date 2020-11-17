# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 03:03:37 2020

@author: Alvl_SAM
"""

import os



SAVE_LIT = './Dataset/Compile_data/Lit_Split.txt'

LINKS_LIT = './Dataset/Links/Literature_links.txt'
LIT_DATA_HTML = './Dataset/Downloads/Lit/'


Theme = []

Essay = []
esse = []

with open(LINKS_LIT, "r", encoding='utf-8') as file:
    Links = file.readlines() 
file.close()

files = os.listdir(LIT_DATA_HTML)

for now_html in files:
    with open(LIT_DATA_HTML + now_html, "r", encoding='utf-8') as file:
            contents = file.readlines() 
            Theme.append(contents[514])
            esse = []
            
            for i in range(100, 1000):
                if (len(contents[i].split('<div id="podpiska">'))) != 1:
                    break
            for ii in range(i, 100, -1):
                if contents[ii] == " </div>" + '\n' or contents[ii] == "		</h2>" + '\n':
                    break
            for iii in range(ii+1, i):
                esse.append(contents[iii])
            #print(RUS_DATA_HTML + now_html, esse)
            Essay.append(esse)
                
    file.close()
    
now_them = 0
buffer = ""

for them in Theme:
    buffer = ""
    for char in them:
        if char == '<':
            break
        if char != '\t':
            buffer += char
    Theme[now_them] = buffer
    now_them += 1

buf_esse = []
now_them = 0
eese = []
for eese in Essay:
    buf_esse = []
    for string_ in eese:
        if len(string_.split('</p>')) != 1:
            buf_esse.append(string_)
            #print(string_)
    Essay[now_them] = buf_esse
    now_them += 1

now_them = 0
scobka = False
start = False

for eese in Essay:
    buf_esse = []
    for string_ in eese:
        buf_str = ""
        start = False
        for char in string_:
            if char != '\t':  
                if char == ' ' and start == False:
                    print("GHJ<TK <K")
                else:
                    if char == '<':
                        scobka = True
                    if (ord(char) < 65 or ord(char) > 90) and (ord(char) < 97 or ord(char) > 123) and char != '&' and char != ';' and scobka == False:
                        buf_str += char
                        start = True
                    if char == '>':
                        scobka = False
                
        #print(buf_str)
        buf_esse.append(buf_str)
    Essay[now_them] = buf_esse
    now_them += 1
    
now_them = 0

for them in Theme:
    buf_str = ""
    for char in them:
        if (ord(char) < 65 or ord(char) > 90) and (ord(char) < 97 or ord(char) > 123) and char != '&' and char != ';':
            buf_str += char
    
    Theme[now_them] = buf_str
    now_them += 1

now_them = 0
now_sep = 1
mass = []

cout = 0
now_them = 0

for esse in Essay:
    
    now_sep = 1
    for string in esse:
        if len(string) > 2:    
            now_sep += 1
    if now_sep < 15 and now_sep > 4:   
        with open(SAVE_LIT, 'a', encoding='utf-8') as f:    
            f.write("t/" + Theme[now_them] + '/t' + '\n')
            
        f.close()
        for string in esse:
            with open(SAVE_LIT, 'a', encoding='utf-8') as f:
                f.write(string)
            f.close()
    now_them += 1
    print(now_them, now_sep)
    if now_sep < 40 and now_sep > 1:
        cout += 1
        mass.append(now_sep)
    print (cout)
    
import matplotlib.pyplot as plt
plt.plot(mass)
plt.show()
    