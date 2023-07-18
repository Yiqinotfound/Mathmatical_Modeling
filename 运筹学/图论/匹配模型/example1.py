# 稳定匹配,以婚配问题为例：

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  
# Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
plt.rcParams['axes.unicode_minus'] = False    
# 解决Matplotlib坐标轴负号'-'显示为方块的问题

N = 2000
# 男女偏好矩阵
np.random.seed(3)
wpref1 = np.random.rand(N,N)
mpref1 = np.random.rand(N,N)

# 画出表格

fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,10))

ax1.set_title('Women Preference Table')
im1 = ax1.imshow(wpref1,  interpolation='nearest', cmap='Blues')
plt.colorbar(im1, ax=ax1)

ax2.set_title('Man Preference Table')
im2 = ax2.imshow(mpref1,  interpolation='nearest', cmap='Oranges')
plt.colorbar(im2, ax=ax2)

plt.show()

# 根据偏好矩阵进行排序
wpre = [] 
mpre = []

for i in range(N):
    temp1 = [i for i in range(N)]
    temp2 = [i for i in range(N)]
    zipped_1 = sorted(zip(wpref1[i],temp1),reverse=True)
    zipped_2 = sorted(zip(mpref1[i],temp2),reverse=True)
    temp1_sorted = [t[1] for t in zipped_1]
    temp2_sorted = [t[1] for t in zipped_2]
    wpre.append(temp1_sorted)
    mpre.append(temp2_sorted)
   

# 记录男女的匹配情况

wmatch = [False]*N
mmatch = [False]*N

# 记录拒绝情况,reject[i][j]表示女生j是否拒绝过男生i

reject = [[False]*N for _ in range(N)]

# 开始配对
pursuers_matrix = [[] for _ in range(N)] # 每个女生的追求者矩阵
mmatch_dic = {} # 男生的匹配字典
wmatch_dic = {} # 女生的匹配字典
round = 0
m_score = []  # 男生对象的得分
w_score = []  # 女生对象的得分
while(True):
    round += 1
    if False not in mmatch:
        break
    # 男生的一轮追求：
    for i in range(0,N):
        if  mmatch[i] == False: # 如果男生没有npy,就开始追求
            for j in range (0,N) : # 从最喜欢的女生mpre[i][0]开始追求
                if reject[i][mpre[i][j]] == False: # 如果没有拒绝过，就表白，成为mpre[i][j]女生的追求者
                    pursuers_matrix[mpre[i][j]].append(i)  
                    break                  
    # 男生的追求结束后，女生开始选择：
    
    for i in range(0,N):
        if len(pursuers_matrix[i]) > 1 or (len(pursuers_matrix[i]) == 1 and wmatch[i] == False): # 如果追求者大于1，或者追求者为1但是女生没有匹配
            best_boy = -1
            max_score = -1
            for pursuer in pursuers_matrix[i]:
                if wpref1[i][pursuer] > max_score:
                    max_score = wpref1[i][pursuer]
                    best_boy = pursuer

            if wmatch[i] == False: # 没有匹配
                for pursuer in pursuers_matrix[i]:
                    if  pursuer == best_boy:
                        continue
                    else:
                        reject[pursuer][i] = True
                wmatch[i] = True
                mmatch[best_boy] = True
                pursuers_matrix[i] = []
                pursuers_matrix[i].append(best_boy)
                mmatch_dic[best_boy] = i
                wmatch_dic[i] = best_boy
            else: # 有匹配
                if not pursuers_matrix[i][0] == best_boy: # 如果best-boy不是原来的匹配者，直接抛弃
                    mmatch[pursuers_matrix[i][0]] = False 
                    mmatch_dic.pop(pursuers_matrix[i][0])
                    reject[pursuers_matrix[i][0]][i] = True # pursuers_matrix[i][0]被女生i拒绝
                    mmatch[best_boy] = True
                    pursuers_matrix[i] = [best_boy]
                    mmatch_dic[best_boy] = i
                    wmatch_dic[i] = best_boy
                else: # 如果是原来的匹配者，只需重置pursuers_matrix[i]，并拒绝剩下的追求者
                    for pursuer in pursuers_matrix[i]:
                        if pursuer == best_boy:
                            continue
                        else:
                            reject[pursuer][i] = True
                    pursuers_matrix[i] = [best_boy] 
                    
                    
                
        else:
            continue
        
    # 每一轮配对后，记录每个男生的匹配对象的平均得分，没有对象的不计算，记录每个女生匹配对象的平均得分，没有对象的不计算
    sum_score1 ,sum_score2 = 0,0
    cnt_1,cnt_2 = 0,0
    for i in range(N):
        if mmatch[i] == True:
            cnt_1 += 1
            sum_score1 += mpref1[i][mmatch_dic[i]]
        
        if wmatch[i] == True:
            cnt_2 += 1
            sum_score2 += wpref1[i][wmatch_dic[i]]
    
    m_score.append(sum_score1/cnt_1)
    w_score.append(sum_score2/cnt_2)
    
   
    
        
        
        
# 生成匹配结果矩阵 match_result[i][j]表示女生j是否和男生i匹配（现在match_matrix和match_result是一样的）

match_result = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    match_result[pursuers_matrix[i][0]][i] = 1

# 男生的匹配结果
gf = [0 for _ in range(N)]
for i in range(N):
    gf[pursuers_matrix[i][0]] = i
# 作出匹配图像

x_1 = [-0.5] * N  # 所有点的 x 坐标都为 0
y = list(range(0,4*N,4))  # 点的 y 坐标为 0 到 N-1
x_2 = [0.5] * N  

# 绘制点的散点图
fig = plt.figure(figsize=(5, 20))
plt.scatter(x_1, y, c='b', marker='o', s=50, alpha=0.5,) # type: ignore
plt.scatter(x_2, y, c='r', marker='o', s=50, alpha=0.5) # type: ignore

for i in range(N):
    plt.text(x_1[i]-0.1, y[i], str(i+1), fontsize=8, color='b', ha='right', va='center')
    plt.text(x_2[i]+0.1, y[i], str(i+1), fontsize=8, color='r', ha='left', va='center')
# 绘制点的连线图
for i in range(N):
    plt.plot([x_1[i], x_2[match_result[i].index(1)]], [y[i], y[match_result[i].index(1)]], 'k-', alpha=0.5)
    
# 设置坐标轴范围和标签
plt.xlim(-1, 1)
plt.ylim(-1, 4*N)


# 显示图像
plt.axis('off')
plt.savefig("test.svg", dpi=300,format="svg")
plt.show()

# 画出匹配得分图像随着轮数的变化
print(len(m_score),len(w_score))
print(round)
plt.plot(range(1,round),m_score,label = '男生匹配对象得分')

plt.plot(range(1,round),w_score,label = '女生匹配对象得分')

plt.xlabel('轮数')
plt.ylabel('匹配得分')
plt.legend()
plt.show()


