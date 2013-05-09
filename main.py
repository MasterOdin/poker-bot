from game import Game
import bot

game = Game()
playerF = False
botF = False
winner = 0
gameGoing = True

def getAction(botAction,part):
    global winner
    cont = False
    while not cont:
        a = input('--> ')
        a = a.lower()
        action = ''
        bot = ''
        if a == 'bet':
            action = 'bet'
        elif a == 'check':
            action = 'check'
        elif a == 'call':
            if bot != 'bet':
                action = 'check'
            else:
                action = 'call'
                return True
        elif a == 'fold':
            winner = 2
            return False
        else:
            continue        
        b = botAction
        if b == -1:
            if action == 'check':
                bot = 'check'
                cont = True
            else:
                bot = 'fold'
                winner = 1              
                print("Bot: " + bot)
                return False
        elif b == 1:
            if action == 'check':
                bot = 'check'
                cont = True
            else:
                bot = 'call'
                cont = True
        elif b == 2:
            bot = 'bet'
        print("Bot: " + bot)

    return True

print("Let's play poker!!! (Actions: check | fold | call | bet)\n")
while gameGoing:
    game.startRound()
    game.displayPlayer(1)
    if (not getAction(bot.chooseAction(game.getHandStrength(2),0),0)):
        break
    print("---Flop---")
    game.dealFlop()
    game.displayPlayer(0)
    if (not getAction(bot.chooseAction(game.getHandStrength(2),1),1)):
        break
    print("---Turn---")
    game.dealTurn()
    game.displayPlayer(0)
    if (not getAction(bot.chooseAction(game.getHandStrength(2),2),2)):
        break
    print("---River---")
    game.dealRiver()
    game.displayPlayer(0)
    if (not getAction(bot.chooseAction(game.getHandStrength(2),3),3)):
        break
    winner = game.getWinner()
    if winner == -1:
        winner = 2
    gameGoing = False

print("Player " + str(winner) + " won!")
