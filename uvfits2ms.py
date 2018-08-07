# uvfits2ms.py

import sys
from glob import glob

files1=glob('/home/champ3/Desktop/fitsfiles/zen*.uvfits') # goes through every file in the fitsfiles folder 

for i in files1:
    dir=i.split('/')
    newdir='/'.join(dir[0:4]+['msfiles',''])#this prints'/home/champ3/Desktop/msfiles/'
    vis=newdir+dir[-1]# this prints '/home/champ3/Desktop/msfiles/zen***.uvfits'
    filename=vis.split('/')[-1]#this will print 'zen.***.uvfits'
    fn=filename.split('.')[:-1]+['_7_27_18_Strategy']+['ms']#This prints the following:['zen', 'grp1', 'of2', 'xx', 'LST', '1', '28828', 'uvOCRSL', 'ms']
    filename2='.'.join(fn) #this will print: 'zen.grp1.of2.xx.LST.1.28828.uvOCRSL.ms'
    filename3=vis.split('/')[0:5]+[filename2]#This prints:['home','champ3','Desktop','fitsfiles','msfiles','zen.grp1.of2.xx.LST.1.28828.uvOCRSL.ms']

    filename4='/'.join(filename3)#This will print: 'home/champ3/Desktop/fitsfiles/msfiles/zen.grp1.of2.xx.LST.1.28828.uvOCRSL.ms'
    importuvfits(fitsfile=i, vis=filename4)

    #Once the uvfits to ms conversion is completed, the ms file will be stored in the msfiles folder 




