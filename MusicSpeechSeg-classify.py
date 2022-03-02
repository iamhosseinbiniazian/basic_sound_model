from PyAudio import audioTrainTest as aT
from PyAudio import audioSegmentation as aS

dirnamesm=['data/MusicSpeech/music',
           'data/MusicSpeech/speech']
#aT.featureAndTrain(dirnamesm, 1.0, 1.0, aT.shortTermWindow,aT.shortTermStep, "svm", "svmMusicSpeech", computeBEAT=False)

[flagsInd, classesAll, acc, CM] = aS.mtFileClassification("out2.WAV", "svmModel", "svm", True)
print("Hello World")
