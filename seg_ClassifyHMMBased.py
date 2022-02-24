from PyAudio import audioTrainTest as aT
from PyAudio import audioSegmentation as aS
import numpy as np
import os
#aS.trainHMM_fromFile('data/count.wav', 'data/count.segments', 'hmmTemp1', 0.1, 0.1) # train using a single file
#aS.trainHMM_fromDir('radioFinal/small/', 'hmmTemp2', 1.0, 1.0)                          # train using a set of files in a folder
aS.hmmSegmentation('data/count2.wav', 'hmmTemp1', True, 'data/count2.segments')             # test 1
#aS.hmmSegmentation('data/scottish.wav', 'hmmTemp2', True, 'data/scottish.segments')             # test 2