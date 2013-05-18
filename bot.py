'''
    Read in saved probabilities for different card strengths
    and save it to lists for access later
'''

line = "."

valuesPocket = []
probPocket = []
valuesFlop = []
probFlop = []
valuesTurn = []
probTurn = []
valuesRiver = []
probRiver = []

f = open("results/pocket.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue
    line = line[:(len(line)-1)]
    parts = line.split(":")
    valuesPocket.append(float(parts[0]))
    probPocket.append(float(parts[1]))
f.close()
line = "."
f = open("results/flop.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue    
    line = line[:(len(line)-1)]
    parts = line.split(":")
    valuesFlop.append(float(parts[0]))
    probFlop.append(float(parts[1]))
f.close()
line = "."
f = open("results/turn.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue    
    line = line[:(len(line)-1)]
    parts = line.split(":")
    valuesTurn.append(float(parts[0]))
    probTurn.append(float(parts[1]))
f.close()
line = "."
f = open("results/river.txt","r")
while line != "":
    line = f.readline()
    if line == "":
        continue    
    line = line[:(len(line)-1)]
    parts = line.split(":")
    valuesRiver.append(float(parts[0]))
    probRiver.append(float(parts[1]))
f.close()

'''
returns:
    -1 - fold on other person betting
    0 - prefer check, but might bet/fold otherwise (not really used)
    1 - call opponent
    2 - bet opponent
'''
def chooseAction(strength,part):
    action = 0
    if part == 0:
        if strength not in valuesPocket:
            return -1
        i = valuesPocket.index(strength)
        if probPocket[i] < .3:
            action = -1
        elif probPocket[i] < .6:
            action =  1
        elif probPocket[i] >= .6:
            action = 2
    elif part == 1:
        if strength not in valuesFlop:
            return -1        
        i = valuesFlop.index(strength)
        if probFlop[i] < .3:
            action = -1
        elif probFlop[i] < .6:
            action =  1
        elif probFlop[i] >= .6:
            action = 2        
    elif part == 2:
        if strength not in valuesTurn:
            return -1               
        i = valuesTurn.index(strength)
        if probTurn[i] < .3:
            action = -1
        elif probTurn[i] < .6:
            action =  1
        elif probTurn[i] >= .6:
            action = 2        
    elif part == 3:
        if strength not in valuesRiver:
            return -1           
        i = valuesRiver.index(strength)
        if probRiver[i] < .3:
            action = -1
        elif probRiver[i] < .6:
            action =  1
        elif probRiver[i] >= .6:
            action = 2
    return action
