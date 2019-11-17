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
  0: 'a7',
  1: 'b7',
  2: 'c7',
  3: 'f7',
  4: 'h7',
  5: 'c6',
  6: 'd6',
  7: 'e6',
  8: 'f6',
  9: 'k6',
  10: 'k5',
  11: 'a4',
  12: 'c4',
  13: 'f4',
  14: 'i4',
  15: 'k4',
  16: 'a3',
  17: 'g3',
  18: 'i3',
  19: 'j3',
  20: 'a2',
  21: 'c2',
  22: 'f2',
  23: 'a1',
  24: 'd1',
  25: 'g1',
  26: 'j1',
  27: 'k1'
}

square_map = {v:k for k,v in squares.items()}

knights = ['a7', 'f6', 'c4', 'i4', 'f2', 'k1']

edges = [
    ('a7', 'c6', 1),
    ('b7', 'c6', 2),
    ('b7', 'd6', 1),
    ('c7', 'e6', 1),
    ('f7', 'd6', 1),
    ('f7', 'h7', 2),
    ('h7', 'f6', 1),
    ('c6', 'a7', 1),
    ('d6', 'b7', 1),
    ('d6', 'c4', 1),
    ('d6', 'f7', 1),
    ('e6', 'c7', 1),
    ('e6', 'c6', 2),
    ('e6', 'f4', 1),
    ('f6', 'd6', 2),
    ('f6', 'h7', 1),
    ('k6', 'k4', 2),
    ('k5', 'i4', 1),
    ('k5', 'j3', 1),
    ('a4', 'a2', 2),
    ('a4', 'c2', 2),
    ('a4', 'c6', 2),
    ('c4', 'a3', 1),
    ('c4', 'a2', 2),
    ('c4', 'c2', 4),
    ('c4', 'd6', 1),
    ('f4', 'g1', 4),
    ('f4', 'e6', 1),
    ('f4', 'c2', 3),
    ('i4', 'j3', 2),
    ('i4', 'g3', 1),
    ('i4', 'h7', 2),
    ('i4', 'k5', 1),
    ('k4', 'i3', 1),
    ('k4', 'j3', 2),
    ('a3', 'c2', 1),
    ('a3', 'c4', 1),
    ('g3', 'g1', 2),
    ('g3', 'i3', 2),
    ('g3', 'i4', 1),
    ('i3', 'g1', 2),
    ('i3', 'j1', 2),
    ('i3', 'k4', 1),
    ('j3', 'k1', 1),
    ('j3', 'k5', 1),
    ('a2', 'c2', 2),
    ('a2', 'd1', 2),
    ('c2', 'a3', 1),
    ('c2', 'a1', 1),
    ('c2', 'g1', 3),
    ('f2', 'c2', 3),
    ('f2', 'd1', 1),
    ('f2', 'g1', 2),
    ('a1', 'c2', 1),
    ('d1', 'f2', 1),
    ('d1', 'a2', 2),
    ('d1', 'c2', 2),
    ('g1', 'i3', 2),
    ('j1', 'i3', 1),
    ('k1', 'i3', 2),
    ('k1', 'j3', 1)
]

# parse edges to numbers
edges = [(square_map[x[0]], square_map[x[1]], x[2]) for x in edges]
vert_count = len(squares.keys())

# define graph

fw_distances = [[INF for x in range(vert_count)] for y in range(vert_count)]
for i, j, weight in edges:
    fw_distances[i][j] = weight

for i in squares:
    fw_distances[i][i] = 0

for k in range(vert_count):
    for i in range(vert_count):
        for j in range(vert_count):
            fw_distances[i][j] = min(fw_distances[i][j], fw_distances[i][k] + fw_distances[k][j])

shortest_path = None
shortest_weight = INF

START_NODE = 13
knights = [square_map[x] for x in knights]

for permutation in itertools.permutations(knights):
    weight = fw_distances[START_NODE][permutation[0]]
    for i in range (len(knights) -1):
        weight = weight + fw_distances[permutation[i]][permutation[i+1]]
    if weight < shortest_weight:
        shortest_path = permutation
        shortest_weight = weight
        print "current fastest solution is weight {}".format(shortest_weight)

print "done! this solution has a weight of {}".format(shortest_weight)
print [squares[x] for x in shortest_path]

