color = ["hearts", "clubs", "spades", "diamonds"]
value = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "knight", "queen", "king"]

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
        deck.append(card(x, y))

for x in deck:
    print(x.color + " " + x.value)

#nu har vi en oblandad kortlek, 52 kort i en list
#efteråt skall skapas ett spel, "higher lower"

"""
if deck[random.randrange(0, 52)] < choice:
    print("correct")
"""