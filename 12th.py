import numpy as np

file = open('12-input.txt', 'r')

compass = ["N", "E", "S", "W"]
dir = 1
pos = np.array([0.,0.])

while True:
    line = file.readline()
    if not line:
        break
    action = line[0]
    nr = int(line[1:])
#    print (line, action, nr)
    if action == "F":
        action = compass[int(dir)]     # Part 1
        #print ("F: ", dir)
    if action == "L":
        dir = (dir - nr/90) % 4
        #print ("L: ", dir)
    elif action == "R":
        dir = (dir + nr/90) % 4
        #print ("R: ",dir)
    elif action == "N":
        pos[0] += nr
        #print ("N", pos)
    elif action == "S":
        pos[0] -= nr
        #print ("S", pos)
    elif action == "E":
        pos[1] += nr
        #print ("E", pos)
    elif action == "W":
        pos[1] -= nr
        #print ("W", pos)
file.close()

print("Part 1")
print("final diraction: ", compass[int(dir)])
print("final position: ")
if pos[0] < 0:
    print (abs(pos[0]), " units south")
elif pos[0] > 0:
    print (pos[0], " units north")
if pos[1] < 0:
    print (abs(pos[1]), " units west")
elif pos[1] > 0:
    print (pos[1], " units east")

print("manhatten position: ", abs(pos[0]) + abs(pos[1]))

# Part 2

file = open('12-input.txt', 'r')

pos = np.array([0.,0.])
waypoint = np.array([1.,10.])
rotL = np.array([[0.,1.],[-1.,0.]])
rotR = np.array([[0.,-1.], [1.,0.]])

while True:
    line = file.readline()
    if not line:
        break
    action = line[0]
    nr = int(line[1:])
#    print (line, action, nr)
    if action == "F":
        pos += waypoint * nr    # Part 2
        #print (line, pos)
    elif action == "L":
        if nr == 90:
            waypoint = np.dot(rotL, waypoint)
        elif nr == 180:
            waypoint = np.dot(np.dot(rotL,rotL), waypoint)
        elif nr == 270:
            waypoint = np.dot(np.dot(np.dot(rotL,rotL),rotL), waypoint)
        #print (line, waypoint)
    elif action == "R":
        if nr == 90:
            waypoint = np.dot(rotR, waypoint)
        elif nr == 180:
            waypoint = np.dot(np.dot(rotR,rotR), waypoint)
        elif nr == 270:
            waypoint = np.dot(np.dot(np.dot(rotR,rotR),rotR), waypoint)
        #print (line, waypoint)
    elif action == "N":
        waypoint[0] += nr
        #print (line, waypoint)
    elif action == "S":
        waypoint[0] -= nr
        #print (line, waypoint)
    elif action == "E":
        waypoint[1] += nr
        #print (line, waypoint)
    elif action == "W":
        waypoint[1] -= nr
        #print (line, waypoint)
file.close()

print ("part 2")
print("final position: ")
if pos[0] < 0:
    print (abs(pos[0]), " units south")
elif pos[0] > 0:
    print (pos[0], " units north")
if pos[1] < 0:
    print (abs(pos[1]), " units west")
elif pos[1] > 0:
    print (pos[1], " units east")

print("manhatten position: ", abs(pos[0]) + abs(pos[1]))
