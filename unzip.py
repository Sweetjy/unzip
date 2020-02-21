import os
import zipfile

path="D:\GDELTfile"
filelist = os.listdir(path)  #读取所有文件
for i in range(0,len(filelist)):
    if filelist[i].split('.')[-1]=="zip":
        file=os.path.join(path,filelist[i])
        print(file)
        fz = zipfile.ZipFile(file,'r')
        fz.extract(fz.namelist()[0],path)#解压下载下来的zip文件
        fz.close()
        if(os.path.exists(file[:-4])):
            os.remove(file)#删除zip文件夹，只保存解压后的数据