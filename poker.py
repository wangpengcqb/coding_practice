order = ['A', 'K', 'Q', 'J'] + list(str(i) for i in range(10, 1, -1))


a = ['5H', '2H', 'AH']
hands = [['5H', '2H', 'AH'], ['7D', '8D', '9D'], ['2S', 'JC', '3S'], ['KH', 'QS', 'JC']]

a.sort(key=lambda x: order.index(x[0]))
print(a)

for hand in hands:
    hand.sort(key=lambda x: order.index(x[0]))
    
hands.sort(key=lambda x: order.index(x[0][0]))

print(hands)