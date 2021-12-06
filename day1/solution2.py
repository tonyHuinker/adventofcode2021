f = open("input.txt", "r")

lines = f.readlines()

count = 0
numLines = len(lines)
print(numLines)
for x in range(0, numLines-3):
    sum2 = int(lines[x+1]) + int(lines[x+2]) + int(lines[x+3])
    sum1 = int(lines[x+0]) + int(lines[x+1]) + int(lines[x+2])
    print("Comparing %d to %d" % (sum2, sum1))
    if(sum2 > sum1):
        count += 1
        print("increasing!")
    #z = input("hold")

print(count)


