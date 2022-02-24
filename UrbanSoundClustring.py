import os
import sys
import numpy as np
import scipy as sp
from subprocess import call
import shutil
from sklearn.cluster import SpectralClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import Birch
UrbanFeature='UrbanFeature.npy'
UrbanLabel='UrbanLabel.npy'
Feature=np.load(UrbanFeature)
Label=np.load(UrbanLabel)
sc = Birch(n_clusters=10)
label=sc.fit_predict(Feature)
print(label)

