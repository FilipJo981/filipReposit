import random

color = ["hjärter", "klöver", "spader", "ruter"]
value = ["ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "kneckt", "dam", "kung"]

#klassen card definieras, den innehåller endast en färg och ett värde
class card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

deck = []

#assign value and color to indexes in the deck list (cards in the deck)
#loop through colors
for y in color:
    #loop through values
    for x in value:
        #define card and give properties
        deck.append(card(y, x))

def drawCardPlayer(count):
    for x in range(count):
        drawnCard = random.randrange(0, (len(deck)-1))
        playerHand.append(deck[drawnCard])
        print("Du drog " + str(deck[drawnCard].color) + " " + str(deck[drawnCard].value))
        deck.pop(drawnCard)

def printPlayerHand(input):
    hand = "\nDin hand: "
    points = 0
    for x in playerHand:
        hand += (x.color + " " + str(x.value) + ", ")
        if (x.value == "ess" or x.value == "kneckt" or x.value == "dam" or x.value == "kung"):
            points += 10
        else:
            points += int(x.value)
    hand += "\nDina poäng totalt: " + str(points)
    if (input == "string"):
        return hand
    elif (input == "points"):
        return points

playerHand = []
dealerHand = []

print("Spelet startar! Du får 2 kort!")
drawCardPlayer(2)

while(printPlayerHand("points")<= 21):
    print(printPlayerHand("string"))
    answer = input("Vill du dra ett till kort? y/n")
    if (answer == "y"):
        drawCardPlayer(1)
        answer = ""
    elif (answer == "n"):
        #avsluta spelet
        break
    else:
        print("Du måste skriva y (yes) eller n (no)")


print("Spelet är över!\n"
      +printPlayerHand("string") + "\n")

if (printPlayerHand("points") > 21):
    print("Du har över 21 poäng, du förlorade!")
else:
    print("Du har under 21 poäng")

print("Done!")

print("hej")
#hejhej