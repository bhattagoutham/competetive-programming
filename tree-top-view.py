class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


class Q:
    def __init__(self):
        self.q = []
    
    def __str__(self):
        return ']'.join([str(i) for i in self.q])+']'
    
    def isEmpty(self):
        if len(self.q):
            return False
        return True
        
    def push(self, e):
        # push multiple elemets at once
        if type(e) is list:
            for i in e:
                self.q.append(i)
        else:
            self.q.append(e)
    
    def pop(self):
        if len(self.q):
            temp = self.q[0]
            del self.q[0]
            return temp
        print('Q is Empty')

    def top(self):
        return self.q[0]

def topView(root):
    q = Q()
    q.push([(root, 0), None])
    maxRight = 0; minLeft = 0
    result = [(root, 0)]
    print('\n-----\n')
    while(not q.isEmpty()):
        # for storing travesed level nodes
        # to find the extreme L, R's
        curr_lvl_nodes = []
        
        # level order traversal
        while(q.top()!=None):
            root = q.pop()
            curr_lvl_nodes.append(root)
            if root[0].left:
                q.push((root[0].left,root[1]-1))

            if root[0].right:
                q.push((root[0].right,root[1]+1))

        # # left_most_node of current level
        # left_mst_node = curr_lvl_nodes[0]
        # # lly
        # right_mst_node = curr_lvl_nodes[-1]
        
        for node in curr_lvl_nodes:
            # if True, place node to left side of result
            if node[1] < minLeft:
                minLeft = node[1]
                temp_arr = result
                result = [node]
                result.extend(temp_arr)
            
            # if True place node to right side of result
            if node[1] > maxRight:
                maxRight = node[1]
                result.append(node)
        
        # debug-stmt: prints (node, col-num) of a level
        # print(', '.join(['('+str(i[0].info)+','+str(i[1])+')' for i in curr_lvl_nodes]))
            

        # lvl order traversal
        q.pop()
        if (q.isEmpty()):
            break
        else:
            q.push(None)

    print(' '.join([str(i[0].info) for i in result]))
        

if __name__ == '__main__':
    tree = BinarySearchTree()
    t = int(input())
    arr = list(map(int, input().split()))

    for i in range(t):
        tree.create(arr[i])

    topView(tree.root)


# input

    # 116

    # 37 23 108 59 86 64 94 14 105 17 111 65 55 31 79 97 78 25 50 22 66 46 104 98 81 90 68 40 103 77 74 18 69 82 41 4 48 83 67 6 2 95 54 100 99 84 34 88 27 72 32 62 9 56 109 115 33 15 91 29 85 114 112 20 26 30 93 96 87 42 38 60 7 73 35 12 10 57 80 13 52 44 16 70 8 39 107 106 63 24 92 45 75 116 5 61 49 101 71 11 53 43 102 110 1 58 36 28 76 47 113 21 89 51 19 3

# output

    # 1 2 4 14 23 37 108 111 115 116 83 84 85 