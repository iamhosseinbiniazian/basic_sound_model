
from PyAudio import audioBasicIO
from PyAudio import audioFeatureExtraction
import matplotlib.pyplot as plt
[Fs, x] = audioBasicIO.readAudioFile("data/count.wav")
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.030*Fs, 0.010*Fs);
plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel('ZCR');
plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()
