import math

binset = []
subset = []
powset = []
n = int(input())
aset = [int(input())for i in range(n)]
a = math.pow(2,n)

for i in range(int(a)):
    b = bin(i)[2:]
    b = str(0) * (n-len(b)) + b
    binset = b
    subset = []
    for j in range(n):
        if(int(binset[j]) == 1):
            subset.append(aset[j])
    powset.append(subset)
print(powset)
