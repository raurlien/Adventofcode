import numpy as np

file = open('2-input.txt', 'r')
valid = 0
valid2 = 0
while True:
    line = file.readline()
#    print(line)
    if not line:
        break
    h = 2
    low = line[0]
    if (line[1] != "-"):
        low += line[1]
        h = 3
    low = int(low)
    c = h + 2
    high = line[h]
    if (line[h+1] != " "):
        high += line[h+1]
        c += 1
    high = int(high)
    char = line[c]
    string = line[c+3:]
    #print(low, high, char, string)

    n = 0
    for i in range(len(string)):
        if (string[i] == char):
            n += 1
    if (n>=low and n<=high):
        valid +=1
        #print(low, high, char, string)

    if (string[low-1] == char or string[high-1] == char):
        if (string[low-1] == char and string[high-1] == char) == False:
            print(low, high, char, string)
            valid2 +=1




print("Number of valid passwords for part 1: ", valid)

print("Number of valid passwords for part 2: ", valid2)
