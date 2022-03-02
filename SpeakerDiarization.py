from PyAudio import audioBasicIO as aIO
from PyAudio import audioSegmentation as aS
soundpathth='data/diarizationExample.wav'
def mainSpeakerDiarization(soundpath,numspeaker):
    m=aS.speakerDiarization(soundpath,
                        numOfSpeakers=numspeaker)
    finalresult={'value':m,'NumSpeaker':numspeaker}
    return finalresult
m=mainSpeakerDiarization(soundpathth,4)
print(m)
