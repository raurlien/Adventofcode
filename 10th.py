import numpy as np

input = np.loadtxt("10-input.txt")
n = input.size

input.sort()
ones = 0
twos = 0
threes = 0
jolt = 0
diff = np.empty(n)

for i in range(n):
    if (input[i]-jolt == 1):
        ones+=1
        diff[i]=1
    elif (input[i]-jolt == 2):
        twos+=1
        diff[i]=2
    elif (input[i]-jolt == 3):
        threes+=1
        diff[i]=3
    else:
        print("error")
    jolt = input[i]
print(input)
print(diff)
print("ones: ", ones)
print("twos: ", twos)
print("threes: ", threes)

print ("check:", n - ones - twos - threes)

print ("threees times ones: ", (threes+1)*ones)

arr = 0.
i = 0
j = 0
number = 1
while (j < n):
    while (i<n and diff[i]==1):
        arr += 1
        i   += 1
    if (arr == 0.):
        print("0")
    elif (arr == 1):
        print("1")
    elif (arr == 2):
        print("2")
        number *= 2
    elif (arr == 3):
        print("3")
        number *= 4
    elif (arr == 4):
        print("4")
        number *= 7
    else:
        print(arr)
    i += 1
    arr = 0
    j = i

print ("number of combinations:", number)
