def process(input):
    if not input:
        return []
        
    start = end = 0
    
    s = input["sentence"]
    matches = input["matches"]
    
    ind = []
    for match in matches:
        if match["should_highlight"]:
            ind.append((match["start_index"], match["end_index"]))
    
    output = []
    i = 0
    while end < len(s):
        while end < len(s) and s[end] != ' ':
            end += 1
        word = s[start:end]
        
        should_highlight = False
        if start <= ind[i][0] and end >= ind[i][1]:
            should_highlight = True
            i += 1
        
        output.append({"word":word, "should_highlight":should_highlight})
    
        while end < len(s) and s[end] == ' ':
            end += 1
        start = end
        
    return output
        
input = {
    "sentence": "foobar badword lorem ipsum badword2 blah badword",
    "matches": [
        {
            "start_index": 7,
            "end_index": 13,
            "should_highlight": False
        },
        {
            "start_index": 27,
            "end_index": 34,
            "should_highlight": True
        },
        {
            "start_index": 42,
            "end_index": 46,
            "should_highlight": True
        }
    ]
}

print(process(input))