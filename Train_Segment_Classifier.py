from PyAudio import audioTrainTest as aT
from PyAudio import audioSegmentation as aS
import numpy as np
import os
folder='data/genresTrainTest/test/'
#directory for genere music classification
dirname=['data/genresTrainTest/train/blues',
         'data/genresTrainTest/train/classical',
         'data/genresTrainTest/train/country',
         'data/genresTrainTest/train/disco',
         'data/genresTrainTest/train/hiphop',
         'data/genresTrainTest/train/jazz',
         'data/genresTrainTest/train/metal',
         'data/genresTrainTest/train/pop',
         'data/genresTrainTest/train/reggae',
         'data/genresTrainTest/train/rock']
#direcxtory for speech/music classification
dirnamesm=['data/MusicSpeech/music',
           'data/MusicSpeech/speech']
#aT.featureAndTrain(dirnamesm, 1.0, 1.0, aT.shortTermWindow,aT.shortTermStep, "svm", "svmMusicSpeech", computeBEAT=False)

#[flagsInd, classesAll, acc, CM] = aS.mtFileClassification("data/scottish.wav", "svmMusicSpeech", "svm", True, 'data/scottish.segments')
ii=0
trues=0
for d, ds, fs in os.walk(folder):
    for fname in fs:
        if fname[-4:] != '.WAV':
            continue
        ii+=1;
        h=d.split('/')
        fullname=d+'/'+fname
        m=aT.fileClassification(fullname, "svmrbfMusicGenre3","svm_rbf")
        print("Trues=",h[-1])
        i= np.where( m[1]==max(m[1]))
        print("Predict=",m[2][i[0][0]])
        if h[-1]==m[2][i[0][0]]:
            trues+=1
print("Accurecy=",trues/ii)
