from random import choice
def generate(s, grammar):
    
    def helper(s, grammar):
        
        if s not in grammar.keys():
            return s
        
        val = choice(grammar[s])
        if isinstance(val, str):
            return val
            
        res = ''
        for e in val:
            space = ' ' if res else ''
            res = res + space + helper(e, grammar)
                
        return res

    return helper(s, grammar)


grammar = dict( 
    # A grammar for a trivial subset of English.
    S = [['NP','VP'],['S','and','S']],
    NP = [['Art', 'N']],
    VP = [['V', 'NP']],
    Art = ['the', 'a'],
    N = ['man', 'ball', 'woman', 'table'],
    V = ['hit', 'took', 'saw', 'liked']
)
print(generate('S', grammar))

print(generate('NP', grammar))

print(generate('VP', grammar))

print(generate('N', grammar))