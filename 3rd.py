import numpy as np

tree = np.zeros(5)
notree = np.zeros(5)
i = 0
steps = np.array([1,3,5,7,1])

for j in range (steps.size):
    file = open('3-input.txt', 'r')
    while True:
        line = file.readline()
        if (j == 4):
            line = file.readline()
        if not line:
            break
        if (line[i] == "#"):
            tree[j] += 1
        elif (line[i] == "."):
            notree[j] += 1
        else:
            print("error")
        i = (i+steps[j]) % (len(line)-1)
    i = 0
    file.close()

print ("Number of threes:", tree)
print("No threes: ", notree)

print(np.prod(tree))
