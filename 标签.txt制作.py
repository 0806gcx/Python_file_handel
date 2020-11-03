# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:28:09 2020

@author: 60215
"""
import os
from os import listdir, getcwd
from os.path import join

if __name__ == '__main__':
    source_folder = 'D:/Deep_learning/darknet-master/build/darknet/x64/data/obj'
    dest = 'D:/Deep_learning/darknet-master/build/darknet/x64/data/train.txt'  # train.txt文件路径
    dest2 = 'D:/Deep_learning/darknet-master/build/darknet/x64/data/val.txt'  # val.txt文件路径
    file_list = os.listdir(source_folder)
    train_file = open(dest, 'a')
    val_file = open(dest2, 'a')
    file_num = 0
    for file_obj in file_list:
        file_path = os.path.join(source_folder, file_obj)
        file_name, file_extend = os.path.splitext(file_obj)
        file_num = file_num + 1


        if (file_num % 4 == 0):  # 每隔4张选取一张验证集
            val_file.write('data/obj/'+file_name + '.jpg'+'\n')
        else:
            train_file.write('data/obj/'+file_name +'.jpg'+ '\n')


        # val_file.write(file_name + '\n')
        #
        # train_file.write(file_name + '\n')
train_file.close()
val_file.close()


