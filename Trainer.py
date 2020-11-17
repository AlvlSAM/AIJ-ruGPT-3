# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 23:29:22 2020

@author: Alvl_SAM
"""

import argparse
from subprocess import Popen, PIPE

def main():
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("--SS_save", 
                        default=None, 
                        type=str, 
                        required=True,
                        help="The output directory where the model Social studies predictions and checkpoints will be written.")
    parser.add_argument("--Rus_save", 
                        default=None, 
                        type=str, 
                        required=True, 
                        help="The output directory where the model Russian language predictions and checkpoints will be written.")
    parser.add_argument("--His_save", 
                        default=None, 
                        type=str, 
                        required=True, 
                        help="The output directory where the model History predictions and checkpoints will be written.")
    parser.add_argument("--Lit_save", 
                        default=None, 
                        type=str, 
                        required=True, 
                        help="The output directory where the model Literature predictions and checkpoints will be written.")
    args = parser.parse_args()
    if args.SS_save == None or args.Lit_save == None or args.His_save == None or args.Rus_save == None:
        print("Error paths save models")
    else:
        models_perplexi = []
        print("Congrats train is started")
        out, err = Popen('python pretrain_transformers.py --output_dir=' + args.SS_save +' --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3medium_based_on_gpt2 --do_train --train_data_file=trainSS.txt --do_eval --fp16 --eval_data_file=validSS.txt --eval_all_checkpoints --per_gpu_train_batch_size 1 --gradient_accumulation_steps 1 --num_train_epochs 2 --block_size 2048 --overwrite_output_dir', shell=True, stdout=PIPE).communicate()
        models_perplexi.append(["Обществознание", str(out, 'utf-8')]) # или var = str(out, 'utf-8')
        out, err = Popen('python pretrain_transformers.py --output_dir=' + args.Rus_save +' --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3medium_based_on_gpt2 --do_train --train_data_file=trainRus.txt --do_eval --fp16 --eval_data_file=validRus.txt --eval_all_checkpoints --per_gpu_train_batch_size 1 --gradient_accumulation_steps 1 --num_train_epochs 8 --block_size 2048 --overwrite_output_dir', shell=True, stdout=PIPE).communicate()
        models_perplexi.append(["Русский язык", str(out, 'utf-8')]) # или var = str(out, 'utf-8')
        out, err = Popen('python pretrain_transformers.py --output_dir=' + args.His_save +' --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3medium_based_on_gpt2 --do_train --train_data_file=trainHis.txt --do_eval --fp16 --eval_data_file=validHis.txt --eval_all_checkpoints --per_gpu_train_batch_size 1 --gradient_accumulation_steps 1 --num_train_epochs 15 --block_size 2048 --overwrite_output_dir', shell=True, stdout=PIPE).communicate()
        models_perplexi.append(["История", str(out, 'utf-8')]) # или var = str(out, 'utf-8')
        out, err = Popen('python pretrain_transformers.py --output_dir=' + args.Lit_save +' --model_type=gpt2 --model_name_or_path=sberbank-ai/rugpt3medium_based_on_gpt2 --do_train --train_data_file=trainLit.txt --do_eval --fp16 --eval_data_file=validLit.txt --eval_all_checkpoints --per_gpu_train_batch_size 1 --gradient_accumulation_steps 1 --num_train_epochs 3 --block_size 2048 --overwrite_output_dir', shell=True, stdout=PIPE).communicate()
        models_perplexi.append(["Литература", str(out, 'utf-8')]) # или var = str(out, 'utf-8')
        for data in models_perplexi:
            print(data[0] + ":", data[1])


















if __name__ == "__main__":
    main()