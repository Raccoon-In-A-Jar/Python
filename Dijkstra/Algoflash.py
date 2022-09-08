infinity = float("inf")

G = "graph"
V = [] #vertex list
E = [] #edge list

L = [] #list of distances from one vertex to one another
P = [] #list of predecessors of each vertex in a shortest path with an s origin

M = [] #list of processed vertices

def initialize(V, E, L, P, s):
    L[s] = 0
    P[s] = s
