import numpy as np
import pandas as pd

import sklearn.cluster

import matplotlib.pyplot as plt
from itertools import cycle

def calculateRealErrorRate(save,data,plt):

    data2 = data[(data.code_point != -1) & ((data.intent_code_point == 32) | ((data.intent_code_point >= 97) & (data.intent_code_point <= 122)))]
    data2['removal'] = False    
    key = pd.DataFrame(data2,columns=['distance','acc'])

    key['acc'] = key['acc'] / 50

    kmeans = sklearn.cluster.KMeans(5,n_init=1)
    kmeans.fit(key)

    key.reset_index()
    #key['cluster'] = pd.Series(kmeans.labels_)

    centers = kmeans.cluster_centers_
    
    n_clusters = len(np.unique(kmeans.labels_))

    Xmax = max(kmeans.cluster_centers_.T[0])
    Ymax = max(kmeans.cluster_centers_.T[1])

    removeList = []

    for i in kmeans.cluster_centers_:
        if i[0] == Xmax or i[1] == Ymax:
            removeList.append(True)
        else:
            removeList.append(False)

    plt.subplot(222)
    for k, col in zip(range(n_clusters), 'bgrcmyk'):
        
        my_members = kmeans.labels_ == k
        
        if removeList[k] == True:
                data2.loc[my_members,'removal'] = True

        plt.plot(key[my_members]['distance'],key[my_members]['acc'],col+'.')

    plt.title("cluster")

    data2 = data2[data2.removal != True]

    data2.reset_index();
    real_error = []

    for index, row in save.iterrows():
        valid_key_count = len(data2[data2.test_name == row['file_name']])
        valid_error_count = 0.0;
        for keyIndex, keyRow in data2[data2.test_name == row['file_name']].iterrows():
            if keyRow['code_point'] != keyRow['intent_code_point']:
                valid_error_count += 1

        if valid_key_count == 0:
            valid_key_count = 1;

        real_error.append(valid_error_count/valid_key_count)
        
    return real_error

