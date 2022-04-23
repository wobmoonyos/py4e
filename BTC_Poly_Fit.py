import numpy as np
import matplotlib.pyplot as plt

time = [.741,1.511,2.348,3.282,4.283,5.283,11.55,13.083,23.83]
distance = [5.2,10.4,15.6,20.8,26,31.2,38,51.56,74.55]
f = np.polyfit(distance,time,3)
print (f)

g= np.poly1d(f)
print (g)

print(g(62))
x = np.arange(1,100,1)

z=[]
for i in x:
    z.append(g(i))
    i+=1

plt.plot(x,z,'bo')
plt.plot(distance,time ,'+', color='red')
plt.xlim(0,100)
plt.ylim(0,35)
plt.show()
