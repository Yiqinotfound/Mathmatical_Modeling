N = 7

weight = [35, 30, 60, 50, 40, 10, 25]
value = [10, 40, 30, 50, 35, 40, 30]

capacity = 150

# 初始化dp数组
dp = [[0 for i in range(capacity+1)] for i in range(N+1)]

# 递推计算
for i in range(1,N+1):
    for j in range(1,capacity+1):
        if j > weight[i-1]: # 背包容量大于物品重量
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+value[i-1])
        else :
            dp[i][j] = dp[i-1][j]
            
            
print(dp[N][capacity])