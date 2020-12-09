import numpy as np

input = np.loadtxt("9-input.txt")
n = input.size

for i in range (25, n):
    found = False
#    print("i:", i)
    for j in range (i-25,i-1):
#        print("j:", j)
        for k in range (j+1, i):
#            print("k", k)
            r = input[j]+input[k]
            if (input[i]==r):
                found = True
    if (found == False):
        print("First illegal number: ", i, input[i])
        number = input[i]

i = 0
list = False
while (list == False and i <n+1):
    k = i
    sum = 0.
    while (sum < number):
        sum += input[k]
        if sum == number:
            #print (i, k)
            list = True
            contiguous = input[i:k+1]
            #print(input[i], input[k])
        k +=1
    i +=1

#print(contiguous)
#print(np.max(contiguous))
#print(np.min(contiguous))

print("Sum of smallest and largest number: ", np.min(contiguous)+ np.max(contiguous) )
