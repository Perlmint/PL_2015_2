import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def calculateConvenience(data,error_rate,plt):
    pca_data = pd.DataFrame(data,columns=['WPM'])
    pca_data['error_rate'] = pd.Series(error_rate)
    
    pca_data['error_rate'] = 1 - pca_data['error_rate']
    
    pca = PCA(2)
    x_pca = pca.fit_transform(pca_data)

    data['Convenience'] = x_pca.T[0]

    plt.subplot(221)

    plt.plot(pca_data['WPM'],pca_data['error_rate'],'bo')

    plt.title("PCA")
    plt.grid(True)


    plt.subplot(223)
    plt.plot(pca.explained_variance_ratio_)
    
    return data

