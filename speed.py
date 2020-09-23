import numpy as np 
import matplotlib.pyplot as plt 
from polynomial_regression.polyregress import polynomial_regression as pr
import time 


n=60000
deg=1
a=[i%10000 for i in range(n)]
b=[i**2+2*i+3 for i in a]

x=np.asarray(a)
y=np.asarray(b)

pr_regress_time=[]
np_polyfit_time=[]
np_polynomial_time=[]

for i in range(200):
    t1=time.time()
    c=pr.regress(x,y,deg)
    t2=time.time()
    pr_regress_time.append(t2-t1)

for i in range(200):
    t1=time.time()
    c=np.polyfit(x,y,deg)
    t2=time.time()
    np_polyfit_time.append(t2-t1)


'''
x=np.linspace(1,200,num=200)
plt.plot(x[25:200], pr_regress_time[25:200], label="pr_regress_time")
plt.plot(x[25:200], np_polyfit_time[25:200], label="np_polyfit_time")
plt.legend()
plt.show()
'''