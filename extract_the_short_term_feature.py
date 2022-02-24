#The following code uses stFeatureExtraction() to extract the short term feature sequences for
#an audio signal, using a frame size of 50 msecs and a frame step of 25 msecs (50% overlap). In
#The following code uses stFeatureExtraction() to extract the short term feature sequences for an audio signal, using a frame size of 50 msecs and a frame step of 25 msecs (50% overlap). In order to read the audio samples,
# we call function readAudioFile() from the audioBasicIO.py file.
from PyAudio import audioBasicIO
from PyAudio import audioFeatureExtraction
import matplotlib.pyplot as plt
[Fs, x] = audioBasicIO.readAudioFile("data/count.wav")
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.030*Fs, 0.010*Fs);
plt.subplot(2,1,1); plt.plot(F[0,:]); plt.xlabel('Frame no'); plt.ylabel('ZCR');
plt.subplot(2,1,2); plt.plot(F[1,:]); plt.xlabel('Frame no'); plt.ylabel('Energy'); plt.show()