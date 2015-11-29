import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy import linalg

def calculateCorrelation(save,plt):

    size = []
    for i, r in save.iterrows():
        size.append(r['width'] * r['height'] / 20000)

    save['size'] = size

    data = pd.DataFrame(save,columns=['Convenience','size'])

    data_cov = data.corr()

    vmax = data_cov.values.max()

    print data_cov

    fig, ax = plt.subplots()
    ax.xaxis.tick_top()

    plt.imshow(data_cov.values, interpolation='nearest', vmin=-vmax,vmax=vmax, cmap=plt.cm.RdBu_r)

    plt.xticks(range(0,2))
    plt.yticks(range(0,2))
    
    return data_cov
