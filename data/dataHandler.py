import os
import shutil
import numpy as np
import configparser
import glob
if not os.path.exists('images'):
    os.makedirs('images/train')
    os.makedirs('images/valid')
if not os.path.exists('labels'):
    os.makedirs('labels/train')
    os.makedirs('labels/valid')

# 训练集和测试集的比例
TRAIN_RATE = 0.8
txt_list=glob.glob('./CUHKSYSU/labels_with_ids/*.txt')
print(txt_list)
for i, txt in enumerate(txt_list):
    label_list=[]
    with open(txt,'r') as fs:
        txt_lines=fs.readlines()
        if len(txt_lines) <1:
            continue
        for txt_line in txt_lines:
            txt_line=txt_line.replace('\n','').split()
            line_new=str(txt_line[0]+' '+txt_line[2]+' '+txt_line[3]+' '+txt_line[4]+' '+txt_line[5])
            label_list.append(line_new)
    txt_write=txt.replace('\\','/').split('/')[-1]
    image_path='./CUHKSYSU/images/'+txt_write.replace('txt','jpg')
    txt_pull_path="./labels/train/"+txt_write
    valid_pull_path = './labels/valid/' + txt_write
    image_path_new='./images/train/'+txt_write.replace('txt','jpg')
    image_valid_new='./images/valid/'+txt_write.replace('txt','jpg')
    # image_new_path="./labels/train"+
    if i < int(len(txt_list) * TRAIN_RATE):
        with open(txt_pull_path, 'w') as fw:
            for label in label_list:
                fw.write(label+'\n')
        shutil.copy(image_path,image_path_new)
        print(f'train: >>>>正在处理{i}/{len(txt_list) * TRAIN_RATE}')
        
    else:
        with open(valid_pull_path, 'w') as fw:
            for label in label_list:
                fw.write(label+'\n')
        shutil.copy(image_path,image_valid_new)
        print(f'valid: >>>>正在处理{i}/{len(txt_list) * TRAIN_RATE}')