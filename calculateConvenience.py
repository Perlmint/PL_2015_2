import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def calculateConvenience(data,plt):
    pca_data = pd.DataFrame(data,columns=['WPM','error_rate','years_of_use'])

    pca_data['error_rate'] = 1 - pca_data['error_rate']
    
    pca = PCA(2)
    x_pca = pca.fit_transform(pca_data)

    data['Convenience'] = x_pca.T[0]

    plt.subplot(221)

    plt.plot(pca_data['WPM'],pca_data['error_rate'],'bo')

    plt.title("PCA")
    plt.grid(True)
    
    return data

