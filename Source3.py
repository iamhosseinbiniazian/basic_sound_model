import tensorflow as tf
import tflearn
import numpy as np
from PyAudio import audioFeatureExtraction as aF
from PyAudio import audioTrainTest as aT
from sklearn.preprocessing import OneHotEncoder
from sklearn.utils import shuffle
import random
'''dirnamesm=['/home/quadro2/PycharmProjects/PyTest/data/MusicSpeech/speech',
           '/home/quadro2/PycharmProjects/PyTest/data/MusicSpeech/music'
           ]
[features, classNames, _] = aF.dirsWavFeatureExtraction(dirnamesm,1.0, 1.0, aT.shortTermWindow,aT.shortTermStep,\
                                                     computeBEAT=False)
Data=np.array([])
Label=[]
for i,l in enumerate(features):
    print(i)
    print("######################################")
    print(l)
    print("######################################")
    for j in range(l.shape[0]):
        Label.append(i)
    if len(Data) == 0:
        Data = l
    else:
        Data = np.append(Data, l, axis=0)
np.save(""musicspeechdata.npy,Data)
np.save("musicspeechLabel.npy",Label)
print("Hello World")'''
data=np.load("musicspeechdata.npy")
Label=np.load("musicspeechLabel.npy")

hh=np.unique(Label)
label=np.zeros([len(Label),len(hh)])
for i,j in enumerate(Label):
    label[i,j]=1
data,label=shuffle(data,label,random_state=0)
testindex=random.sample(range(0, data.shape[0]), int(0.2*data.shape[0]))
trainindex=[i for i in range(data.shape[0]) if i not in testindex]
Traindata=data[trainindex]
TrainLabel=label[trainindex]
Testdata=data[testindex]
TestLabel=label[testindex]
print("Hello")
tflearn.init_graph(num_cores=8, gpu_memory_fraction=0.5)

net = tflearn.input_data(shape=[None, 68])
net = tflearn.fully_connected(net, 64)
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, 32)
net = tflearn.dropout(net, 0.75)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net)
model.fit(Traindata, TrainLabel,batch_size=2,n_epoch=30,validation_set=[Testdata,TestLabel],show_metric=True)
r=model.evaluate(Testdata,TestLabel)
print("##################################################")
print("##################################################")
print(r)