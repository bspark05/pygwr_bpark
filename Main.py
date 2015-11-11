'''
Created on Nov 9, 2015

@author: Bumsub
'''
import PyGWR.FileIO as pyFileIO
import matplotlib.pyplot as plt
import seaborn as sns
from array import array
import numpy as np


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
    
    plt.scatter(xCoord,yCoord)
    plt.show()

    