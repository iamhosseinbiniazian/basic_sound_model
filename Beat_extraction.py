from PyAudio import audioAnalysis
wavefile='data/small.wav'
audioAnalysis.beatExtractionWrapper(wavefile,plot=True)