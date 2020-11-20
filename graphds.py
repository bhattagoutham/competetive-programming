# 10:41 AM
# 03-OCT-20
# Author : Goutham Bhatta

from collections import deque

class node:
    def __init__(self, vtx, dist, par_vtx):
        self.vtx = vtx
        self.dist = dist
        self.par_vtx = par_vtx
    
    def __lt__(self, other):
        if self.dist < other.dist:
            return True
    
    
class priorityQue:

    def __init__(self):
        self.min_heap = []
    
    def isEmpty(self):
        return True if self.min_heap else False

    def get_parent(self, idx):
        return int((idx-1)/2)
    
    def get_childs(self, idx):
        ec = len(self.min_heap)
        l = 2*idx+1 if 2*idx+1 < ec else -1
        r = 2*idx+2 if 2*idx+2 < ec else -1
        return (l, r)
    
    def swap(self, child_idx, par_idx):
        temp = self.min_heap[child_idx]
        self.min_heap[child_idx] = self.min_heap[par_idx]
        self.min_heap[par_idx] = temp

    def push(self, ele):
        self.min_heap.append(ele)

        if len(self.min_heap) == 1:
            return
        
        curr_idx = len(self.min_heap)-1

        while curr_idx > 0:
            # unsafe indexing opn
            par_idx = self.get_parent(curr_idx)
            if self.min_heap[curr_idx] < self.min_heap[par_idx]:
                self.swap(curr_idx, par_idx)
                curr_idx = par_idx
            else:
                break
    
    def pop(self):
        if len(self.min_heap) == 1:
            temp = self.min_heap[0]
            del self.min_heap[0]
            return temp
        
        min_val = self.min_heap[0]
        self.min_heap[0] = self.min_heap[-1]
        del self.min_heap[-1]
        
        curr_idx = 0

        while True:
            l, r = self.get_childs(curr_idx)

            if l == -1 and r == -1:
                break
            elif l == -1:
                min_child = r
            elif r == -1:
                min_child = l
            else:
                min_child = l if self.min_heap[l] < self.min_heap[r] else r
            
            self.swap(curr_idx, min_child)
            curr_idx = min_child
        return min_val
    

    def find(self, vt):
        idx = 0; found = False
        for i, ele in enumerate(self.min_heap):
            if vt == ele.vtx:
                idx = i; found = True; break
        return found, idx, self.min_heap[idx]

    def changep(self, vt):
        
        found, idx, _ = self.find(vt.vtx)
        
        while idx > 0 and found:
            par_idx = self.get_parent(idx)
            if self.min_heap[idx] < self.min_heap[par_idx]:
                self.swap(idx, par_idx)
            else:
                break
            
# pq-test-cases
# pq = priorityQue()
# pq.push(node(4, 3, 3))
# pq.push(node(3, 2, 1))
# pq.push(node(0, 0, 0))
# pq.push(node(1, 1, 0))
# pq.push(node(2, 2, 1))
# pq.push(node(5, 4, 4))
# pq.changep(node(5, 3, 1))

# while pq.isEmpty():
#     print(pq.pop().vtx)




class Graph:

    def __init__(self, v):
        self.v = v
        self.graph = [[] for i in range(v)]
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, strt_vtx):
        q = deque()
        visited = [False]*self.v
        q.append(strt_vtx)
        visited[strt_vtx] = True
        while q:
            vtx = q.popleft()
            print(vtx, end = ', ')
            
            for adj_vtx in self.graph[vtx]:
                if not visited[adj_vtx]:
                    q.append(adj_vtx)
                    visited[adj_vtx] = True
    
    def dfs(self, strt_vtx):

        stk = []
        visited = [False]*self.v
        stk.append((strt_vtx, 0))
        visited[strt_vtx] = True
        result=[strt_vtx]
        
        while stk:

            vtx, nof_adj_visit = stk[-1]
            adj_vts = self.graph[vtx]

            while nof_adj_visit < len(adj_vts) and visited[adj_vts[nof_adj_visit]]:
                nof_adj_visit += 1
            
            if nof_adj_visit >= len(adj_vts) :
                stk.pop()
            else:
                stk[-1] = (vtx, nof_adj_visit)
                stk.append((adj_vts[nof_adj_visit], 0))
                visited[adj_vts[nof_adj_visit]] = True
                result.append(adj_vts[nof_adj_visit])
        
        print(', '.join(map(str, result)))

    def undi_eq_wt_ssp(self, s):
        q = deque()
        visited = [False]*self.v
        dist = [-1]*self.v
        q.append(s)
        dist[s] = 0; visited[s] = True

        while q:

            vtx = q.popleft()

            for adj_vtx in self.graph[vtx]:

                if not visited[adj_vtx]:
                    dist[adj_vtx] = dist[vtx] + 1
                    visited[adj_vtx] = True
                    q.append(adj_vtx)
                    
        print(dist)

    
class WtUndiGraph:

    def __init__(self, v):
        self.v = v
        self.graph = [[] for i in range(v)]
    
    def addEdge(self, u, v, wt):
        # u, v, wt = e
        self.graph[u].append((v, wt))
        self.graph[v].append((u, wt))
    
    def undi_uneq_wt_ssp(self, s):
        
        # vtx_dist_parent_matrix = [[-1, i] for i in range(self.v)]
        # vtx_dist_parent_matrix[s] = [0, s]
        
        visited = [False]*self.v
        q = deque(); q.append(s)
        pq = priorityQue(); pq.push(node(s, 0, s))

        visited[s] = True

        while q:
            vtx = q.popleft(); print(vtx)
            _, __, vtx = pq.find(vtx) # vtx should exist in pq

            for adj_vtx in self.graph[vtx.vtx]:
                
                adj_vtx, wt = adj_vtx
                dist_of_vtx_frm_s = vtx.dist+wt

                
                found, _, adj_vtx = pq.find(adj_vtx)

                if not found:
                    pq.push(node(adj_vtx.vtx, dist_of_vtx_frm_s, vtx.vtx))
                elif dist_of_vtx_frm_s < adj_vtx.dist:
                    pq.changep(node(adj_vtx.vtx, dist_of_vtx_frm_s, vtx))
                    
                
                if not visited[adj_vtx.vtx]:
                    q.append(adj_vtx.vtx)
                    visited[adj_vtx.vtx] = True
                
        while pq.isEmpty():
            print(pq.pop())
        



if __name__ == '__main__':

    g = WtUndiGraph(9)
    g.addEdge(0, 1, 1)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 4, 3)
    g.addEdge(2, 3, 2)
    g.addEdge(2, 5, 3)
    g.addEdge(3, 6, 2)
    g.addEdge(4, 5, 0)
    g.addEdge(5, 6, 1)
    g.addEdge(5, 7, 2)
    g.addEdge(6, 8, 1)
    print(g.graph)
    # g.dfs(0)
    # g.bfs(0)
    g.undi_uneq_wt_ssp(0)
