'''
Created 5/6/2013

poker-bot:
    Create a working poker bot that initially only knows the rules of texas
    hold'em. It knows nothing of a strong hand or anything, but will learn
    through use of Monte Carlo policy updates for reinforcement learning
    by playing against itself.
'''

from game import Game

main = Game()

'''
    need to put hand strength into a part of episode
    [
        hand strength
        community strength
    ]
    is it worth subtracing community from hand for one strength number?
    I have no idea, but we'll save states based off these two things for now
'''
main.startRound()
main.dealFlop()
main.dealTurn()
main.dealRiver()