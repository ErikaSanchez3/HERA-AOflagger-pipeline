#! /bin/bash

echo'This script will make all the necessary file conversions in order to apply a strategy using AOflagger. After AOflagger has been applied, it will convert back to uvfits inorder to make occupancy plots and waterfall plots of the shortest and longest baselines. The pipeline goes as follows: miriad file -->  uvfits --> measurement set --> uvfits'

strategy='/home/champ3/Desktop/7_26_18_Strategy.rfis' # This is the strategy that will be applied to the data set. It was created previously created using rfigui

files=(/home/champ3/Desktop/miriadfiles/zen.*) # Reads in Miriad files(from the miriad folder) that will be used 
echo ${files[@]}

# miriad to uvfits
python miriad2uvfits.py ${files[@]} # This python link will make the first conversion from miriad files to uvfits

# uvfits to ms using casa

in_path='/home/champ3/Desktop/fitsfiles/'
mkdir $in_path
out_path='/home/champ3/Desktop/msfiles/'
echo 'Running CASA' 
/home/champ3/casa-5.3.0/bin/casa -c uvfits2ms.py # Here we run casa and then feed it a python link to make the uvfits to ms conversion (This conversion is necessary because AOflagger only takes ms miles)

# AOFlagger
msfiles=($out_path'*.ms')
aoflagger -strategy $strategy ${msfiles[@]} # AOflagger applies the strategy 

#ms to uvfits using casa
echo 'Running CASA'
/home/champ3/casa-5.3.0/bin/casa -c ms2uvfits.py # makes the final conversion from ms back to uvfits

# occupancy plots
echo 'Making occupancy plots...'
python occupancyplots.py

# Waterfall plot
echo 'Making waterfall plots...'
python waterfallplot.py
