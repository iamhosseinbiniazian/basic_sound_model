import tensorflow as tf
from DataPrepration import AudioPreprate
import os
import numpy as np
fs,sig=AudioPreprate.ReadAudio("small.wav")
Frames=AudioPreprate.FrameBlocking(sig,fs,0.03,0.01)
print(Frames.shape)
dir='data/genresTrainTest/train/'
Fdir='data/FeaturegenresTrainTest/train/'
for d, ds, fs in os.walk(dir):
    for fname in fs:
        if fname[-4:] != '.WAV':
            continue
        if fname[0] == '.':
            continue
        fullname=d+'/'+fname
        fs, sig = AudioPreprate.ReadAudio(fullname)
        Frames = AudioPreprate.FrameBlocking(sig, fs, 0.03, 0.01)
        path=fullname.split('/')
        SavePath=Fdir+path[-2]+'/'
        if not os.path.exists(SavePath):
            os.makedirs(SavePath)
        np.save(SavePath+fname[:-4]+'.npy',Frames)
        print("Converted:",fullname)

