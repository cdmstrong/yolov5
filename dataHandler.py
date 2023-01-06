import os
import shutil
import numpy as np
import configparser
import glob
if not os.path.exists('data/images'):
    os.makedirs('data/images/train')
if not os.path.exists('data/images/labels'):
    os.makedirs('data/labels/train')


txt_list=glob.glob('data/CUHKSYSU/labels_with_ids/*.txt')
print(txt_list)
for  txt in txt_list:
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
    image_path='data/images/'+txt_write.replace('txt','jpg')
    txt_pull_path="data/labels/train/"+txt_write
    image_path_new='data/images/train/'+txt_write.replace('txt','jpg')
    # image_new_path="./labels/train"+
    with open(txt_pull_path, 'w') as fw:
        for label in label_list:
            fw.write(label+'\n')
    shutil.copy(image_path,image_path_new)
