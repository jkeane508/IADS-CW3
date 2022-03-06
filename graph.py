import math
import random
import copy

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self, n, filename):
        
        if n == -1: #specific for euclidean distance files
            self.n = len(open(filename).readlines())
            
            coords = open(filename).readlines()
            coords = [x.replace('\n' , '').strip().split('  ') for x in coords]
            coords = [map(int, x) for x in coords]
            coords.insert(0, [0,0])
        
            scores = []
        
            for i in coords:
                n = []
                for j in coords:
                    n.append([euclid(i,j)])
                scores.append(n)
                
                self.dists = scores
        else: #for general case files
            self.n = n
            
            edges = open(filename).readlines()
            edges = [ x.replace('\n' , '').strip().replace(' ', ',').split(',') for x in edges]
            edges = [map(int, x) for x in edges]


            edge_scores =  [[[]for _ in range(n)] for _ in range(n)]

            for i in edges:
                edge_scores[i[0]][i[1]] = i[2]
                
            self.dists = edge_scores
            
                
        self.perm = list(range(0,(self.n)))


    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        cost = 0.0

        for x in self.perm:
            if x == self.perm[-1]: #allows wraparound back to starting node
                y = self.perm[0]
            else:
                y = self.perm[((self.perm.index(x))+1)]
            dist_x_y = self.dists[x][y]
            
            if dist_x_y == []:
                try:
                    dist_x_y = self.dists[y][x] #if no distance try reverse 
                except:
                    pass
            
            if type(dist_x_y) == int:   #may return int or [int] depending on general or euclidean
                cost = cost + dist_x_y
            else:
                cost = cost + sum(dist_x_y)
                
        
        return cost
        

    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    def trySwap(self,i):
        cost_original = self.tourValue()
        perm = copy.copy(self.perm)
        swapped_perm = copy.copy(self.perm)
        
        if self.perm[i] == self.perm[-1]:
            swapped_perm[i], swapped_perm[0] = swapped_perm[0], swapped_perm[i]
        else:
            swapped_perm[i], swapped_perm[i+1] = swapped_perm[i+1], swapped_perm[i]
    
        self.perm = swapped_perm
        cost_swapped = self.tourValue()
        
        if cost_swapped < cost_original:
            self.perm = swapped_perm
            result = True
        else:
            self.perm = perm #reverts to original perm is the cost is not lower
            result = False
        
        return result
        

    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    def tryReverse(self,i,j):
        perm = copy.copy(self.perm)
        cost_original = self.tourValue()
        
        reverse_perm = copy.copy(self.perm)
        reverse_perm[i:j+1] = reverse_perm[i:j+1 ][::-1]
        self.perm = reverse_perm
        cost_reversed = self.tourValue()
        
        
        if cost_reversed < cost_original:
            self.perm = reverse_perm
            result =  True
        else:
            self.perm = perm
            result = False
        return result

    def swapHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self,k):
        better = True
        count = 0
        while better and (count < k or k == -1):
            better = False
            count += 1
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True

                        
    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    def Greedy(self):
        unused_nodes = copy.copy(self.perm)
        greedy_tour = []
        current_node = unused_nodes[0]
        greedy_tour.append(current_node)
        
        while True:
            distances = []
            unused_nodes.remove(current_node)
            
            for x in unused_nodes:
                distance = (self.dists[current_node][x], x)
                
                if distance[0] == [0.0]: #ignores 0 values (for euclidean version)
                    pass
                elif distance[0] == []: #if empty try reverse 
                        distance = (self.dists[x][current_node], x) #tuple (distance, node)
                        distances.append(distance)
                else:
                    distances.append(distance)
            
            if distances == []: #if list distances are empty no more nodes to traverse, break loop
                break
            
            minimum_score = min(distances)
            greedy_tour.append(minimum_score[1])
            current_node = minimum_score[1]
            
        self.perm = greedy_tour
        return greedy_tour
    
    
    #function that gets the node closest to current node
    #similar to code from Greedy algorithm
    # returns tuple (distance, node)
    def getNearestNode(self, currentNode, unusedNodes):
        
        distances = []
        for x in unusedNodes:
            distance = (self.dists[currentNode][x], x)
            
            if distance[0] == [0.0]:
                    pass
            elif distance[0] == []: 
                    distance = (self.dists[x][currentNode], x)
                    distances.append(distance)
            else:
                distances.append(distance)
                
        minimum_score = min(distances)
        nearestNode = minimum_score
        
        return nearestNode
    
    #takes subtour and node to be inserted
    #finds most optimal position for node in partial tour
    #uses tour cost as metric
    #returns int that is the best position for node    
    def findCheapestInsertion(self, partialTour, insertionNode):
        
        perm = copy.copy(self.perm)
        originalTour = copy.copy(partialTour) #need to keep tour the same after function call
        newTour = copy.copy(partialTour)
        tourCosts = []
           
        for x in range(len(newTour)+1): 
            newTour.insert(x, insertionNode)
            self.perm = newTour
            cost = (self.tourValue(), x)
            tourCosts.append(cost)
            self.perm = copy.copy(originalTour)
            newTour = copy.copy(originalTour)
        
        
        cheapestInsertionIndex = (min(tourCosts))[1]
        
        partialTour = copy.copy(originalTour)
        self.perm = copy.copy(perm)
        
        return int(cheapestInsertionIndex)
    
    #Chooses random node and closest node to random to begin
    #picks node nearest to any node in sub tour (partialTour)
    #inserts node in position that is the cheapest
    #repeats until all nodes are used in subTour
    #returns sub tour
    def cheapestInsertion(self):
        
        #initialisation - creates sub tour of 2 nodes, one random and the closest to random
        originalPerm = copy.copy(self.perm)
        unusedNodes = originalPerm
        
        startingNode = random.choice(unusedNodes)
        unusedNodes.remove(startingNode)
        partialTour = [startingNode]
        
        nextNode = (self.getNearestNode(startingNode, unusedNodes))[1]
        unusedNodes.remove(nextNode)
        partialTour.append(nextNode)
        
        
        while unusedNodes != []:
            
            #selection -> finds unused node that is nearest to any node in sub tour(partialTour)
            nearestNodes = [self.getNearestNode(x, unusedNodes) for x in partialTour]
            nearestNode = (min(nearestNodes))[1]
            
            #insertion -> finds cheapest place to insert unused node
            insertionNodeIndex = self.findCheapestInsertion(partialTour, nearestNode)
            
            partialTour.insert(insertionNodeIndex, nearestNode)
            unusedNodes.remove(nearestNode) #remove inserted node from unused nodes
            
            self.perm = originalPerm
        
        self.perm = partialTour
        
        return partialTour
        


        
            
            
        
            
        
        
        
        
        
        
