from PyAudio import audioTrainTest as aT
#Train
#aT.featureAndTrainRegression("data/speechEmotion/", 1, 1,
#                            aT.shortTermWindow, aT.shortTermStep,
#                            "svm", "data/svmSpeechEmotion", False)
#Test
m=aT.fileRegression("data/00.wav", "data/svmSpeechEmotion", "svm")
print(m)