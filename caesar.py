
class Node:
    def __init__(self, nm, end=0):
        self.nm = nm
        self.end = end
        self.childs = []

def comm_prefix(s1, s2):
    n1 = len(s1); n2 = len(s2)
    min_len = n1 if n1 < n2 else n2
    idx = -1
    while idx < min_len-1 and s1[idx+1] == s2[idx+1]:
        idx +=1
    return idx

def add_suffix(node, s):
    for child in node.childs:
        idx = comm_prefix(child.nm, s)
        if idx >= 0:
            add_suffix(child, s[idx:])
            return
    
    node.childs.append(Node(s, 1))
                

def build_suffix_tree(s):
    n = len(s)
    root = Node('root', 0)

    for i in range(n):
        suffix = s[i:]
        print(suffix)
        add_suffix(root, suffix)
    print('-------------')
    return root

root = build_suffix_tree('tatat')
q = [root]

while q:
    n = q.pop()
    print(n.nm)
    for c in n.childs:
        q.append(c)