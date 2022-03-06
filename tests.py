import math
import graph
import copy
import time
import numpy

#------------------------------------------------------------ sixnodes------------------------------------------------------------------------
print('\n\n\n--six nodes--')

#------------ Default ----------------------------

n = 0
results = 0
timestaken = []
while n != 100:
    g=graph.Graph(6,"sixnodes")
    start_time = time.time()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('default = ', results)
print('time taken = ', avgTimeTaken)

#------------ Swap -------------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(6,"sixnodes")
    start_time = time.time()
    g.swapHeuristic(-1)
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('swap = ', results)
print('time taken = ', avgTimeTaken)

#------------ two opt  -----------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(6,"sixnodes")
    start_time = time.time()
    g.swapHeuristic(-1)
    g.TwoOptHeuristic(-1)
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('2 opt = ', results)
print('time taken = ', avgTimeTaken)

#------------ Greedy -------------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(6,"sixnodes")
    start_time = time.time()
    g.Greedy()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('greedy = ', results)
print('time taken = ', avgTimeTaken)


#------------ Cheapest Insertion -------------------
n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(6,"sixnodes")
    start_time = time.time()
    g.cheapestInsertion()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('cheapest = ', results)
print('time taken = ', avgTimeTaken)


#------------------------------------------------------------ twelve nodes ------------------------------------------------------------------------

print('\n\n\n--twelve nodes--')

#------------ Default ----------------------------

n = 0
results = 0
timestaken = []
while n != 100:
    g=graph.Graph(12, "twelvenodes")
    start_time = time.time()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('default = ', results)
print('time taken = ', avgTimeTaken)

#------------ Swap -------------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(12, "twelvenodes")
    start_time = time.time()
    g.swapHeuristic(-1)
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('swap = ', results)
print('time taken = ', avgTimeTaken)

#------------ two opt  -----------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(12, "twelvenodes")
    start_time = time.time()
    g.swapHeuristic(-1)
    g.TwoOptHeuristic(-1)
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('2 opt = ', results)
print('time taken = ', avgTimeTaken)

#------------ Greedy -------------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(12, "twelvenodes")
    start_time = time.time()
    g.Greedy()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('greedy = ', results)
print('time taken = ', avgTimeTaken)


#------------ Cheapest Insertion -------------------
n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(12, "twelvenodes")
    start_time = time.time()
    g.cheapestInsertion()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('cheapest = ', results)
print('time taken = ', avgTimeTaken)

#------------------------------------------------------------ cities 50 ------------------------------------------------------------------------

print('\n\n\n--cities 50--')

#------------ Default ----------------------------

n = 0
results = 0
timestaken = []
while n != 100:
    g=graph.Graph(-1,"cities50")
    start_time = time.time()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('default = ', results)
print('time taken = ', avgTimeTaken)

#------------ Swap -------------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(-1,"cities50")
    start_time = time.time()
    g.swapHeuristic(-1)
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('swap = ', results)
print('time taken = ', avgTimeTaken)

#------------ two opt  -----------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(-1,"cities50")
    start_time = time.time()
    g.swapHeuristic(-1)
    g.TwoOptHeuristic(-1)
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('2 opt = ', results)
print('time taken = ', avgTimeTaken)

#------------ Greedy -------------------------------

n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(-1,"cities50")
    start_time = time.time()
    g.Greedy()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('greedy = ', results)
print('time taken = ', avgTimeTaken)


#------------ Cheapest Insertion -------------------
n = 0
results = 0
timestaken = []

while n != 100:
    g=graph.Graph(-1,"cities50")
    start_time = time.time()
    g.cheapestInsertion()
    timetaken = (time.time() - start_time)
    timestaken.append(timetaken)
    results += g.tourValue()
    n += 1

results = results/100
avgTimeTaken = numpy.mean(timestaken)
print('cheapest = ', results)
print('time taken = ', avgTimeTaken)