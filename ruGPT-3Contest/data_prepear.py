# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 01:04:59 2020

@author: Alvl_SAM
"""
import os



PATH = './Dataset/'

def read_dataset(): 
    contents = []
    Quest = []
    Essay = []
    Subject = []
    
    buf_Quest = ""
    buf_Essay = ""
    
    Quest_read = False
    End_Quest_read = True
    
    Essay_read = False
    End_Essay_read = True
    
    files = os.listdir(PATH)
    for file in files:    
        with open(PATH + file, "r", encoding='utf-8') as file:
            contents = file.readlines()
            for line in contents:
                for character in line:
                    if character == 't':
                        if Quest_read:
                            if len(buf_Quest) != 0:
                                Quest.append(buf_Quest)
                                print(file.name)
                                if file.name.split('/')[2] == "social_studies_train.txt":
                                    Subject.append("Предмет: Обществознание")
                                buf_Quest = ""
                            Quest_read = False
                            End_Quest_read = True
                        else:
                            Quest_read = True
                    if character == 's':
                        if Essay_read:
                            if len(buf_Essay) != 0:
                                Essay.append(buf_Essay)
                                buf_Essay = ""
                            Essay_read = False
                            End_Essay_read = True
                        else:
                            Essay_read = True
                                               
                    if character == '/':
                        if Quest_read:
                            End_Quest_read = False
                        if Essay_read:
                            End_Essay_read = False
                            
                    if End_Quest_read == False and character != '/':
                        buf_Quest += character
                        
                    if End_Essay_read == False and character != '/':
                        buf_Essay += character

    return Subject, Quest, Essay




Subjects, Themes, Essay = read_dataset()
i = 0
out = ""
out_ = ""
for them in Themes:
    #print(them, Essay[i])
    if i < 90:
        esse = "<s>" + Subjects[i] + '\n'
        esse += "Тема: " + them + '\n'
        esse += "Сочинение: " + Essay[i] + "</s>" + '\n'
        out += esse
        i = i + 1
    else:
        esse = "<s>" + Subjects[i] + '\n'
        esse = "Тема: " + them + '\n'
        esse += "Сочинение: " + Essay[i] + "</s>" + '\n'
        out_ += esse
        i = i + 1


with open("train.txt", "w") as file:
    file.write(out)



with open("valid.txt", "w") as file:
    file.write(out_)















