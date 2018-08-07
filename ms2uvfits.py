#ms2uvfits.py

import sys
from glob import glob

files1=glob('/home/champ3/Desktop/msfiles/zen*.ms') # ges through all ms files in msfiles folder

for i in files1:
    dir=i.split ('/')
    newdir='/'.join(dir[0:4]+['AOFuvfits',''])
    vis=newdir+dir[-1]
    filename=vis.split('/')[-1]
    fn=filename.split('.')[:-1]+['AOF']+['uvfits'] # adds AOF in the name of the file inorder to distinguish it from the orginal uvfits file that did not have the strategy applied 
    filename2='.'.join(fn)
    filename3=vis.split('/')[0:5]+[filename2]
    filename4='/'.join(filename3)
    exportuvfits(vis=i, fitsfile=filename4) # This new uvfits file is then stored in AOFuvfits folder 
