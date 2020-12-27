from copy import deepcopy
import bisect
def mincoins(coins, target):
    if not coins:
        return []
        
    dp = [float('inf') for i in range(target+1)]
    res = [[] for i in range(target+1)]
    
    dp[0] = 0 
    
    for coin in coins:
        for x in range(coin, target+1):
            if dp[x] > dp[x-coin]+1:
                dp[x] = dp[x-coin]+1
                val = deepcopy(res[x-coin])
                val.append(coin)
                res[x] = val
            
    if res[target]:
        res[target].sort(reverse=True)
        return res[target]
    
    # Didn't find exact match, use greedy
    coins.sort()
    
    i = bisect.bisect_left(coins, target)-1
    output = []
    while target >= coins[i]:
        n = target//coins[i]
        output.extend([coins[i]]*n)
        target = target - n*coins[i]
        i -= 1
        
    return output

coins = [1,3,5,10]
target = 33

print(mincoins(coins, target))

coins = [5,10]
target = 33

print(mincoins(coins, target))

coins = [10,20,50]
target = 189

print(mincoins(coins, target))