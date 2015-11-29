import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy import linalg

def calculateCorrelation(save,plt):

    size = []
    for i, r in save.iterrows():
        size.append(r['width'] * r['height'] / 10000)

    data_cov = np.corrcoef(save['Convenience'],size)

    vmax = data_cov.max()

    fig, ax = plt.subplots()
    ax.xaxis.tick_top()

    plt.imshow(data_cov, interpolation='nearest', vmin=-vmax,vmax=vmax, cmap=plt.cm.RdBu_r)

    
    
