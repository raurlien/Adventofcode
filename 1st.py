import numpy as np

input = np.loadtxt("1-input.txt")
n = input.size
print("1st problem solution:")
for i in range(n):
    for j in range (i+1,n):
        a = input[i]+input[j]
        if (a == 2020):
            print("input: ", input[i], input[j])
            print("sum: ", input[i]+input[j])
            print("multiplyed: ", input[i]*input[j])

print("2nd problem solution:")
for i in range(n):
    for j in range (i+1,n):
        for k in range (j+1, n):
            b = input[i]+input[j]+input[k]
            if (b == 2020):
                print("input: ", input[i], input[j], input[k])
                print("sum: ", input[i]+input[j]+input[k])
                print("multiplyed: ", input[i]*input[j]*input[k])
