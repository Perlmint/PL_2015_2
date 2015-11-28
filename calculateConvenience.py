import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def calculateConvenience(data):
    pca_data = pd.DataFrame(data,columns=['WPM','error_rate','years_of_use'])

    pca_data['error_rate'] = 1 - pca_data['error_rate']
    
    pca = PCA(1)
    x_pca = pca.fit_transform(pca_data)

    data['Convenience'] = x_pca

    
    return data

