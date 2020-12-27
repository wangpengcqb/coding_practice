from copy import deepcopy
def mincoins(coins, target):
    if not coins:
        return []
        
    dp = [float('inf') for i in range(target+1)]
    res = [[0 for i in range(len(coins))] for i in range(target+1)]
    
    dp[0] = 0 
    
    for i, coin in enumerate(coins):
        for x in range(coin, target+1):
            if dp[x] > dp[x-coin]+1:
                dp[x] = dp[x-coin]+1
                val = deepcopy(res[x-coin])
                val[i] += 1
                res[x] = val
    return res[-1]

coins = [1,5,10,25]
target = 33

print(mincoins(coins, target))