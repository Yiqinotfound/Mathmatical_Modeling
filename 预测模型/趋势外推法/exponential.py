import numpy as np
from matplotlib import pyplot as plt



def exponential_forecast(x,y):
    # 或者从外面加载,yt = np.loadtxt('data.txt')
    n = len(y)
    m = len(y) // 3
    cf = np.diff(y) # 一阶差分数组
    bzh = np.array([cf[i+1]/cf[i] for i in range(n-2)]) # 比值数组
    r = (np.min(bzh),np.max(bzh)) # 比值范围
    s1 = np.sum(y[:m])
    s2 = np.sum(y[m+1:2*m])
    s3 = np.sum(y[2*m+1:])
    b = np.power((s3-s2)/(s2-s1),1/m)
    a = (s2-s1)*(b-1)/(b*np.power((np.power(b,m)-1),2)) # b=((s3-s2)/(s2-s1))^(1/m) a=(s2-s1)*(b-1)/(b*(b^m-1)^2) 
    k = (s1-a*b*(np.power(b,m)-1)/(b-1))/m   # k=(s1-a*b*(b^m-1)/(b-1))/m
    function = lambda x: k + a*np.power(b,x)
    return a,b,k,function(x)    
    
x = np.array([i for i in range(27)])
y = 1+2**x

noise = np.random.normal(0,2,27)
y = y + noise

a,b,k,forcast = exponential_forecast(x,y)

# 可视化

plt.plot(x,y,label='Actual')
plt.plot(x,forcast,label='Forecast')
plt.legend()
plt.show()

print(a,b,k)