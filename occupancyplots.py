#occupancyplots.py


import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pyuvdata import UVData 
import numpy as np
from glob import glob


uvd = UVData()
files=glob('/home/champ3/Desktop/AOFuvfits/zen.*.AOF.uvfits')

# defines a function that will calc the occupancy for each baseline in the file 
def get_occupancy(uvd,i,j):
    m = np.mean(uvd.get_flags(i,j), axis =0 ) 
    return m 
# defines a function that will look for the shortes and longest baselines  
def get_distance(uvd):  
    d=[]
    for ind,(i,j) in enumerate(uvd.get_antpairs()):
        dist=np.sqrt(np.sum((uvd.antenna_positions[i,:2]-uvd.antenna_positions[j,:2])**2))
        if dist>10.0:
            d.append(dist)
        else:
            dist=np.nan
            d.append(dist)
    min=np.nanargmin(d)
    max=np.nanargmax(d)
    return uvd.get_antpairs()[min],uvd.get_antpairs()[max]
    
# make a new empty dictionary 
occupancy_stats={}

for f in files:
    print(f)
    uvd.read_uvfits(f,run_check_acceptability=False)
    bsl1,bsl2=get_distance(uvd)
    antpairs = uvd.get_antpairs()
    for ind,(i,j) in enumerate(antpairs):
        ap_str=str(i)+'_'+str(j)  
        if occupancy_stats.has_key(ap_str): # checks to see if antenna pair exists, if it does, it yields the mean  occupanies of the same antenna pair across times/files
            occupancy_stats[ap_str]=np.mean((occupancy_stats[ap_str],get_occupancy(uvd,i,j)),axis=0)
        else:
            occupancy_stats[ap_str]=get_occupancy(uvd,i,j) # if the antenna pair does not exist, it sets it equal to the first occupancy it  finds for that antenna and it averages it then it takes the average

#bsl1,bsl2=get_distance(uvd)
#occupancy=get_occupancy(uvd,i,j)
imin=bsl1[0]
jmin=bsl1[1]
imax=bsl2[0]
jmax=bsl2[1]
b1=str(imin)+'_'+str(jmin)
b2=str(imax)+'_'+str(jmax)
plt.figure()     
plt.subplot(211)
plt.plot(occupancy_stats[b1])
plt.subplot(212)
plt.plot(occupancy_stats[b2])
plt.show()

