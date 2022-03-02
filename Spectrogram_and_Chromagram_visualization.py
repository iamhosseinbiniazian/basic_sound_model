from PyAudio import audioAnalysis
wavefilename='data/doremi.wav'
#Spectrogram
#audioAnalysis.fileSpectrogramWrapper(wavefilename)
#Chromagram
audioAnalysis.fileChromagramWrapper(wavefilename)
