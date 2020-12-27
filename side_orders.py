import heapq
def sideorders(orders):
    if not orders or len(orders) == 1:
        return 0
        
    buy = []
    sell = []
    
    cnt = 0
    
    for order in orders:
        if order[2] == 'buy':
            buy_cnt = order[1]
            buy_price = order[0]
            while sell and sell[0][0] <= buy_price and buy_cnt > 0:
                sell_price, sell_cnt = heapq.heappop(sell)
                if buy_cnt == sell_cnt:
                    cnt += sell_cnt
                    buy_cnt -= sell_cnt
                elif buy_cnt < sell_cnt:
                    sell_cnt -= buy_cnt
                    cnt += buy_cnt
                    heapq.heappush(sell, (sell_price, sell_cnt))
                    buy_cnt = 0
                else:
                    cnt += sell_cnt
                    buy_cnt -= sell_cnt
            if buy_cnt > 0:
                heapq.heappush(buy, (-buy_price, buy_cnt))
        
        elif order[2] == 'sell':
            sell_price = order[0]
            sell_cnt = order[1]
            while buy and -buy[0][0] > sell_price and sell_cnt > 0:
                buy_price, buy_cnt = heapq.heappop(buy)
                if sell_cnt == buy_cnt:
                    cnt += buy_cnt
                    sell_cnt = 0
                elif sell_cnt < buy_cnt:
                    buy_cnt -= sell_cnt
                    cnt += sell_cnt
                    heapq.heappush(buy, (buy_price, buy_cnt))
                    sell_cnt = 0
                else:
                    cnt += buy_cnt
                    sell_cnt -= buy_cnt
            if sell_cnt > 0:
                heapq.heappush(sell, (sell_price, sell_cnt))
    return cnt
 

orders = [[150, 5, 'buy'], [190, 1, 'sell'], [200, 1, 'sell'], [100, 9, 'buy'], [140, 8, 'sell'], [210, 4, 'buy']]
print(sideorders(orders))

orders = [[150, 10, "buy"], [165, 7, "sell"], [168, 3, "buy"], [155, 5, "sell"], [166, 8, "buy"]]
print(sideorders(orders))