# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 08:15:47 2020

@author: Alvl_SAM
"""

PATHRUS = './Dataset/Compile_data/Rus_Handmade.txt'
PATHRUS_SAVE = './Dataset/Compile_data/Rus_Compile.txt'

with open(PATHRUS, "r", encoding='utf-8') as file:
    Content = file.readlines()

themes = []
Essay = []

them = False
esse = False

them_ok = False
esse_ok = False

buf_str = ""
buf_esse = []
Content_buf = []

now_string = 0;
for string in Content:
    buf_str = ""
    for char in string:
        if char == 't':
            if them == False:
                if esse == True:
                    esse = False
                    them = True
                    them_ok = True
                    esse_ok = False
                else:
                    esse = False
                    them = True
                    them_ok = True
                    esse_ok = False
            else:
                if esse == False:
                    esse = True
                    them = False
                    esse_ok = True
                else:
                    esse = True
                    them = False
                    esse_ok = True
        #print(them, esse)
        if char != '/' and char != '\n' and char != 't' and char != '\xa0':
            buf_str += char
    if len(buf_str) > 1 and them_ok == True:
        themes.append(buf_str)
        buf_str = ""
        them_ok = False

counter = 0

for string in Content:
    if len(string.split('/t')) != 1:
        Content_buf.append("s")
        counter += 1
        
    else:
        Content_buf.append(string)

for string in Content_buf:
    if string == 's':
        if len(buf_esse) != 0:
            Essay.append(buf_esse)
            buf_esse = []
    else:
        if len(string) > 2:
            buf_esse.append(string)
if len(buf_esse) != 0:
    Essay.append(buf_esse)
    buf_esse = []
    
now_esse = 0
buf_esse = []
for esse in Essay:
    if len(esse) == 7:
        buf_esse.append(esse[0] + esse[1])
        buf_esse.append(esse[2])
        buf_esse.append(esse[3])
        buf_esse.append(esse[4] + ' ' + esse[5])
        buf_esse.append(esse[6])
        Essay[now_esse] = buf_esse
        buf_esse = []
    now_esse += 1
    
    

with open(PATHRUS_SAVE, 'a', encoding='utf-8') as f:
    now_esse = 0
    for eese in Essay:
        f.write("t/" + themes[now_esse] + '/t' + '\n')
        f.write("a1/" + esse[0][:len(esse[0])-1] + '/a1' + '\n' + 
                "a2/" + esse[1][:len(esse[1])-1] + '/a2' + '\n' + 
                "a3/" + esse[2][:len(esse[2])-1] + '/a3' + '\n' + 
                "a4/" + esse[3][:len(esse[3])-1] + '/a4' + '\n' +
                "a5/" + esse[4][:len(esse[4])-1] + '/a5' + '\n')
        now_esse += 1
    f.write(string)
f.close()






























    

    