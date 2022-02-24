import numpy as np
Feature=np.load('Esc50Feture.npy')
Label=np.load('Esc50Label.npy')
maxlenth=-1
for index,fet in enumerate(Feature):
    print(index)
    if fet.shape[0]>maxlenth:
        maxlenth=fet.shape[0]
for index,fet in enumerate(Feature):
    padSecs=maxlenth-fet.shape[0]
    padfet=np.pad(fet, ((0, padSecs), (0, 0)), 'constant', constant_values=0)
    Feature[index]=padfet
Classname=list(set(Label))
newLabel=[]
for lab in Label:
    newLabel.append(Classname.index(lab))
print(Classname)
newLabel=np.array(newLabel)
newFeture=np.ndarray((Feature.shape[0],maxlenth,Feature[0].shape[1]))
for index,fet in enumerate(Feature):
    newFeture[index]=fet
np.save('Esc50Feture.npy',newFeture)
np.save('Esc50Label.npy',newLabel)
print(newLabel.shape)
print("maxlenth is: ",maxlenth)
print("Number of class: ",len(Classname))