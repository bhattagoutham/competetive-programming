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

        

def lca(root, v1, v2):

    if root == None:
        return -1
    if root.info == v1:
        return v1
    if root.info == v2:
        return v2

    l = lca(root.left, v1, v2)
    r = lca(root.right, v1, v2)

    if l != -1 and r != -1 and l+r == v1+v2:
        return root.info
    elif l != -1:
        return l
    elif r!= -1:
        return r
    else:
        return -1




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans)




