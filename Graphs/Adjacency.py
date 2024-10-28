class Graph:
    def __init__(self,num_nodes) -> None:
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(self.num_nodes)]
        pass
    
    def add_edge(self,src,dest):
        self.data[src].append(dest)
        self.data[dest].append(src)
    
    def remove_edge(self,src,dest):
        self.data[src].remove(dest)
        self.data[dest].remove(src)
        pass

    def dfs_rec(self,visit,s):
        visit[s]=True
        print(s,end=" ")

        for i in self.data[s]:
            if not visit[i]:
                self.dfs_rec(visit,i)

    def DFS(self):
        visit=[False for _ in range(self.num_nodes)]

        for i in range(self.num_nodes):
            if not visit[i]:
                self.dfs_rec(visit,i)
        print()


    def BFS(self,s):
        visited=[False for _ in range(self.num_nodes)]

        queue=[]
        
        queue.append(s)
        visited[s]=True

        while queue:
            d=queue.pop(0)
            print(d,end=" ")

            for i in self.data[d]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
        print()
            
    
    def printData(self):
        return "\n".join([ "{}:{}".format(i,neighbours) for i,neighbours in enumerate(self.data)])

graph=Graph(4)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(0,3)
graph.add_edge(2,3)
graph.add_edge(1,3)
# print(graph.printData())
# graph.remove_edge(1,2)
graph.BFS(0)
graph.DFS()
print(graph.printData())