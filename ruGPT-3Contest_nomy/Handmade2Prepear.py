# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 08:15:47 2020

@author: Alvl_SAM
"""

PATHRUS = './Dataset/Compile_data/Rus_Handmade.txt'
PATHSS = './Dataset/Compile_data/Social_studies_Handmade.txt'
PATHLIT = './Dataset/Compile_data/Lit_Handmade.txt'
PATHHIS = './Dataset/Compile_data/History_Handmade.txt'

PATHRUS_SAVE = './Dataset/Compile_data/Rus_Compile.txt'
PATHSS_SAVE = './Dataset/Compile_data/Social_studies_Compile.txt'
PATHLIT_SAVE = './Dataset/Compile_data/Lit_Compile.txt'
PATHHIS_SAVE = './Dataset/Compile_data/History_Compile.txt'

with open(PATHRUS, "r", encoding='utf-8') as file:
    Content = file.readlines()
file.close()
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
    

with open(PATHRUS_SAVE, 'a', encoding='utf-8') as f:
    now_esse = 0
    for eese in Essay:
        f.write("t/" + themes[now_esse] + '/t' + '\n')      
        f.write("s/" + eese[0][:eese[0].__len__() - 1] + ' ' + 
                eese[1][:eese[1].__len__() - 1] + ' ' + 
                eese[2][:eese[2].__len__() - 1] + ' ' + 
                eese[3][:eese[3].__len__() - 1] + ' ' +
                eese[4][:eese[4].__len__() - 1] + "/s" + "\n")
        now_esse += 1
        
    f.write(string)
f.close()

with open(PATHSS, "r", encoding='utf-8') as file:
    Content = file.readlines()
file.close()
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
    
with open(PATHSS_SAVE, 'a', encoding='utf-8') as f:
    now_esse = 0
    for eese in Essay:
        f.write("t/" + themes[now_esse] + '/t' + '\n')
        f.write("s/" + eese[0][:eese[0].__len__() - 1] + ' ' + 
                eese[1][:eese[1].__len__() - 1] + ' ' + 
                eese[2][:eese[2].__len__() - 1] + '/s' + '\n')
        now_esse += 1
    f.write(string)
f.close()



with open(PATHLIT, "r", encoding='utf-8') as file:
    Content = file.readlines()
file.close()
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

with open(PATHLIT_SAVE, 'a', encoding='utf-8') as f:
    now_esse = 0
    for eese in Essay:
        f.write("t/" + themes[now_esse] + '/t' + '\n')
        f.write("s/" + eese[0][:eese[0].__len__() - 1] + ' ' + 
                eese[1][:eese[1].__len__() - 1] + ' ' + 
                eese[2][:eese[2].__len__() - 1] + '/s' + '\n')
        now_esse += 1
    f.write(string)
f.close()

with open(PATHHIS, "r", encoding='utf-8') as file:
    Content = file.readlines()
file.close()
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
    

with open(PATHHIS_SAVE, 'a', encoding='utf-8') as f:
    now_esse = 0
    for eese in Essay:
        f.write("t/" + themes[now_esse] + '/t' + '\n')
        f.write("s/" + eese[0][:eese[0].__len__() - 1] + ' ' + 
                eese[1][:eese[1].__len__() - 1] + ' ' + 
                eese[2][:eese[2].__len__() - 1] + ' ' + 
                eese[3][:eese[3].__len__() - 1] + '/s' + '\n')
        now_esse += 1
    f.write(string)
f.close()

