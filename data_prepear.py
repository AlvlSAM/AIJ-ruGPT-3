# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 01:04:59 2020

@author: Alvl_SAM
"""
import os
import random


PATH_IMPORT = './Dataset/Compile_data/Compile/'
PATH_EXPORT = './Dataset/Compile_data/TrainTest/'

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
    
    files = os.listdir(PATH_IMPORT)
    for file in files:    
        with open(PATH_IMPORT + file, "r", encoding='utf-8') as file:
            contents = file.readlines()
            for line in contents:
                for character in line:
                    if character == 't':
                        if Quest_read:
                            if len(buf_Quest) != 0:
                                Quest.append(buf_Quest)
                                print(file.name)
                                if file.name.split('/')[4] == "Social_studies_Compile.txt":
                                    Subject.append("Предмет: Обществознание")
                                if file.name.split('/')[4] == "Rus_Compile.txt":
                                    Subject.append("Предмет: Русский язык")
                                if file.name.split('/')[4] == "Lit_Compile.txt":
                                    Subject.append("Предмет: Литература")
                                if file.name.split('/')[4] == "History_Compile.txt":
                                    Subject.append("Предмет: История")
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
        file.close()

    return Subject, Quest, Essay




Subjects, Themes, Essay = read_dataset()
i = 0
out = ""
out_ = ""
Dataset = []
for them in Themes:
    #print(them, Essay[i])
    esse = "<s>" + Subjects[i] + '\n'        
    esse += "Тема: " + them + '\n'
    esse += "Сочинение: " + Essay[i] + "</s>" + '\n'
    Dataset.append(esse)
    i += 1


random.shuffle(Dataset)


i = 0

valid = []
train = []

for data in Dataset:
    if i < 10:
        valid.append(data)
        i += 1
    else:
        train.append(data)



with open(PATH_EXPORT + "valid.txt", "a") as file:
    for data in valid:  
        file.write(data)
file.close()

with open(PATH_EXPORT + "train.txt", "a") as file:
    for data in train:  
        file.write(data)
file.close()




# with open(PATH_EXPORT + "train.txt", "a") as file:
#     for data in Dataset:  
#         if i < 10:
#             file.write(data)
#         i += 1
# file.close()




# i = 0

# SS = []
# Lit = []
# Rus = []
# His = []
# for them in Themes:
#     #print(them, Essay[i])
#     if Subjects[i] == "Обществознание":    
#         esse = "<s>Тема: " + them + '\n'
#         esse += "Сочинение: " + Essay[i] + "</s>" + '\n'
#         SS.append(esse)
#     if Subjects[i] == "Русский язык":    
#         esse = "<s>Тема: " + them + '\n'
#         esse += "Сочинение: " + Essay[i] + "</s>" + '\n'
#         Rus.append(esse)
#     if Subjects[i] == "Литература":    
#         esse = "<s>Тема: " + them + '\n'
#         esse += "Сочинение: " + Essay[i] + "</s>" + '\n'
#         Lit.append(esse)
#     if Subjects[i] == "История":    
#         esse = "<s>Тема: " + them + '\n'
#         esse += "Сочинение: " + Essay[i] + "</s>" + '\n'
#         His.append(esse)
#     i += 1


# i = 0
# with open(PATH_EXPORT + "trainRUS.txt", "a") as file:
#     for data in Rus:  
#         if i <= len(Rus) - 10:
#             file.write(data)
#         i += 1
# file.close()

# i = 0

# with open(PATH_EXPORT + "trainLit.txt", "a") as file:
#     for data in Lit:  
#         if i <= len(Lit) - 10:
#             file.write(data)
#         i += 1
# file.close()

# i = 0

# with open(PATH_EXPORT + "trainHis.txt", "a") as file:
#     for data in His:  
#         if i <= len(His) - 10:
#             file.write(data)
#         i += 1
# file.close()

# i = 0

# with open(PATH_EXPORT + "trainSS.txt", "a") as file:
#     for data in SS:  
#         if i <= len(SS) - 10:
#             file.write(data)
#         i += 1
# file.close()

# i = 0

# with open(PATH_EXPORT + "validRUS.txt", "a") as file:
#     for data in Rus:  
#         if i + len(Rus) - 10  < len(Rus):
#             file.write(data)
#         i += 1
# file.close()

# i = 0

# with open(PATH_EXPORT + "validLit.txt", "a") as file:
#     for data in Lit:  
#         if i + len(Lit) - 10  < len(Lit):
#             file.write(data)
#         i += 1
# file.close()

# i = 0

# with open(PATH_EXPORT + "validHis.txt", "a") as file:
#     for data in His:  
#         if i + len(His) - 10  < len(His):
#             file.write(data)
#         i += 1
# file.close()

# i = 0

# with open(PATH_EXPORT + "validSS.txt", "a") as file:
#     for data in SS:  
#         if i + len(SS) - 10  < len(SS):
#             file.write(data)
#         i += 1
# file.close()









