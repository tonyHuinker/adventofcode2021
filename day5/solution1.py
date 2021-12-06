from parse import *
import numpy as np
f = open("input.txt", "r")

lines = f.readlines()

#first, find max number
oBig = 0
for line in lines:
    result = parse("{},{} -> {},{}\n", line)
    result = list(map(int, result))
    cBig = max(result[0], result[1], result[2], result[3])
    if(cBig > oBig):
        oBig = cBig

#create map
grid = np.zeros((oBig+1, oBig+1))

#now, lets draw the lines!
for line in lines:
    result = parse("{},{} -> {},{}\n", line)
    result = list(map(int, result))
    #only straight lines

    #vertical lines
    if(result[0] == result[2]):
        if(result[1] <= result[3]):
            for y in range(result[1], result[3]+1):
                grid[result[0], y] += 1
        else:
            for y in range(result[3], result[1]+1):
                grid[result[0], y] += 1
    #horizontal lines
    elif(result[1] == result[3]):
        if(result[0] <= result[2]):
            for x in range(result[0], result[2]+1):
                grid[x, result[1]] += 1
        else:
            for x in range(result[2], result[0]+1):
                grid[x, result[1]] += 1
    #diagnol lines
    elif(abs(result[0]- result[2]) == abs(result[1]- result[3])):
        print(result)
        #x1 lower than x2
        if(result[0] <= result[2]):
            xstep = 1
        else:
            xstep = -1
        if(result[1] <= result[3]):
            ystep = 1
        else:
            ystep = -1
        for x,y in zip(range(result[0], result[2] + xstep, xstep),range(result[1], result[3] + ystep, ystep)):
            #print(xstep, ystep)
            #print(x,y)
            grid[x,y] += 1
            #temp = input("hold")
        

            
    
occurances = grid > 1
total = occurances.sum()
print(total)


