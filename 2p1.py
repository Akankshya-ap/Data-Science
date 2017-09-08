import matplotlib
#import sklearn
from matplotlib import pyplot as plt
import pandas
import numpy

###################### Data retrieval ##################

df = pandas.read_csv('C:\Users\Akankshya\Desktop\data sciene\dat2.csv')

data_y = df['d']
del df['d']
data_x = df
print data_x
print data_y
X_test = numpy.array(data_x, dtype=float)
Y_test = numpy.array(data_y, dtype=float)
print X_test.shape
print Y_test.shape
