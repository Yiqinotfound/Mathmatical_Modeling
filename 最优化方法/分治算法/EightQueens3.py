# 遗传算法

# 遗传算法是模拟达尔文进化论的自然选择和遗传学机理的生物进化过程的计算模型
# ，是一种通过模拟自然进化过程搜索最优解的方法，是随机束搜索的一个变形
# ，通过将两个父状态结合来生成后续。以八皇后问题来说明遗传算法，随机生成K个状态，以一定概率
# （不相互攻击的皇后对数越多，概率越大）选择两个状态，通过交换前N（0 < N < 8）个位置获得两个新的后代，
# 同时将K个后代继续配对。配对过程可能产生变异，此时实验设置变异概率为10%。K在本次实验设为4.
import random
 
def get_num_of_no_conflict(status): # 获取该状态下不互相攻击的皇后对数
	num_of_conflict = 0
	for col1 in range(0, 7):
		for col2 in range(col1+1, 8):
			if (status[col1] == status[col2]) \
			or ((col2 - col1) == abs(status[col1] - status[col2])) : #判断是否相互攻击
				num_of_conflict += 1
	return 28 - num_of_conflict #此处是求不相互攻击的
 
def get_parent(all_status, no_conflict_num):  #按照比例求状态群的某一个状态作为父亲之一
	choose_parent = random.randint(0, sum(no_conflict_num) - 1)
	if choose_parent < no_conflict_num[0]:
		return all_status[0]
	elif choose_parent >= no_conflict_num[0] and choose_parent < (no_conflict_num[0] + no_conflict_num[1]):
		return all_status[1]
	elif choose_parent >= (no_conflict_num[0] + no_conflict_num[1])  \
	and choose_parent < (no_conflict_num[0] + no_conflict_num[1] + no_conflict_num[2]):
		return all_status[2]
	return all_status[3]
 
 
def variation(all_status):  #变异
	for i in range(0, 4):
		col = random.randint(0, 7)
		row = random.randint(0, 7)
		all_status[i][col] = row
	return all_status
 
def inheritance(all_status):  #杂交
	no_conflict_num = []
	new_all_status = []

	for i in range(0, 4):
		no_conflict_num.append(get_num_of_no_conflict(all_status[i]))
	for t in range(0, 2): #一次生成两个子代，循环两次
		father = get_parent(all_status, no_conflict_num)
		mother = get_parent(all_status, no_conflict_num)
		while father == mother:
			mother = get_parent(all_status, no_conflict_num)
		first_child = father[:]
		second_child = mother[:]
		num = random.randint(0, 6)  #各种交换下标0-num的数，形成子代
		for i in range(0, num+1):
			first_child[i] = second_child[i]
			second_child[i] = father[i]
		new_all_status.append(first_child)
		new_all_status.append(second_child)
	return new_all_status #返回新的状态种族
 
def find_answer(all_status): #判断该状态种族是否有解
	for i in range(0, 4):
		if get_num_of_no_conflict(all_status[i]) == 28:
			print("find a answer:")
			print(all_status[i])
			return True
	return False
 
 
all_status = []
for i in range(0, 4):  #随机生成4个状态，即种族
	status = [0, 0, 0, 0, 0, 0, 0, 0]
	for col in range(0, 8):
		row = random.randint(0, 7)
		status[col] = row
	all_status.append(status)
print("the initial all_status: ")
print(all_status)
all_status = inheritance(all_status) #杂交
while find_answer(all_status) == False:  #找不到最优后代（最优解）则一直繁衍
	whether_variation = random.randint(1, 10) #10%变异的几率
	if whether_variation == 1:
		print("have a variation,and the all_status:")
		all_status = variation(all_status)
		print(all_status)
	else:
		all_status = inheritance(all_status) #杂交
		print("the next all_status: ")
		print(all_status)