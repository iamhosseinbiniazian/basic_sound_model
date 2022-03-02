#!/usr/bin/env python2

from PyAudio import audioTrainTest as aT
import os
from sys import argv
from PyAudio import convertToWav
subdirectories = ["data/audioClassification/trainingData/bomb",\
                  "data/audioClassification/trainingData/cry",\
                  "data/audioClassification/trainingData/gun",\
                  "data/audioClassification/trainingData/laugh"]
aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel2", False)
