'''
Created 5/6/2013

game.py:
    Main game class and logic. Contains methods on creating deck and shuffling
    and dealing out cards as needed

    Note: while dealing with the hand, it should be kept self sorted when adding
    new cards. Lowest card first in the list for the hand.

    self.__second should start at 00 and proceed upward as necessary
'''

from card import Card
import random

class Game:
    def __init__(self):
        self.deckStart = self.__createDeck();
        self.__handOne = []
        self.__handTwo = []
        self.__community = []

    # public functions
    def startRound(self):
        self.__deck = self.__shuffle(self.deckStart[:]);
        self.__handOne = []
        self.__handTwo = []
        self.__addToHand(self.__handOne,self.__deck.pop(0))
        self.__addToHand(self.__handTwo,self.__deck.pop(0))
        self.__addToHand(self.__handOne,self.__deck.pop(0))
        self.__addToHand(self.__handTwo,self.__deck.pop(0))
        self.__iHandOne = self.__handOne[:]
        self.__iHandTwo = self.__handTwo[:]        
        self.__community = []

    def dealFlop(self):
        self.__deck.pop(0)
        card = self.__deck.pop(0)
        self.__addToHand(self.__community,card)
        self.__addToHand(self.__handOne,card)
        self.__addToHand(self.__handTwo,card)
        card = self.__deck.pop(0)
        self.__addToHand(self.__community,card)
        self.__addToHand(self.__handOne,card)
        self.__addToHand(self.__handTwo,card)
        card = self.__deck.pop(0)
        self.__addToHand(self.__community,card)
        self.__addToHand(self.__handOne,card)
        self.__addToHand(self.__handTwo,card)                         

    def dealTurn(self):
        self.__deck.pop(0)
        card = self.__deck.pop(0)
        self.__addToHand(self.__community,card)
        self.__addToHand(self.__handOne,card)
        self.__addToHand(self.__handTwo,card) 

    def dealRiver(self):
        self.__deck.pop(0)
        card = self.__deck.pop(0)
        self.__addToHand(self.__community,card)
        self.__addToHand(self.__handOne,card)
        self.__addToHand(self.__handTwo,card) 

    def getHandStrength(self,player):
        if (player == 0):
            return round(self.__calculateHand(self.__community),15)
        if (player == 1):
            return round(self.__calculateHand(self.__handOne),15)
        elif (player == 2):
            return round(self.__calculateHand(self.__handTwo),15)
        else:
            return 0

    def getWinner(self):
        one = self.__calculateHand(self.__handOne)
        two = self.__calculateHand(self.__handTwo)
        if (one > two):
            return 1
        elif (one == two):
            return 0
        else:
            return -1

    def displayPlayer(self,player):
        if (player == 1):
            use = self.__iHandOne
        elif (player == 2):
            use = self.__iHandTwo
        elif (player == 0):
            use = self.__community
        else:
            return False
        print("Player " + str(player) + " has:")
        for i in range(0,len(use)):
            print(use[i].getCard())
        return True

    # internal functions
    def __createDeck(self):
        deck = [];
        suits = ['spade','heart','club','diamond']
        count = 0;
        for suit in suits:
            for i in range(2,15):
                deck.append(Card(suit,i));

            '''
            deck.append(Card(suit,"jack"));
            deck.append(Card(suit,"queen"));
            deck.append(Card(suit,"king"));
            deck.append(Card(suit,"ace"));
            '''
        return deck;

    def __shuffle(self, deck):
        for i in range(0,3):
            for j in range(0,52):
                rand = int(random.uniform(0,52))
                temp = deck[j];
                deck[j] = deck[rand];
                deck[rand] = temp;
        return deck

    def __addToHand(self,hand,card):
        if (len(hand) == 0):
            hand.append(card)
        else:
            for i in range(0,len(hand)):
                if (hand[i].getNumber() > card.getNumber()):
                    hand.insert(i,card)
                    return
            hand.append(card)

    '''
    ways to win:
        0: card high
        1: pair
        2: two pair
        3: three of a kind
        4: straight
        5: flush
        6: full house
        7: four of a kind
        8: straight flush
        9: royal flush

        returns:
            double - strength of win based on calculation 
                format: 
                    x.xxx - first number is type above
                    rest of the numbers is strength of type
    '''
    def __calculateHand(self,hand):
        first = 0
        self.__second = 0
        self.__suits = [0,0,0,0]
        self.__cards = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        #               0 1 2 3 4 5 6 7 8 9 0 j q k a
        self.__calculateDistribution(hand)
        if (len(self.__community) > 0):
            if (self.__checkRoyalFlush(hand)):
                first = 9
            elif (self.__checkStraightFlush(hand)):
                first = 8
            elif (self.__checkFourKind(hand)):
                first = 7
            elif (self.__checkFullHouse(hand)):
                first = 6
            elif (self.__checkFlush(hand)):
                first = 5
            elif (self.__checkStraight(hand)):
                first = 4
            elif (self.__checkThreeKind(hand)):
                first = 3
            elif (self.__checkTwoPair(hand)):
                first = 2
            elif (self.__checkPair(hand)):
                first = 1
            elif (self.__checkHighCard(hand)):
                first = 0
        else:
            if (self.__checkPair(hand)):
                first = 1
            elif (self.__checkHighCard(hand)):
                first = 0

        return first+self.__second;

    def __calculateDistribution(self,hand):
        ten = False
        for i in range(0,len(hand)):
            self.__suits[hand[i].getSuitNumber()] += 1
            self.__cards[hand[i].getNumber()] += 1
            if (hand[i].getNumber() == 10 and not ten):
                self.__firstTen = i
                ten = True

    def __checkRoyalFlush(self,hand):
        for i in range(10,15):
            if (self.__cards[i] == 0):
                return False
        for i in range(0,4):
            if (self.__suits[i] < 5):
                continue
            count = 0
            card = 10
            for j in range(self.__firstTen,len(hand)):
                if (hand[j].getNumber() == card and hand[j].getSuitNumber() == i):
                    card += 1
                    count += 1
                elif (hand[j].getNumber() == (card+1)):
                    break
                if (count == 5):
                    return True
            return False

    def __checkStraightFlush(self,hand):
        for i in range(0,4):
            if (self.__suits[i] < 5):
                continue
            count = 1
            card = hand[0].getNumber()
            for j in range(1,len(hand)):
                if (hand[j].getSuitNumber() == i):
                    if (hand[j].getNumber() == card+1):
                        card += 1
                        count += 1
                    elif (count < 5):
                        if (card == 5 and count == 4):
                            if (self.__cards[14] > 0):
                                count += 1
                        else:                     
                            card = hand[j].getNumber()
                            count = 1
                    else:
                        break
            if (count == 5):
                self.__second = self.__calculateDistance(8)*(card-5)
                return True
        return False        
        
    def __checkFourKind(self,hand):
        kicker = 0
        dist = 0
        for i in range(14,1,-1):
            if (self.__cards[i] == 4):
                dist = self.__calculateDistance(13)
                card = i
            elif (self.__cards[i] > 0 and kicker == 0):
                kicker = i
        if (dist > 0):
            self.__second = dist*(card-2)+self.__calculateKickerDistance(dist)*(kicker-2)
            return True
        else:
            return False

    def __checkFullHouse(self,hand):
        gotThree = False
        threeValue = 0
        gotTwo = False
        twoValue = 0
        for i in range(14,1,-1):
            if (not gotThree and self.__cards[i] == 3):
                gotThree = True
                threeValue = i
            elif (not gotTwo and self.__cards[i] == 2):
                gotTwo = True
                twoValue = i

            if gotTwo and gotThree:
                dist = self.__calculateDistance(13)
                self.__second = dist*(threeValue-2)+self.__calculateKickerDistance(dist)*(twoValue-2)
                return True

        return False

    def __checkFlush(self,hand):
        for i in range(0,4):
            total = 0
            count = 0            
            if (self.__suits[i] >= 5):
                for j in range((len(hand)-1),-1,-1):
                    if (hand[j].getSuitNumber() == i):
                        total += (self.__calculateDistance(13)*(hand[j].getNumber()-2))/pow(100,(len(hand)-1)-j)
                        count += 1
                        if (count == 5):
                            self.__second = total
                            return True
        return False

    def __checkStraight(self,hand):
        # I think straights are my least favorite calculation
        card = hand[0].getNumber()
        count = 1
        for i in range(1,len(hand)):
            if (hand[i].getNumber() == card+1):
                count += 1
                card += 1
            elif (count < 5):
                # check for wrap around ace
                if (card == 5 and count == 4):
                    if (self.__cards[14] > 0):
                        count += 1
                else:
                    count = 1
                    card = hand[i].getNumber()
            else:
                break
        if (count >= 5):
            self.__second = self.__calculateDistance(8)*(card-5)
            return True
        return False

    def __checkThreeKind(self,hand):
        threeValue = -1
        maxKicker = -1
        secondKicker = -1
        for i in range(14,1,-1):
            if (self.__cards[i] == 3 and threeValue == -1):
                threeValue = i
            elif (self.__cards[i] > 0):
                if (maxKicker == -1):
                    maxKicker = i
                elif (secondKicker == -1):
                    secondKicker = i        
        if (threeValue > -1):
            dist = self.__calculateDistance(13)
            kickerOne = self.__calculateKickerDistance(dist)
            kickerTwo = self.__calculateKickerDistance(kickerOne)
            self.__second = dist*(threeValue-2)+kickerOne*(maxKicker-2)+kickerTwo*(secondKicker-2) 
            return True
        else:
            return False        

    def __checkTwoPair(self,hand):
        firstPair = -1
        secondPair = -1
        kicker = -1
        for i in range(14,1,-1):
            if (self.__cards[i] == 2):
                # get two highest pairs, and ignore the potential third one
                if (firstPair == -1):
                    firstPair = i
                elif (secondPair == -1):
                    secondPair = i
            elif (self.__cards[i] > 0):
                if (kicker == -1):
                    kicker = i
            if (firstPair != -1 and secondPair != -1 and kicker != -1):
                break
        if firstPair > -1:
            dist = self.__calculateDistance(13)
            pairTwo = self.__calculateKickerDistance(dist)
            kickerDist = self.__calculateKickerDistance(pairTwo)    
            self.__second = dist*(firstPair-2)+pairTwo*(secondPair-2)+kickerDist*(kicker-2)
            return True
        else:
            return False

    def __checkPair(self,hand):
        pair = -1
        kickerOne = -1
        kickerTwo = -1
        kickerThree = -1
        for i in range(14,1,-1):
            if (self.__cards[i] == 2):
                if (pair == -1):
                    pair = i
            elif (self.__cards[i] > 0):
                if (kickerOne == -1):
                    kickerOne = i
                elif (kickerTwo == -1):
                    kickerTwo = i
                elif (kickerThree == -1):
                    kickerThree = i
            if (pair != -1 and kickerOne != -1 and kickerTwo != -1 and kickerThree != -1):
                break
        if (pair > 0):
            dist = self.__calculateDistance(13)
            kickOne = self.__calculateKickerDistance(dist)
            kickTwo = self.__calculateKickerDistance(kickOne)
            kickThr = self.__calculateKickerDistance(kickTwo)
            self.__second = dist*(i-2)+kickOne*(kickerOne-2)+kickTwo*(kickerTwo-2)+kickThr*(kickerThree-2)
            return True
        else:
            return False


    def __checkHighCard(self,hand):
        self.__second = self.__calculateDistance(13)*(hand[len(hand)-1].getNumber()-2)
        return True

    # calculate distance bettween whole numbers for number of possible types of a particular hand
    # ie. 13 types of pairs, 13 types of three of a kind, etc.
    def __calculateDistance(self,number):
        return 1/number

    # calculate how much effect kicker has on strenght calculation
    def __calculateKickerDistance(self,dist):
        return (dist)/13
