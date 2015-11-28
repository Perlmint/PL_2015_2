import pandas as ps
import numpy as np
from sklearn.decomposition import PCA

def calculateConvenience(data):
    pca_data = ps.DataFrame(data,columns=['WPM','error_rate','years_of_use'])

    pca_data['error_rate'] = 1 - pca_data['error_rate']
    
    pca = PCA(1)
    x_pca = pca.fit_transform(pca_data)

    s = ps.DataFrame(x_pca,columns=['Convenience'])

    
    result = ps.concat([data,s],axis=1)

    return result

