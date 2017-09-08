import matplotlib
import sklearn
from matplotlib import pyplot as plt
import pandas
import numpy

###################### Data retrieval ##################

df = pandas.read_csv('C:\Users\Akankshya\Desktop\study\data sciene\data.csv')

data_y = df['Pre']
del df['Pre']
data_x = df
#print data_x
#print data_y
X_test = numpy.array(data_x, dtype=float)
Y_test = numpy.array(data_y, dtype=float)

#print X_test.shape
#print Y_test.shape

##################### Processing the data ###########

X_test_t = numpy.transpose(X_test)
print X_test
print X_test_t
Identity_mat = numpy.identity(5)

Err = []
ErrX = []

f=-13.78
j=0.0001
for i in range(0, 100,1):
    t1 = numpy.dot(X_test_t, X_test)
    t2 = (f+j)*Identity_mat
    f=f+j
    t3 = numpy.add(t1,t2)
    t4 = numpy.linalg.inv(t3)
    t5 = numpy.dot(t4,X_test_t)
    a = numpy.dot(t5,Y_test)

    Y_new = numpy.dot(X_test,a)
    ErrorY = numpy.array(numpy.subtract(Y_test,Y_new))
    #print ErrorY
    error = 0
    for k in range(0,ErrorY.size,1):
        if ErrorY[k] >= (-0.1) and ErrorY[k] <= (0.1):
            error=error+1
    sizeOfErrorY = ErrorY.size
    error = float(float(error)/float(sizeOfErrorY))
    error = error*float(100)
    ErrX.append(f-j)
    Err.append(error)

##################   Plotting Error  vs lamda ##############
print Err
plt.scatter(ErrX, Err)
plt.show()

############ Lambda Decision################

lmd = -13.78
t1 = numpy.dot(X_test_t, X_test)
t2 = lmd*Identity_mat
t3 = numpy.add(t1,t2)
t4 = numpy.linalg.inv(t3)
t5 = numpy.dot(t4,X_test_t)
a_best = numpy.dot(t5,Y_test)
Y_new = numpy.dot(X_test,a_best)
#print Y_new

wr = [7, 9.5, 4.2 , 6.1, 8]
w = numpy.array(wr)
y = numpy.dot(w,a_best)
#print y
