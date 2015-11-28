import numpy as np
import pandas as pd

import sklearn.cluster

import matplotlib.pyplot as plt
from itertools import cycle

key_distances = pd.read_csv('data/key_distances.csv')
model_infos = pd.read_csv('data/model.csv')

def load_key_data(filename):
    key_data = pd.read_csv(filename)
    key_data = pd.merge(key_data, key_distances, how='left', on=['code_point', 'intent_code_point'])
    key_data = pd.merge(key_data, model_infos, how='left', on=['model'])
    return key_data

def calculateRealErrorRate(data):

    data2 = data[(data.code_point != -1) & ((data.intent_code_point == 32) | ((data.intent_code_point >= 97) & (data.intent_code_point <= 122)))]
    
    key = pd.DataFrame(data2,columns=['distance','WPM'])

    kmeans = sklearn.cluster.KMeans(5,n_init=1)
    kmeans.fit(key)

    key.reset_index()
    key['cluster'] = pd.Series(kmeans.labels_)
    
    return key
