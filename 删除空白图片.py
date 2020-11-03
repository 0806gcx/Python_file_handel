import os
import shutil
img_path_img=r'D:\Deep_learning\a_data\test\image'
label_path_img=r'D:\Deep_learning\a_data\test\Annotation'
img_ls = os.listdir(img_path_img)
label_ls = os.listdir(label_path_img)
b = 0
print(len(img_ls))
print(len(label_ls))
for i in img_ls:
    a=0
    for j in label_ls:
        if int(i[:-4])==int(j[:-4]):
            a=1
    if a==0 :
        b = b+1
        os.remove(img_path_img+"/"+i)


