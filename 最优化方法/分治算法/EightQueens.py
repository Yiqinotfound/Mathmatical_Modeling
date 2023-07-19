# 爬山法
import random
# status[col] 代表col列的皇后所在的行数

#爬山法
import random
 
 
def num_of_conflict(status):  # 获取该状态下互相攻击的皇后对数
	num_of_conflict = 0
	for col1 in range(0, 7):
		for col2 in range(col1+1, 8):
			if (status[col1] == status[col2]) \
			or ((col2 - col1) == abs(status[col1] - status[col2])) : #判断是否相互攻击
				num_of_conflict += 1
	return num_of_conflict
 
 
 
def get_min_num_of_conflict_status(status):   #返回该状态status时的最优邻居状态，如不存在，则返回本身
	min_status = status
	for col in range(0,8):  #此处两个循环为遍历56种邻居
		for row in range(0, 8):
			new_status = status[:]
			if status[col] != row:  #相等时跳过，此时是皇后位置
				new_status[col] = row
				if num_of_conflict(new_status) < num_of_conflict(min_status): 
					min_status = new_status   #new_status的相互攻击皇后数小于min_status，所以更min_status
				elif num_of_conflict(new_status) == num_of_conflict(min_status) \
				and num_of_conflict(new_status) != num_of_conflict(status): 
					choose = random.randint(0, 1)  
					if choose == 1:   #当新状态的h也是最小时，根据概率（0,1）随机决定刷新
						min_status = new_status
	return min_status  

def print_board(status):
    for row in range(8):
        pos = status.index(row)
        for col in range(8):
            if col == pos:
                print('*', end=' ')
            else:
                print('-', end=' ')
        print()
                
        
                
                
status = [0 for _ in range(8)]
for col in range(0, 8):   #生成随机八皇后棋盘
	row = random.randint(0, 7)
	status[col] = row
print("the initial status: ")
print(status)
print("the num of conflict: ")
print(num_of_conflict(status))
while num_of_conflict(status) > 0 : #当不为解时
	new_status = get_min_num_of_conflict_status(status)  #获得当前状态的最优邻居
	if new_status == status:  #最优邻居就是自己，证明h已经是最小了
		print("the new status: ") 
		print(status)
		print("the num of conflict: ")
		print(num_of_conflict(status))
		print("can't find a answer!")
		break
	status = new_status
	print("the new status: ")
	print(status)
	print("the num of conflict: ")
	print(num_of_conflict(status))
	if num_of_conflict(status) == 0:
		print_board(status)

        

  

