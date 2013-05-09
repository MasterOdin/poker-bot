'''
Created 5/6/2013

poker-bot:
    Create a working poker bot that initially only knows the rules of texas
    hold'em. It knows nothing of a strong hand or anything, but will learn
    through use of Monte Carlo encountered updates for reinforcement learning
    by playing against itself.
'''

import msvcrt
from game import Game

main = Game()

# because I don't think python allows me to search for a list within a list
# so seperate various parts of a state
statesPocket = []
probPocket = []
encounteredPocket = []
statesFlop = []
probFlop = []
encounteredFlop = []
statesTurn = []
probTurn = []
encounteredTurn = []
statesRiver = []
probRiver = []
encounteredRiver = []

# file inputs
p = open("results/pocket.txt","w")
f = open("results/flop.txt","w")
t = open("results/turn.txt","w")
r = open("results/river.txt","w")

winner = 0

'''
update probability
Takes in indexs, and updates the 'global' lists with new probabilities
@params:
    pocket (int) - index of pocket state
    flop (int) - index of flop state
    turn (int) - index of turn state
    river (int) - index of river state
'''
def update(pocket,flop,turn,river,player):
    if (player == 2):
        local = winner * -1
    else:
        local = winner

    #print(str(pocket) + " " + str(flop) + " " + str(turn) + " " + str(river))
    probPocket[pocket] = probPocket[pocket] + (local-probPocket[pocket])/(encounteredPocket[pocket]+1)
    probFlop[flop] = probFlop[flop] + (local-probFlop[flop])/(encounteredFlop[flop]+1)
    probTurn[turn] = probTurn[turn] + (local-probTurn[turn])/(encounteredTurn[turn]+1)
    probRiver[river] = probRiver[river] + (local-probRiver[river])/(encounteredRiver[river]+1)

def saveResults():
    print("Pocket data...")
    for i in range(0,len(statesPocket)):
        p.write(str(statesPocket[i]) + ":" + str(probPocket[i]) + ":" + str(encounteredPocket[i]) + "\n")
        #print(str(statesPocket[i]) + ": " + str(probPocket[i]) + " - " + str(encounteredPocket[i]))
    print("Flop data...")
    for i in range(0,len(statesFlop)):
        f.write(str(statesFlop[i]) + ":" + str(probFlop[i]) + ":" + str(encounteredFlop[i]) + "\n")
        #print(str(statesFlop[i]) + ": " + str(probFlop[i]) + " - " + str(encounteredFlop[i]))
    print("Turn data...")
    for i in range(0,len(statesTurn)):
        t.write(str(statesTurn[i]) + ":" + str(probTurn[i]) + ":" + str(encounteredTurn[i]) + "\n")
        #print(str(statesTurn[i]) + ": " + str(probTurn[i]) + " - " + str(encounteredTurn[i]))
    print("River data...")
    for i in range(0,len(statesRiver)):
        r.write(str(statesRiver[i]) + ":" + str(probRiver[i]) + ":" + str(encounteredRiver[i]) + "\n")
        #print(str(statesRiver[i]) + ": " + str(probRiver[i]) + " - " + str(encounteredRiver[i]))



'''
    need to put hand strength into a part of episode
    [
        hand strength
        community strength
    ]
    is it worth subtracing community from hand for one strength number?
    I have no idea, but we'll save states based off these two things for now
'''

count = 1
while count < 200001:
    print("Simulating Round " + str(count))
    winner = 0

    main.startRound()
    one = main.getHandStrength(1)
    two = main.getHandStrength(2)
    if one in statesPocket:
        pocketOneIndex = statesPocket.index(one)
        encounteredPocket[pocketOneIndex] += 1
    else:
        statesPocket.append(one)
        pocketOneIndex = (len(statesPocket)-1)
        probPocket.append(0)
        encounteredPocket.append(1)
    if two in statesPocket:
        pocketTwoIndex = statesPocket.index(two)
        encounteredPocket[pocketTwoIndex] += 1
    else:
        statesPocket.append(two)
        pocketTwoIndex = (len(statesPocket)-1)
        probPocket.append(0)
        encounteredPocket.append(1)
    #--------------------------------------------
    main.dealFlop()
    one = main.getHandStrength(1)
    two = main.getHandStrength(2)
    if one in statesFlop:
        flopOneIndex = statesFlop.index(one)
        encounteredFlop[flopOneIndex] += 1
    else:
        statesFlop.append(one)
        flopOneIndex = (len(statesFlop)-1)
        probFlop.append(0)
        encounteredFlop.append(1)
    if two in statesFlop:
        flopTwoIndex = statesFlop.index(two)
        encounteredFlop[flopTwoIndex] += 1
    else:
        statesFlop.append(two)
        flopTwoIndex = (len(statesFlop)-1)
        probFlop.append(0)
        encounteredFlop.append(1)
    #--------------------------------------------
    main.dealTurn()
    one = main.getHandStrength(1)
    two = main.getHandStrength(2)
    if one in statesTurn:
        turnOneIndex = statesTurn.index(one)
        encounteredTurn[turnOneIndex] += 1
    else:
        statesTurn.append(one)
        turnOneIndex = (len(statesTurn)-1)
        probTurn.append(0)
        encounteredTurn.append(1)
    if two in statesTurn:
        turnTwoIndex = statesTurn.index(two)
        encounteredTurn[turnTwoIndex] += 1
    else:
        statesTurn.append(two)
        turnTwoIndex = (len(statesTurn)-1)
        probTurn.append(0)
        encounteredTurn.append(1)
    #--------------------------------------------
    main.dealRiver()
    one = main.getHandStrength(1)
    two = main.getHandStrength(2)
    if one in statesRiver:
        riverOneIndex = statesRiver.index(one)
        encounteredRiver[riverOneIndex] += 1
    else:
        statesRiver.append(one)
        riverOneIndex = (len(statesRiver)-1)
        probRiver.append(0)
        encounteredRiver.append(1)
    if two in statesRiver:
        riverTwoIndex = statesRiver.index(two)
        encounteredRiver[riverTwoIndex] += 1
    else:
        statesRiver.append(two)
        riverTwoIndex = (len(statesRiver)-1)
        probRiver.append(0)
        encounteredRiver.append(1)
    #--------------------------------------------
    winner = main.getWinner()

    update(pocketOneIndex,flopOneIndex,turnOneIndex,riverOneIndex,1)
    update(pocketTwoIndex,flopTwoIndex,turnTwoIndex,riverTwoIndex,2)

    if (msvcrt.kbhit()):
        if (ord(msvcrt.getch()) == 27):
            break

    count += 1

saveResults()
p.close()
f.close()
t.close()
r.close()