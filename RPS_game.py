def calscore(input):
    if not input or len(input) != 2:
        return dict()
        
    res = {'player1':0, 'player2':0}
    tie = 0
    last = 0
    for i1, i2 in zip(input[0], input[1]):
        s = score(i1, i2)
        if s == 0:
            if last == 0:
                last = 1
            else:
                last *= 2
            tie += last
        if s == 1:
            res['player1'] = res['player1'] + 1 + tie
            tie = 0
        elif s == -1:
            res['player2'] = res['player2'] + 1 + tie
            tie = 0
            
    return res
        
    
def score(i1, i2):
    if i1 == i2:
        return 0
        
    if i1 == 'R' and i2 == 'S' \
    or i1 == 'P' and i2 == 'R' \
    or i1 == 'S' and i2 == 'P':
        return 1
    
    return -1



input = [['R', 'P', 'P', 'S', 'R', 'S'], ['P', 'S', 'P', 'S', 'R', 'P']]

print (calscore(input))