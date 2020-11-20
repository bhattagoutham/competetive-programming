# Author: Goutham Bhatta
# UnionFind (by size)

class UnionFind:

    def __init__(self):
        self.parents = None
        self.max_val = 0
        

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
    
    def get_min(self):
        min_val = self.max_val
        for x in self.parents:
            if x < -1 and abs(x) < min_val:
                min_val = abs(x)
        return min_val

    def set_max(self, ele):
        if abs(self.parents[ele]) > self.max_val:
                self.max_val = abs(self.parents[ele])
        

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
            self.set_max(e1)
        else:
            self.parents[e2] += self.parents[e1]; self.parents[e1] = e2
            self.set_max(e2)

# test-cases
if __name__ == "__main__":
    
    
    uf = UnionFind()

    with open('conn-comp-test-case.txt', 'r') as f:
        
        N = int(f.readline())
        uf.makeset(2*N)
        
        lnum = 0

        while N>0:
            query = f.readline()[0:-1] # ignoring the new-line
            print(lnum,": ", query)

            e1, e2 = query.split()
            e1 = int(e1); e2 = int(e2)

            uf.merge(e1, e2)
            N -= 1; lnum+=1
        min_val = uf.get_min()
        print(min_val, uf.max_val)
        print(uf.parents)
