import os
import shutil
path_img='D:\\PR\\new_test\\data'
ls = os.listdir(path_img)
print(len(ls))
a=0
for i in ls:
    print(int(i[:-4]))
    if int(i[:-4])%4 == 0.0:
        a = a+1;
        print("yes",a)
        shutil.move(path_img+'/'+i,"D:\\PR\\new_test\\SourceJPGImages_test\\VOC2012\\Annotations\\"+i)

