import itertools
import collections

def printSolution(dist):
    print "Following matrix shows the shortest distances between every pair of vertices" 
    for i in range(len(dist)):
        for j in range(len(dist)):
            if(dist[i][j] == INF):
                print "%7s" %("INF"),
            else:
                print "%7d\t" %(dist[i][j]),
            if j == len(dist)-1:
                print ""

INF = 1000000

squares = {
  0: 'b7',
  1: 'd7',
  2: 'e7',
  3: 'f7',
  4: 'h7',
  5: 'i7',
  6: 'k7',
  7: 'a6',
  8: 'b6',
  9: 'd6',
  10: 'e6',
  11: 'h6',
  12: 'i6',
  13: 'k6',
  14: 'a5',
  15: 'b5',
  16: 'd5',
  17: 'f5',
  18: 'h5',
  19: 'j5',
  20: 'k5',
  21: 'b4',
  22: 'c4',
  23: 'f4',
  24: 'i4',
  25: 'j4',
  26: 'c3',
  27: 'd3',
  28: 'f3',
  29: 'h3',
  30: 'k3',
  31: 'a2',
  32: 'd2',
  33: 'e2',
  34: 'g2',
  35: 'h2',
  36: 'i2',
  37: 'k2',
  38: 'b1',
  39: 'c1',
  40: 'd1',
  41: 'e1',
  42: 'f1',
  43: 'g1',
  44: 'h1',
  45: 'k1'
}

square_map = {v:k for k,v in squares.items()}

knights = [0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 40, 41, 42, 43]

edges = [
    ('b7', 'a5'),
    ('b7', 'd6'),
    ('d7', 'b6'),
    ('e7', 'd5'),
    ('e7', 'f5'),
    ('e7', 'h7'),
    ('f7', 'd6'),
    ('f7', 'h6'),
    ('i7', 'h7'),
    ('i7', 'h5'),
    ('i7', 'j5'),
    ('i7', 'k6'),
    ('k7', 'i6'),
    ('k7', 'j5'),
    ('a6', 'b4'),
    ('a6', 'd7'),
    ('b6', 'c4'),
    ('b6', 'd5'),
    ('b6', 'd7'),
    ('d6', 'b7'),
    ('d6', 'b5'),
    ('d6', 'c4'),
    ('d6', 'f5'),
    ('d6', 'f7'),
    ('e6', 'd7'),
    ('e6', 'f4'),
    ('e6', 'h7'),
    ('h6', 'f7'),
    ('h6', 'f5'),
    ('h6', 'i4'),
    ('h6', 'j5'),
    ('i6', 'h7'),
    ('i6', 'j4'),
    ('i6', 'k5'),
    ('i6', 'k7'),
    ('k6', 'i7'),
    ('k6', 'j4'),
    ('a5', 'c4'),
    ('b5', 'c3'),
    ('b5', 'd6'),
    ('d5', 'b6'),
    ('d5', 'b4'),
    ('d5', 'c3'),
    ('d5', 'd7'),
    ('d5', 'e7'),
    ('d5', 'f4'),
    ('f5', 'd6'),
    ('f5', 'e7'),
    ('f5', 'h7'),
    ('f5', 'h6'),
    ('h5', 'f4'),
    ('h5', 'h7'),
    ('h5', 'i7'),
    ('h5', 'j4'),
    ('j5', 'h6'),
    ('j5', 'i7'),
    ('j5', 'k7'),
    ('j5', 'k3'),
    ('k5', 'i6'),
    ('k5', 'i4'),
    ('b4', 'a6'),
    ('b4', 'a2'),
    ('b4', 'c1'),
    ('b4', 'd5'),
    ('b4', 'd3'),
    ('c4', 'a5'),
    ('c4', 'b6'),
    ('c4', 'b1'),
    ('c4', 'd6'),
    ('c4', 'd2'),
    ('f4', 'd5'),
    ('f4', 'd3'),
    ('f4', 'e6'),
    ('f4', 'e2'),
    ('f4', 'h7'),
    ('f4', 'g2'),
    ('f4', 'h5'),
    ('f4', 'h3'),
    ('i4', 'h6'),
    ('i4', 'h2'),
    ('i4', 'k5'),
    ('i4', 'k3'),
    ('j4', 'h5'),
    ('j4', 'h3'),
    ('j4', 'i6'),
    ('j4', 'i2'),
    ('j4', 'k6'),
    ('j4', 'k2'),
    ('c3', 'a2'),
    ('c3', 'b5'),
    ('c3', 'b1'),
    ('c3', 'd5'),
    ('c3', 'd1'),
    ('c3', 'e2'),
    ('d3', 'b4'),
    ('d3', 'b1'),
    ('d3', 'c1'),
    ('d3', 'e1'),
    ('d3', 'f4'),
    ('f3', 'd2'),
    ('f3', 'e1'),
    ('f3', 'g1'),
    ('f3', 'h2'),
    ('h3', 'f4'),
    ('h3', 'g1'),
    ('h3', 'j4'),
    ('k3', 'i4'),
    ('k3', 'i2'),
    ('k3', 'j5'),
    ('k3', 'k1'),
    ('a2', 'b4'),
    ('a2', 'c3'),
    ('a2', 'c1'),
    ('d2', 'b1'),
    ('d2', 'c4'),
    ('d2', 'f3'),
    ('d2', 'f1'),
    ('e2', 'c3'),
    ('e2', 'c1'),
    ('e2', 'f4'),
    ('e2', 'g1'),
    ('g2', 'e1'),
    ('g2', 'f4'),
    ('h2', 'f3'),
    ('h2', 'f1'),
    ('h2', 'i4'),
    ('h2', 'k1'),
    ('i2', 'g1'),
    ('i2', 'j4'),
    ('i2', 'k3'),
    ('i2', 'k1'),
    ('k2', 'j4'),
    ('b1', 'c3'),
    ('b1', 'd2'),
    ('c1', 'a2'),
    ('c1', 'd3'),
    ('c1', 'e2'),
    ('d1', 'b1'),
    ('d1', 'c3'),
    ('e1', 'c1'),
    ('e1', 'd3'),
    ('e1', 'f3'),
    ('e1', 'g2'),
    ('f1', 'd2'),
    ('f1', 'h2'),
    ('g1', 'e2'),
    ('g1', 'f3'),
    ('g1', 'h3'),
    ('g1', 'i2'),
    ('k1', 'i2')
]

# parse edges to numbers
edges = [(square_map[x[0]], square_map[x[1]]) for x in edges]
vert_count = len(squares.keys())

# define graph

fw_distances = [[INF for x in range(vert_count)] for y in range(vert_count)]
for i, j in edges:
    fw_distances[i][j] = 1

for i in squares:
    fw_distances[i][i] = 0

for k in range(vert_count):
    for i in range(vert_count):
        for j in range(vert_count):
            fw_distances[i][j] = min(fw_distances[i][j], fw_distances[i][k] + fw_distances[k][j])

parent = dict()
rank = dict()

subgraph_edges = []

for i in knights:
    for j in knights:
        if fw_distances[i][j] == 1:
            subgraph_edges.append((i, j, fw_distances[i][j]))

def dfs(graph, start):
    visited, stack = set(), [start]
    ordered_visit = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            ordered_visit.append(vertex)
            neighbours = set([x[1] for x in graph if x[0] == vertex])
            stack.extend(neighbours - visited)
    return ordered_visit

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        neighbours = set([x[1] for x in graph if x[0] == vertex])
        for next in neighbours - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, root): 
    visited, queue = set(), collections.deque([root])
    ordered_visit = []

    visited.add(root)
    ordered_visit.append(root)

    while queue: 
        vertex = queue.popleft()
        neighbours = set([x[1] for x in graph if x[0] == vertex])
        for neighbour in neighbours: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                ordered_visit.append(neighbour)
                queue.append(neighbour)

    return ordered_visit

START_NODE = 23

for knight in knights:
    longest_path = 0
    print "generating all paths from f4 to {}...".format(squares[knight])
    for path in dfs_paths(edges, START_NODE, knight):
        if len(path) >= longest_path:
            longest_path = len(path)
            print "found path of size {}".format(longest_path)
            missing_knights = [x for x in knights if x not in path]
            if len(missing_knights) == 0:
                print "viable path!"
                print [squares[x] for x in path]
            else:
                print "missing knights {}".format([squares[x] for x in missing_knights])

'''
def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
	else:
	    parent[root1] = root2
	if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
	    make_set(vertice)
	    minimum_spanning_tree = set()
    m_edges = list(graph['edges'])
    m_edges.sort(key= lambda x: x[2])
	    #print edges
    for edge in m_edges:
	    vertice1, vertice2, weight = edge

	    if find(vertice1) != find(vertice2):
	        union(vertice1, vertice2)
	        minimum_spanning_tree.add(edge)
	    
    return sorted(minimum_spanning_tree)

graph = {'vertices': knights, 'edges': subgraph_edges}

solution = kruskal(graph)

print len(solution)

for step in solution:
    print (squares[step[0]], squares[step[1]])
'''






