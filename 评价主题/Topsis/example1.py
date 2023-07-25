import numpy as np

def inter_to_max(x,a,b): # 区间型的正向化函数
    '''
    para:
        x: 原始评价矩阵中的列向量
    '''
    len_x = len(x)
    M = max([a-min(x),max(x)-b])
    posit_x = np.zeros(len_x)
    for i in range(len_x):
        if x[i] < a:
            posit_x[i] = 1-(a-x[i])/M
        elif x[i] > b:
            posit_x[i] = 1-(x[i]-b)/M
        else:
            posit_x[i] = 1
        
    return posit_x

def mid_to_max(x,best): # 中间型的正向化函数
    '''
    para:
        x: 原始评价矩阵中的列向量
        best: 最优值
    '''
    M = max(np.abs(x-best))
    posit_x = 1-np.abs(x-best)/M 
            
    return posit_x

def min_to_max(x):
    '''
    para:
        x: 原始评价矩阵中的列向量
    '''
    posit_x = max(x)-x
    return posit_x

def positivisation(x,method,col): # 正向化函数
    '''
    para:
        x: 原始评价矩阵中的列向量
        method: 正向化的方法，是字符串
        col: x所在的列
    '''
    posit_x = np.zeros(len(x))
    if method == 'inter_to_max':
        print('第',col,'列采用区间型的正向化函数')
        a = float(input('请输入区间的下限：'))
        b = float(input('请输入区间的上限：'))
        posit_x = inter_to_max(x,a,b)
        print('第',col,'列正向化后的值为：',posit_x)
        print('------------------------------------')
    elif method == 'mid_to_max':
        print('第',col,'列采用中间型的正向化函数')
        best = float(input('请输入最优值：'))
        posit_x = mid_to_max(x,best)
        print('第',col,'列正向化后的值为：',posit_x)
        print('------------------------------------')
    elif method == 'min_to_max':
        print('第',col,'列采用最小型的正向化函数')
        posit_x = min_to_max(x)
        print('第',col,'列正向化后的值为：',posit_x)
        print('------------------------------------')
    elif method == '0':
        return x
    return posit_x

def normalisation(x): # 归一化函数,对每一列进行向量归一化
    '''
    para:
        x: 原始评价矩阵
    '''
    len_x = len(x) # 行数
    len_y = len(x[0]) # 列数
    norm_x = np.zeros((len_x,len_y))
    for i in range(len_y):
        norm_x[:,i] = x[:,i]/np.sqrt(sum(x[:,i]**2))
        
    return norm_x

def best_and_worst(x):
    '''
    para:
        x: 归一化之后的评价矩阵
    '''
    len_x = len(x) # 行数
    len_y = len(x[0]) # 列数
    best = np.zeros(len_y)
    worst = np.zeros(len_y)
    for i in range(len_y):
        best[i] = max(x[:,i])
        worst[i] = min(x[:,i])
        
    return best,worst

def weight(x): # 用熵权法计算权重
    '''
    para:
        x: 原始评价矩阵
    '''
    norm_x = normalisation(x)
    weight = np.zeros(len(x[0]))
    len_x = len(x) # 行数
    len_y = len(x[0]) # 列数
    for i in range(len_y):
        weight[i] = np.sum(norm_x[:,i]*np.log(norm_x[:,i]))/(-len_x)
    
    return weight

def topsis(x):
    m,n = x.shape
    print('有',m,'个评价对象，',n,'个评价指标')
    for i in range(n):
        method = input('请输入第'+str(i+1)+'个指标的正向化方法（不需正向化输入0)：')
        x[:,i] = positivisation(x[:,i],method,i+1)
        
    norm_x = normalisation(x)
    print('归一化后的评价矩阵为：\n',norm_x)
    weight_ = weight(x)
    print('权重为：',weight_)
    
    # 计算各个对象与最优最劣方案的距离
    
    best,worst = best_and_worst(norm_x)
    print('最优方案为：',best)
    print('最劣方案为：',worst)
    dist_best = np.zeros(m)
    dist_worst = np.zeros(m)
    for i in range(m):
        dist_best[i] = np.sqrt(sum((norm_x[i,:]-best)**2))
        dist_worst[i] = np.sqrt(sum((norm_x[i,:]-worst)**2))
        
    print('各个对象与最优方案的距离为：',dist_best)
    print('各个对象与最劣方案的距离为：',dist_worst)
    
    # 计算各个对象的综合得分
    score = dist_worst/(dist_best+dist_worst)
    print('各个对象的综合得分为：',score)
    
    # 对各个对象的综合得分进行排序
    rank = np.argsort(score)
    print('各个对象的综合得分排序为：',rank)
    

    