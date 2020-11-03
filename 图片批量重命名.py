#coding=gbk
import os
import sys
def rename():
    path=r"D:\Deep_learning\数据集\picture_test"
    num_x=input("请输入位数:")
    startNumber=input("请输入开始数:")
    fileType=input("请输入后缀名（如 .jpg、.txt等等）:")
    startNumber = str(int(startNumber)).zfill(int(num_x))
    print("正在生成以"+startNumber+fileType+"迭代的文件名")
    count=0
    filelist=os.listdir(path)
    for files in filelist:
        Olddir=os.path.join(path,files)
        if os.path.isdir(Olddir):
            continue
        Newdir=os.path.join(path,str((count+int(startNumber))).zfill(int(num_x))+fileType)
        os.rename(Olddir,Newdir)
        count+=1
        print("count:"+str(count))
    print("一共修改了"+str(count)+"个文件")

rename() 
