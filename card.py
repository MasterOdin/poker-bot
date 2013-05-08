class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def getCard(self):
        return [self.suit, self.number]

    def getCardDisplay(self):
        return [self.suit, self.__convertToDisplay(self.number)]

    def getSuit(self):
        return self.suit;

    def getSuitNumber(self):
        if (self.suit == "club"):
            return 0
        elif (self.suit == "diamond"):
            return 1
        elif (self.suit == "heart"):
            return 2
        elif (self.suit == "spade"):
            return 3

    def getNumber(self):
        return self.number;

    def getNumberDisplay(self):
        return self.__convertToDisplay(self.number);

    def __convertToDisplay(self,number):
        if (number < 11):
            return number;
        elif (number == 11):
            return "Jack"
        elif (number == 12):
            return "Queen"
        elif (number == 13):
            return "King"
        elif (number == 14):
            return "Ace"
        else:
            return "Unknown"
