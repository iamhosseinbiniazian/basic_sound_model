import numpy as np
from keras.layers import Input,Dense,Conv2D,MaxPool2D,BatchNormalization,Bidirectional,Flatten,Dropout
from keras.models import Model
from keras.utils import to_categorical
from keras.layers.recurrent import LSTM
import keras.backend as K
Feature=np.load('Esc50Feture.npy')
Label=np.load('Esc50Label.npy')
maxlenth=2992
nummfcc=13
numclass=2
Label=to_categorical(Label,numclass)
inputt=Input((maxlenth,nummfcc))
network=LSTM(128,activation='elu')(inputt)
network=Dropout(0.3)(network)
network=Dense(numclass,activation='softmax')(network)
model=Model(inputt,network)
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(Feature,Label,batch_size=4,epochs=15,validation_split=0.1,shuffle=True)