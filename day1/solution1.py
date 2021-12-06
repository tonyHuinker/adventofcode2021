f = open("input.txt", "r")

lines = f.readlines()

count = 0
numLines = len(lines)
print(numLines)
for x in range(0, numLines-6, 3):
    sum2 = lines[x+3] + lines[x+4] + lines[x+5]
    sum1 = lines[x+0] + lines[x+1] + lines[x+2]
    num2 = int(lines[x+1])
    num1 = int(lines[x])
    print("Comparing %d to %d" % (num2, num1))
    if(num2 > num1):
        count += 1

print(count)


