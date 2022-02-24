import os
import sys
import numpy as np
import scipy as sp
from subprocess import call
import shutil
sox=True
path='/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/'
audiopath='audio'
metadatapath='metadata'
for d, ds, fs in os.walk(path+audiopath):
    for fname in fs:
        if fname[-4:]!='.wav':
            continue
        fullfname = d + '/' + fname
        wavfname = fullfname[:-4] + '.WAV'
        tempfname = d + '/' + fname[:-4] + '_temp.wav'
        rawfname = d + '/' + fname[:-4] + '.rttohtk'
        if sox:
            shutil.move(fullfname, tempfname)
            call(['sox', tempfname, wavfname])
            # w/o headers, sox uses extension
            shutil.move(tempfname, rawfname)
            #os.remove(tempfname)
            os.remove(rawfname)
            print("Converted:"+fullfname)
        if sox:
            call(['sox','-S', wavfname,'-b','16', wavfname])