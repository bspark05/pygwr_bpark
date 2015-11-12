'''
Created on Nov 9, 2015

@author: Bumsub
'''
import PyGWR.FileIO as pyFileIO
import matplotlib.pyplot as plt
import seaborn as sns
from array import array
import numpy as np
from pysal.esda.mapclassify import Fisher_Jenks
from matplotlib.colors import Normalize

def norm_cmap(values, cmap, vmin=None, vmax=None):
    """
    Normalize and set colormap
    
    Parameters
    ----------
    values : Series or array to be normalized
    cmap : matplotlib Colormap
    normalize : matplotlib.colors.Normalize
    cm : matplotlib.cm
    vmin : Minimum value of colormap. If None, uses min(values).
    vmax : Maximum value of colormap. If None, uses max(values).
    
    Returns
    -------
    n_cmap : mapping of normalized values to colormap (cmap)
    
    """
    mn = vmin or min(values)
    mx = vmax or max(values)
    norm = Normalize(vmin=mn, vmax=mx)
    n_cmap = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
    return n_cmap


if __name__ == '__main__':
    
    csvResult = pyFileIO.read_CSV("test_csv.csv")
    print(csvResult)
     
    fieldName = csvResult[0]
    fieldValue = csvResult[1]
     
    print(fieldValue[0])
     
    xCoord = []
    yCoord = []
    attr1 = []
    attr2 = []
    for values in fieldValue.itervalues():
        print(values)
        xCoord.append(values[0])
        yCoord.append(values[1])
        attr1.append(float(values[2]))
        attr2.append(float(values[3]))
 
#     xCoordArr = np.asarray(xCoord)
#     yCoordArr = np.asarray(yCoord)
#     cmap = sns.cubehelix_palette(light=1, as_cmap=True)
#     sns.kdeplot(xCoordArr, yCoordArr, n_levels=30, cmap="Purples_d");
    
    attr1Arr = np.asarray(attr1)
    fj = Fisher_Jenks(attr1Arr, k=6)
    cmap = norm_cmap(fj.yb, cmap='YlGn')
    cmap1 = [cmap.to_rgba(value) for value in attr1Arr]
    
    print(cmap)
    print(cmap1)  
    
    plt.scatter(xCoord,yCoord, c=cmap1)
    plt.show()

    