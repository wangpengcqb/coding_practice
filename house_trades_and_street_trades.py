def exact_match(house_trade, street_trade):
    return house_trade.strip() == street_trade.strip()
    
def attribute_match(house_trade, street_trade):
    return house_trade[:house_trade.rfind(',')] == street_trade[:street_trade.rfind(',')]

def process(house_trades, street_trades, match_function):
    
    house_trades.sort()
    street_trades.sort()
    
    house_left = []
    street_left = []
    i = j = 0
    while i < len(house_trades) and j < len(street_trades):
        house_trade = house_trades[i]
        street_trade = street_trades[j]
        
        if match_function(house_trade, street_trade):
            i += 1
            j += 1
        elif house_trade < street_trade:
            house_left.append(house_trade)
            i += 1
        else:
            street_left.append(street_trade)
            j += 1
            
    return (house_left+house_trades[i:], street_left+street_trades[j:])


def match_trades(house_trades, street_trades):
    
    h, s = process(house_trades, street_trades, exact_match)
    
    h, s = process(h, s, attribute_match)
    
    change = dict()
    new_h = []
    for each in h:
        vec = each.split(',')
        if vec[1] == 'B':
            vec[1] = 'S'
        elif vec[1] == 'S':
            vec[1] = 'B'
        new_s = ','.join(vec)
        new_h.append(new_s)
        change[new_s] = each

    h, s = process(new_h, s, attribute_match)
    
    h = list(map(lambda x: change[x] if x in change.keys() else x, h))
    return h + s
    


house_trades = ["AAPL,B,0100,ABC123", "AAPL,S,0100,ABC123", "GOOG,S,0050,CDC333", "AAPL,S,0100,ABC534", "TSLA,S,0030,VBS643", "FB,S,0100,GBG710"]
street_trades = ["FB,B,0100,GBGGGG", "AAPL,B,0100,ABC123", "AAPL,B,0100,ABC456", "GOOG,S,0050,CDC76432", "AAPL,B,0100,ABC845" ]

print(match_trades(house_trades, street_trades))