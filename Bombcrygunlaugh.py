from PyAudio import audioSegmentation as aS
def BombCryGunLaugh(soundpath):
    [flagsInd, classesAll, acc, CM] = aS.mtFileClassification(soundpath, "svmModel", "svm", True)
    finalresult = {'value':[flagsInd,classesAll,acc,CM]}
    return finalresult
sopath="out2.WAV"
final=BombCryGunLaugh(sopath)
print(final)