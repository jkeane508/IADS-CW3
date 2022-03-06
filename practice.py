import math
import random

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)

coords = open("/Users/jameskeane/Desktop/IADS Sem 2/Courswork 3/IADS_cwk3/cities50").readlines()
coords = [x.replace ('\n' , '').strip().split('  ') for x in coords]
coords = [map(int, x) for x in coords]
coords.insert(0, [0,0])


scores = []
for i in coords:
    n = []
    for j in coords:
        n.append([euclid(i,j)])
    scores.append(n)


perm = [random.randrange(1, 50, 1) for i in range(50)]


def tourValue(perm, scores):
    cost = 0.0

    for x in perm:
        if x == perm[-1]:
            y = perm[0]
        else:
            y = perm[((perm.index(x))+1)]
        dist_x_y = scores[x][y]
        cost = cost + sum(dist_x_y)

    return cost

def tryswap(scores, perm, i):
    cost_original = tourValue(perm, scores)
    
    swapped_perm = perm
    if i == perm[-1]:
        swapped_perm[i], swapped_perm[0] = swapped_perm[0], swapped_perm[i]
    else:
        swapped_perm[i], swapped_perm[i+1] = swapped_perm[i+1], swapped_perm[i]
    
    cost_swapped = tourValue(swapped_perm, scores)
    
    if cost_swapped < cost_original:
        return True
    else:
        return False
    
def reverseSwap(scores, perm, i, j):
    cost_original = tourValue(perm, scores)
    
    reverse_perm = perm
    reverse_perm[i:j+1] = reverse_perm[i:j+1 ][::-1]
    cost_reversed = tourValue(reverse_perm, scores)
    
    if cost_reversed < cost_original:
            return True
    else:
        return False
    
edges = open("/Users/jameskeane/Desktop/IADS Sem 2/Courswork 3/IADS_cwk3/twelvenodes").readlines()
edges = [ x.replace('\n' , '').strip().replace(' ', ',').split(',') for x in edges]
edges = [map(int, x) for x in edges]
print(edges)
print (edges[1])


edge_scores =  [[[]for _ in range(12)] for _ in range(12)]
print(edge_scores)

for i in edges:
    x = i[0]
    y = i[1]
    edge_scores[x][y] = i[2]
    
print([min(x) for x in scores])
