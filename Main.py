'''
Created on Nov 9, 2015

@author: Bumsub
'''
import PyGWR.FileIO as pyFileIO
import matplotlib.pyplot as plt

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
        
    plt.scatter(xCoord, yCoord, c=attr2)
    plt.show()