import python_speech_features as psf
import librosa
# import alsaaudio
from scipy.io import wavfile
def ReadAudio(FileName):
    Fs,RawData=wavfile.read(FileName)
    return Fs,RawData
def FrameBlocking(sig,Fs,Framesize,FrameShift):
    return psf.sigproc.framesig(sig,int(Fs*Framesize),int(Fs*FrameShift))