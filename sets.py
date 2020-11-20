# Author: Goutham Bhatta
# UnionFind (by size)

class UnionFind:

    def __init__(self):
        self.parents = None

    # initializes a set of n distinct elements
    def makeset(self, n):
        self.parents = [-1]*(n+1)

    # returns the root node of the set, as well no.of elements in the set
    def get_root(self, ele, printNoE=False):
        
        path_lst = []   # for path compression
        while self.parents[ele] > 0:
            path_lst.append(ele)
            ele = self.parents[ele]
        # for path compression
        for x in path_lst:
            self.parents[x]=ele
        # print nof elements in the set
        if printNoE:
            print(abs(self.parents[ele]))
    
        return ele

    # merges two elements
    def merge(self, e1, e2):
        
        if self.parents[e1] > 0:
            e1 = self.get_root(e1)
        if self.parents[e2] > 0:
            e2 = self.get_root(e2)
        
        # if both belong to same set
        if e1 == e2:
            return
        
        # merges the small set as subtree of the larger one
        if self.parents[e1] > self.parents[e2]:
            self.parents[e1] += self.parents[e2]; self.parents[e2] = e1
        else:
            self.parents[e2] += self.parents[e1]; self.parents[e1] = e2

# test-cases
if __name__ == "__main__":
    
    
    uf = UnionFind()

    with open('unionfind-test-case.txt', 'r') as f:
        l = f.readline()
        N, Q = l.split()
        N = int(N); Q = int(Q)
        uf.makeset(N)
        
        lnum = 0

        while Q>0:
            query = f.readline()[0:-1] # ignoring the new-line
            
            if query[0] == 'Q':
                print(lnum,": ", query)
                _, ele = query.split()
                uf.get_root(int(ele), True)
                
            else:
                print(lnum,": ", query)
                q, e1, e2 = query.split()
                e1 = int(e1); e2 = int(e2)
                uf.merge(e1, e2)
            Q -= 1; lnum+=1
