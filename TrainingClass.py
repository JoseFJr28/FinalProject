import random
import time

class Training:
    def __init__(self, mode = ''):
        self.mode = mode
    def mode():
        w_t = input("Would you like to practice with words or numbers (w or n)")
        if w_t == 'w':
            w1 = input("Would you like to memorize words with 3-5 letters, 6-8 letters, or 9+ letters? Respond with 3, 6, or 9.")
            w2 = input("Would you like to memorize the word in 2 seconds, 5 seconds, or 8 seconds? Respond with 2, 5, or 8.")
            if w1 == 3 and w2 == 8:
                mode = 'wee'
            elif w1 == 3 and w2 == 5:
                mode == 'wem'
            elif w1 == 3 and w2 == 2:
                mode = 'weh'
            elif w1 == 6 and w2 == 8:
                mode = 'wme'
            elif w1 == 6 and w2 == 5:
                mode = 'wmm'
            elif w1 == 6 and w2 == 2:
                mode = 'wmh'
            elif w1 == 9 and w2 == 8:
                mode = 'whe'
            elif w1 == 9 and w2 == 5:
                mode = 'whm'
            elif w1 == 9 and w2 == 2:
                mode = 'whh'
            else:
                #if someone messes up the instructions, they're automatically signed up for a secret mode which is the hardest
                mode = 'insane words'
            return mode
        else:
            w3 = input("Would you like to memorize the order of 3-5 numbers, 6-9 numbers, or 10-11 numbers? Response with 3, 6, or 10.")
            w4 = input("Would you like to memorize the numbers in 3 seconds, 6 seconds, or 9 seconds? Respond with 3, 6, or 9.")
            if w3 == 3 and w4 == 3:
                mode = 'nee'
            elif w3 == 3 and w4 == 6:
                mode == 'nem'
            elif w3 == 3 and w4 == 9:
                mode = 'neh'
            elif w3 == 6 and w4 == 3:
                mode = 'nme'
            elif w3 == 6 and w4 == 6:
                mode = 'nmm'
            elif w3 == 6 and w4 == 9:
                mode = 'nmh'
            elif w3 == 10 and w4 == 3:
                mode = 'nhe'
            elif w3 == 10 and w4 == 6:
                mode = 'nhm'
            elif w3 == 10 and w4 == 9:
                mode = 'nhh'
            else:
                #if someone messes up the instructions, they're automatically signed up for a secret mode which is the hardest
                mode = 'insane numbers'
        return mode
    def training_exercise(mode, t=3):
        keep = input("Would you like to start? Type y")
        count = 0
        wrong = 0