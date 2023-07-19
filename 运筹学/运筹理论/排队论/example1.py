# 1. lambda: 指顾客相继到达时间服从参数为lambda的负指数分布
# 2. mu: 指服务时间服从参数为mu的负指数分布
# 3. s: 服务台数
# 4. k: 系统容量上限，inf代表无穷大

# 1. L:平均队伍长度,系统中的总人数期望
# 2. Lq:平均等待队伍长度
# 3. W:平均逗留时间
# 4. Wq:平均等待时间

import math
def queuing_theory(lambdam,mu,s,k):
    """
    根据四个参数计算排队系统性能指标
    """
    ro=lambdam/mu  #计算顾客与服务台的来往强度
    ros=lambdam/mu/s
    sum1=sum2=0
    if s==1:
        if k=='inf':  #单服务台，系统容量为无穷大
            L=lambdam/(mu-lambdam) #平均队长
            Lq=ro**2/(1-ro) #平均等待队长
            W=1/(mu-lambdam) #平均逗留时间
            Wq=lambdam/(mu*(mu-lambdam))  #平均等待时间
        else:   #单服务台，系统容量为k
            p0=(1-ro)/(1-ro**(k+1))
            pk=ro**k*p0
            L=ro/(1-ro)-(k+1)*ro**(k+1)/(1-ro**(k+1))
            Lq=ro/(1-ro)-ro*(1+k*ro**k)/(1-ro**(k+1))
            W=L/(lambdam*(1-pk))
            Wq=Lq/(lambdam*(1-pk))
    else:
        if k=='inf':  #多服务台，系统容量为无穷大
            for i in range(s):
                sum1+=1/math.factorial(i)*ro**i
            p0=sum1+(1/math.factorial(s))*ro**s*(s*mu/(s*mu-lambdam))
            p0=1/p0
            Lq=ro**s*lambdam*mu*p0/(math.factorial(s-1)*(s*mu-lambdam)**2)
            Wq=Lq/lambdam
            L=Lq+ro
            W=L/lambdam
        else:  #多服务台，系统容量为k
            sum1=0;sum2=0;
            for i in range(s):
                sum1+=ro**i/math.factorial(i)
            for i in range(s):
                sum2+=(i-s)*ro**i/math.factorial(i)
            p0=sum1+ro**s*(1-ros**(k-s+1))/(math.factorial(s)*(1-ros))
            p0=1/p0
            pk=ro**k/(math.factorial(s)*s**(k-s))*p0
            lambdam_e=lambdam*(1-pk)  #顾客到达率
            Lq=p0*ro**s*ros/(math.factorial(s)*(1-ros)**2)*(1-ros**(k-s+1)-(1-ros)*(k-s+1)*ros**(k-s))
            L=Lq+s+p0*sum2
            W=L/lambdam_e
            Wq=W-1/mu
    return [L,Lq,W,Wq]