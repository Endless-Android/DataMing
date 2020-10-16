import re
import numpy
from sklearn import linear_model
from matplotlib import pyplot as plt
fn = open('data.txt','r')
all_data = fn.readlines()
fn.close()
x = []
y = []
# print(all_data)
for single_data in all_data:
    tmp_data = re.split('\t|\n',single_data)
    x.append(float(tmp_data[0]))
    y.append(float(tmp_data[1]))
x = numpy.array(x).reshape([100,1])
y = numpy.array(y).reshape([100,1])
#plt.scatter(x,y)
#plt.show()
model = linear_model.LinearRegression()
model.fit(x,y)
model_coef = model.coef_
model_intercept = model.intercept_
r2 = model.score(x,y)
new_x = [84610,80000]
pre_y = model.predict(numpy.array(new_x).reshape(-1,1))
print(pre_y)