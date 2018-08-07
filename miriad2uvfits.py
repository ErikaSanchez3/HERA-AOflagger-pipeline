#miriad2uvfits.py

import numpy as np
from pyuvdata import UVData 
import sys

files = sys.argv[1:] 

for i in files:
    uvd = UVData()

    uvd.read_miriad(i)

    uvd.select(antenna_nums=(0,1,2,11,12,50,82,98,123,124)) #Can select specific antenna numbers here or comment out the line inorder to process all antennas in your data file 

    uvd.flag_array = np.zeros(np.shape(uvd.flag_array)).astype(bool) # This zeros out original flagsin the miriad file as a precaution
    dir=i.split('/')
    
    newdir='/'.join(dir[0:4]+['fitsfiles',''])

    uvd.write_uvfits(newdir+dir[-1]+'.uvfits', force_phase=True, spoof_nonessential=True)# once the the miriad file has been converted into uvfits, it is saved in the fitsfile
    del(uvd)    
