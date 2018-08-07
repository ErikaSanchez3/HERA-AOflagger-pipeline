#waterfallplot.py

from pyuvdata import UVData 
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

uvd = UVData()
files2=glob('/home/champ3/Desktop/AOFuvfits/zen*.uvfits')
for i in files2:
    uvd.read_uvfits(i,run_check=False,run_check_acceptability=False)
    plt.imshow(uvd.get_flags(123,124),aspect= 'auto') # aspect makes axis equal
    plt.show()
