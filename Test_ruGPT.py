# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:59:47 2020

@author: Alvl_SAM
"""

import json
import argparse
from subprocess import Popen, PIPE

test = ['./test/history.json', './test/literature.json', './test/obhestvo.json', './test/rus_lang.json']

def load(): #функция загрузки темы из json
    with open(test[0] ,'r', encoding='utf-8') as fh:
        data_his = json.load(fh)
    fh.close()
    with open(test[1] ,'r', encoding='utf-8') as fh:
        data_lit = json.load(fh)
    fh.close()
    with open(test[2] ,'r', encoding='utf-8') as fh:
        data_obh = json.load(fh)
    fh.close()
    with open(test[3] ,'r', encoding='utf-8') as fh:
        data_rus = json.load(fh)
    fh.close()
    
    return data_his, data_lit, data_obh, data_rus


def output(data_his, data_lit, data_obh, data_rus): 
    with open(test[0], 'w') as f:
        json.dump(data_his, f)
    f.close()
    with open(test[1], 'w') as f:
        json.dump(data_lit, f)
    f.close()
    with open(test[2], 'w') as f:
        json.dump(data_obh, f)
    f.close()
    with open(test[3], 'w') as f:
        json.dump(data_rus, f)
    f.close()




def json_test():
    data_his, data_lit, data_obh, data_rus = load()
    i = 0
    for data in data_his:
        theme = 'Тема: ' + data['theme'] + '\n' + 'Сочинение: '
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/history --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        data_his[i]['essay'] = str(out, 'utf-8')
        i += 1
    i = 0
    for data in data_lit:
        theme = 'Тема: ' + data['theme'] + '\n' + 'Сочинение: '
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/lit --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        data_lit[i]['essay'] = str(out, 'utf-8')
        i += 1
    i = 0
    for data in data_obh:
        theme = 'Тема: ' + data['theme'] + '\n' + 'Сочинение: '
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/ss --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        data_obh[i]['essay'] = str(out, 'utf-8')
        i += 1
    i = 0
    for data in data_rus:
        theme = 'Тема: ' + data['theme'] + '\n' + 'Сочинение: '
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/rus --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        data_rus[i]['essay'] = str(out, 'utf-8')
        i += 1
    output(data_his, data_lit, data_obh, data_rus)
    
    
    
    
    

def custom_test(theme, subject):
    if subject == 0:
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/history --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        print([str(out, 'utf-8')]) # или var = str(out, 'utf-8')
    if subject == 1:
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/rus --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        print([str(out, 'utf-8')]) # или var = str(out, 'utf-8')
    if subject == 2:
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/lit --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        print([str(out, 'utf-8')]) # или var = str(out, 'utf-8')
    if subject == 3:
        out, err = Popen('python generate_transformers.py --model_type=gpt2 --model_name_or_path=./models/ss --k=5 --p=0.95 --prompt=' + theme + '--length=500', shell=True, stdout=PIPE).communicate()
        print([str(out, 'utf-8')]) # или var = str(out, 'utf-8')

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true", help="Json test")
parser.add_argument("--subject", 
                        default=None, 
                        type=int, 
                        required=True,
                        help="Custom subject for test")
parser.add_argument("--test_theme", 
                        default=None, 
                        type=str, 
                        required=True,
                        help="Custom theme for test")




args = parser.parse_args()
if args.test:
    json_test()
else:
    custom_test(args.test_theme, args.subject)
    
