#!/usr/bin/env python2

from PyAudio import audioTrainTest as aT
import os
from sys import argv
from PyAudio import convertToWav
subdirectories = ["/home/quadro2/PycharmProjects/audioClassification/trainingData/bomb",\
                  "/home/quadro2/PycharmProjects/audioClassification/trainingData/cry",\
                  "/home/quadro2/PycharmProjects/audioClassification/trainingData/gun",\
                  "/home/quadro2/PycharmProjects/audioClassification/trainingData/laugh"]
aT.featureAndTrain(subdirectories, 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmModel2", False)