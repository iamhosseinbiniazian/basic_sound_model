import os
import sys
import shutil
from subprocess import call
rootdir='data/ESC-50/'
for d, ds, fs in os.walk(rootdir):
    for fname in fs:
        if fname[-4:] != '.ogg':
            continue
        if fname[0] == '.':
            continue
        fullfname = d + '/' + fname
        wavfname = fullfname[:-4] + '.WAV'
        tempfname = d + '/' + fname[:-4] + '_temp.wav'
        rawfname = d + '/' + fname[:-4] + '.rttohtk'
        shutil.move(fullfname, tempfname)
        call(['sox', tempfname, wavfname])
        # w/o headers, sox uses extension
        shutil.move(tempfname, rawfname)
        # os.remove(tempfname)
        os.remove(rawfname)
