import os,shutil
from subprocess import call
sox=True
folder='/home/quadro2/PycharmProjects/PyTest/data/MusicSpeech'
for d, ds, fs in os.walk(folder):
        for fname in fs:
            fullfname = d + '/' + fname
            wavfname=fullfname
            wavfname2 = fullfname[:-3] + '.WAV'
            tempfname = d + '/' + fname[:-4] + '_temp.wav'
            rawfname = d + '/' + fname[:-4] + '.rttohtk'
            if sox:
                shutil.move(wavfname, tempfname)
                call(['sox', tempfname, wavfname2])
                # w/o headers, sox uses extension
                os.remove(tempfname)
            print(fullfname)