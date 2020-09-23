import numpy as np 
import matplotlib.pyplot as plt 
from polynomial_regression.polyregress import polynomial_regression as pr
import time 


n=1000000
deg=1
a=[i%12 for i in range(n)]
b=[i**deg+2*i+3 for i in a]

x=np.asarray(a)
y=np.asarray(b)

pr_regress_time=[]
np_polyfit_time=[]
np_polynomial_time=[]

for i in range(50):
    t1=time.time()
    c=pr.regress(x,y,deg)
    t2=time.time()
    pr_regress_time.append(t2-t1)

for i in range(50):
    t1=time.time()
    c=np.polyfit(x,y,deg)
    t2=time.time()
    np_polyfit_time.append(t2-t1)

a=np.median(pr_regress_time)
b=np.median(np_polyfit_time)
ratio=b/a 
print(a, b, ratio)

'''
x=np.linspace(1,200,num=200)
plt.plot(x[25:200], pr_regress_time[25:200], label="pr_regress_time")
plt.plot(x[25:200], np_polyfit_time[25:200], label="np_polyfit_time")
plt.legend()
plt.show()
'''