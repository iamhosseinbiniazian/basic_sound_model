import os
import sys
import shutil
from scipy.io import wavfile
from sklearn import preprocessing
import python_speech_features as psf
import numpy as np
rootdir='/home/apasai/PycharmProjects/PyTest/data/ESC-50/'
Feature=[]
Label=[]
for d, ds, fs in os.walk(rootdir):
    for fname in fs:
        if fname[-4:] != '.WAV':
            continue
        if fname[0] == '.':
            continue
        mm=d.split('/')
        mm=mm[-1].split('-')
        classname=mm[-1]
        Label.append(classname)
        fullfname = d + '/' + fname
        [rate,sig]=wavfile.read(fullfname)
        mfcc=psf.mfcc(sig,rate)
        mfcc=preprocessing.scale(mfcc)
        Feature.append(mfcc)
        print(fullfname)
np.save('Esc50Feture.npy',Feature)
np.save('Esc50Label.npy',Label)
