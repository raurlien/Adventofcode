import numpy as np
import string

letters = string.ascii_lowercase
file = open('6-input.txt', 'r')

answer = np.zeros(len(letters))
sum = 0
while True:
    line = file.readline()
    if not line:
        break
    if line in ['\n', '\r\n']:
        sum += answer.sum()
        answer = np.zeros(len(letters))
    else:
        for i in range(len(line)):
            for k in range(len(letters)):
                if letters[k] == line[i]:
                    answer[k] = 1
sum += answer.sum()
print ("Part 1:", sum)
file.close()

##part2
file = open('6-input.txt', 'r')
answer = np.ones(len(letters))
check = np.zeros(len(letters))
sum = 0
while True:
    line = file.readline()
    if not line:
        break
    if line not in ['\n', '\r\n']:
        for i in range(len(line)):
            for k in range(len(letters)):
                if letters[k] == line[i]:
                    check[k] = 1
        for i in range(len(letters)):
            answer[i] = answer[i] * check[i]
        print("check", check)
        check = np.zeros(len(letters))
    else:
        sum += answer.sum()
        print("answer", answer)
        answer = np.ones(len(letters))
sum += answer.sum()
print ("Part 2:", sum)
file.close()


#

#
