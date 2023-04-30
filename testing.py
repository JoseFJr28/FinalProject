import random

sample = {
    "Animals" : {
        1: "Aardvark",
        2: "Abyssinian",
        3: "Adelie Penguin",
        4: "Affenpinscher",
        5: "Afghan Hound",
        6: "African Bush Elephant",
        7: "African Civet",
        8: "African Clawed Frog",
        9: "African Forest Elephant",
        10: "African Palm Civet",
        11: "African Penguin",
        12: "African Tree Toad",
        13:	"African Wild Dog",
        14:	"Ainu Dog",
        15:	"Airedale Terrier",
        16:	"Akbash",
        17:	"Akita",
        18:	"Alaskan Malamute",
        19:	"Albatross",
        20:	"Aldabra Giant Tortoise"
    }
}
new_brain = []

#How to copy  the dictiomary 
mum = 17
comp ={}

for x in sample.values():
    for y in x:
        print(f'{x[y]}')
        new_brain.append(x[y])
print(new_brain)

"""Determines which items in the dictionary will be addded to the npc brain
list by random number"""
def some():
    crazy = random.randrange(1,20)
    return crazy

#How you would get the dictionary to add the words it needs in its system
#depending on the mode
ram = 8
newcount = 0
finalk = []
while newcount < ram:
    looking = some()
    for x in sample.values():
        for y in x:
            if y == looking and y not in finalk and x[y] not in finalk:
                finalk.append(x[y])
            
    newcount += 1
print(finalk)
