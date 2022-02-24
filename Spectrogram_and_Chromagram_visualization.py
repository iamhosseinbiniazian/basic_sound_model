from PyAudio import audioAnalysis
wavefilename='/media/hossein/New Volume/Source code/PycharmProjects/PyTest/data/doremi.wav'
#Spectrogram
#audioAnalysis.fileSpectrogramWrapper(wavefilename)
#Chromagram
audioAnalysis.fileChromagramWrapper(wavefilename)