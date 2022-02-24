import os
import sys
import numpy as np
import scipy as sp
from subprocess import call
import shutil
from PyAudio import audioFeatureExtraction as aF
from PyAudio import audioTrainTest as aT
from PyAudio import audioBasicIO
import csv
from DataPrepration import AudioPreprate
import wavio
import librosa
import python_speech_features as psf
import scipy.io.wavfile as siw
sox=True
path='/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/'
audiopath='audio'
metadatapath='metadata'
'''with open(path+metadatapath+'/'+'UrbanSound8K.csv', 'r') as csvfile:
    filecsvmeta=csv.reader(csvfile,delimiter=',')
    i=0
    for row in filecsvmeta:
        if i==0:
            i=i+1
            continue
        pathsound=path+audiopath+'/'+'fold'+row[-3]+'/'+row[0]
        #pathsound=pathsound[:-4]+'.WAV'
        print(pathsound)
        [Fs,x]=siw.read(pathsound)
        x = audioBasicIO.stereo2mono(x)
        [mtF, _] = aF.mtFeatureExtraction(x, Fs, round(Fs * 1), round(Fs * 1),
                                       round(Fs * aT.shortTermWindow), round(Fs *  aT.shortTermStep))
        np.save(pathsound[:-4]+'.npy',mtF)
dirnamesm=['/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold1',
           '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold2',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold3',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold4',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold5',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold6',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold7',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold8',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold9',
            '/home/quadro2/PycharmProjects/PyTest/data/UrbanSound8K/audio/fold10']
[features, classNames, _] = aF.dirsWavFeatureExtraction(dirnamesm,1.0, 1.0, aT.shortTermWindow,aT.shortTermStep,\
                                   computeBEAT=False)'''
with open(path+metadatapath+'/'+'UrbanSound8K.csv', 'r') as csvfile:
    filecsvmeta=csv.reader(csvfile,delimiter=',')
    i=0
    allMtFeatures=np.array([])
    Label=[]
    for row in filecsvmeta:
        if i==0:
            i=i+1
            continue
        wavFile=path+audiopath+'/'+'fold'+row[-3]+'/'+row[0]
        #pathsound=pathsound[:-4]+'.WAV'
        print(wavFile)
        if os.stat(wavFile).st_size == 0:
            print("   (EMPTY FILE -- SKIPPING)")
            continue
        [Fs, x] = siw.read(wavFile)  # read file
        x = audioBasicIO.stereo2mono(x)  # convert stereo to mono
        if x.shape[0] < float(Fs) / 10:
            print("  (AUDIO FILE TOO SMALL - SKIPPING)")
            continue
        [MidTermFeatures, _] = aF.mtFeatureExtraction(x, Fs, round(1 * Fs), round(1 * Fs), round(Fs * aT.shortTermWindow),
                                                       round(Fs * aT.shortTermStep))
        MidTermFeatures = np.transpose(MidTermFeatures)
        MidTermFeatures = MidTermFeatures.mean(axis=0)  # long term averaging of mid-term statistics
        if len(allMtFeatures) == 0:  # append feature vector
            allMtFeatures = MidTermFeatures
        else:
            allMtFeatures = np.vstack((allMtFeatures, MidTermFeatures))
        Label.append(row[-2])
np.save('UrbanFeature.npy',allMtFeatures)
np.save('UrbanLabel.npy',Label)
print("Hello World")

