from collections import defaultdict
class Graph:

    def __init__(self,vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.ans = list()

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self,src,target,maxDepth,l):

        if src == target :
          #  print(self.ans)
            return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1,l)):
                    l.append(i)
                    return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self,src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            l = []
            if (self.DLS(src, target, i,l)):
                l.append(src)
                l.reverse()
                return l
        return l

# Create a graph given in the above diagram
n,e = map(int ,input("Enter no.of vertices and edges").split())
g = Graph (n);
for i in range(e):
    a,b = map(int , input().split())
    g.addEdge(a,b)

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 5)
# g.addEdge(2, 6)

target = int(input("Enter the target vertex"))
maxDepth = int(input("Enter the max depth"))
src = 0
l = g.IDDFS(src, target, maxDepth)
if len(l)!=0:
    print(l)
    print ("Target is reachable from source " +
        "within max depth")
else :
    print ("Target is NOT reachable from source " +
        "within max depth")
