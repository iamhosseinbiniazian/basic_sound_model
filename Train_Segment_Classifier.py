from PyAudio import audioTrainTest as aT
from PyAudio import audioSegmentation as aS
import numpy as np
import os
folder='data/genresTrainTest/test/'
#directory for genere music classification
dirname=['/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/blues',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/classical',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/country',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/disco',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/hiphop',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/jazz',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/metal',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/pop',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/reggae',
         '/home/quadro2/PycharmProjects/PyTest/data/genresTrainTest/train/rock']
#direcxtory for speech/music classification
dirnamesm=['/home/quadro2/PycharmProjects/PyTest/data/MusicSpeech/music',
           '/home/quadro2/PycharmProjects/PyTest/data/MusicSpeech/speech']
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
