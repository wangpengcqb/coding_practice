from collections import defaultdict
import itertools
def find_pairs(student_course_pairs):
    
    student = defaultdict(set)
    for pair in student_course_pairs:
        student[int(pair[0])].add(pair[1])
        
    
    res = dict()
    for p in itertools.combinations(student.keys(), 2):
        res[p] = list(set.intersection(student[p[0]], student[p[1]]))
        
    return res


student_course_pairs_1 = [
  ["58", "Software Design"],
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
]

print (find_pairs(student_course_pairs_1))

student_course_pairs_2 = [
  ["42", "Software Design"],
  ["0", "Advanced Mechanics"],
  ["9", "Art History"],
]

print(find_pairs(student_course_pairs_2))


def find_mid_course(all_courses):
    
    indegree = defaultdict(int)
    graph = dict()
    node = set()
    for c in all_courses:
        indegree[c[1]] += 1
        graph[c[0]] = c[1]
        node.add(c[0])
        node.add(c[1])
    
    start = None    
    for n in node:
        if indegree[n] == 0:
            start = n
    
    if not start:
        return None
        
    def dfs(node, res, path):
        path.append(node)
        
        if node not in graph:
            res.append(path[len(path)//2])
            return 
            
        nxt = graph[node]
        dfs(nxt, res, path)
        path.pop()
        
        return
        
    res = []
    path = []
    dfs(start, res, path)
    
    return res[0]
        

all_courses = [['A', 'B'], ['C', 'D'], ['B', 'C'], ['E', 'F'], ['D', 'E'], ['F', 'G']]
print(find_mid_course(all_courses))



def find_mid_courses(all_courses):
    
    indegree = defaultdict(int)
    graph = defaultdict(list)
    node = set()
    for c in all_courses:
        indegree[c[1]] += 1
        graph[c[0]].append(c[1])
        node.add(c[0])
        node.add(c[1])

    start = []
    for n in node:
        if indegree[n] == 0:
            start.append(n)
    
    if not start:
        return []
        
    def dfs(node, res, path):
        path.append(node)
        
        if node not in graph:
            res.add(path[(len(path)-1)//2])
            return 
            
        for child in graph[node]:
            dfs(child, res, path)
            path.pop()
        return
    
    res = set()  
    for s in start:
        path = []
        dfs(s, res, path)

    return list(res)

all_courses = [['LOGIC', 'COBOL'], ['Data Structures', 'Algorithms'], ['Creative Writing', 'Data Structures'], 
['Algorithms', 'COBOL'], ['Intro to Computer Science', 'Data Structures'], ['LOGIC', 'Compilers'],
['Data Structures', 'LOGIC'], ['Creative Writing', 'System Administration'], ['Databases', 'System Administration'],
['Creative Writing', 'Databases']
]

print(find_mid_courses(all_courses))
