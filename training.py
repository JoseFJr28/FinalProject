import time
import random

#demo stages of method, will insert into class and also import list of words from a separate file for the final project
words = ['hill', 'vein', 'queen', 'deafening','malicious', 'womanly', 'busy', 'calculate', 'thrill', 'tenuous', 'melt', 'paltry', 'first', 'own', 'sock'
         ,'rifle', 'cause', 'peaceful', 'arithmetic', 'disillusioned', 'quaint', 'detail', 'rock', 'clap', 'settle', 'tie', 'various', 'property', 'elephant','sloth'] 


def mode():
    """ Function that determines the mode for training
    
    Attributes:
        res (str): number of seconds that user inputs to determine the mode of difficulty
    """
    res = int(input(f"Would you like to 10 seconds, 7 seconds, or 3 seconds to memorize the word? Respond with num only."))
    if res == int("10"):
        mode = "Easy"
    elif res == int("7"):
        mode = "Medium"
    else:
        mode = "Hard"
    return mode

def training(mode):
    keep = input("Would you like to start? Type y")
    count = 0
    wrong = 0
    if mode == "Easy":
        print(f"Your mode is Easy")
        while keep != "n":
            word = random.choice(words)
            print(f"Your word is {word}")
            time.sleep(9)
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            ans = input("What word did you see?")
            if ans == word:
                print(f"Good job! You got it right!")
                keep = input("Would you like to keep going? y or n")
                count += 1
            else:
                print(f"Nice try! The answer is {word}")
                wrong += 1
                keep = input("Would you like to keep going? y or n")
    elif mode == "Medium":
        print(f"Your mode is Medium \n")
        while keep != "n":
            word = random.choice(words)
            print(f"Your word is {word}")
            time.sleep(6)
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            ans = input("What word did you see?")
            if ans == word:
                print(f"Good job! You got it right!")
                keep = input("Would you like to keep going? y or n")
                count += 1
            else:
                print(f"Nice try! The answer is {word}")
                wrong += 1
                keep = input("Would you like to keep going? y or n")     
    else:
        print(f"Your mode is Hard \n")
        while keep != "n":
            word = random.choice(words)
            print(f"Your word is {word}")
            time.sleep(2)
            print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            ans = input("What word did you see?")
            if ans == word:
                print(f"Good job! You got it right!")
                count += 1
                keep = input("Would you like to keep going? y or n")
            else:
                print(f"Nice try! The answer is {word}")
                wrong += 1
                keep = input("Would you like to keep going? y or n")
    print(f"Nice session. You've got {count} words right and {wrong} words wrong! Keep practicing your memory training!")
    


def wmode():
    w_t = input("Would you like to practice with words or numbers (w or n)")
    if w_t == 'w':
        w1 = (input("Would you like to memorize words with 3-5 letters, 6-8 letters, or 9-15 letters? Respond with 3, 6, or 9."))
        w2 = (input("Would you like to memorize the word in 2 seconds, 5 seconds, or 8 seconds? Respond with 2, 5, or 8."))
        mode = ('wee' if w1 == str(3) and w2 == str(8) else 'wem' if w1 == str(3) and w2 == str(5) else 'weh' if w1 == str(3) and w2 == str(2) 
                else 'wme' if w1 == str(6) and w2 == str(8) else 'wmm' if  w1 == str(6) and w2 == str(5) else 'wmh' if w1 == str(6) and w2 == str(2)
                else 'whe' if w1 == str(9) and w2 == str(8) else 'whm' if w1 == str(9) and w2 == str(5) else 'whh' if w1 == str(9) and w2 == str(2)
                else 'insane words')
        return mode
    else:
        w3 = str(input("Would you like to memorize the order of 3-5 numbers, 6-9 numbers, or 10-11 numbers? Response with 3, 6, or 10."))
        w4 = str(input("Would you like to memorize the numbers in 3 seconds, 6 seconds, or 9 seconds? Respond with 3, 6, or 9."))
        mode = ('nee' if w3 == 3 and w4 == 9 else 'nem' if w3 == 3 and w4 == 6 else 'neh' if w3 == 3 and w4 == 3 
                else 'nme' if w3 == 6 and w4 == 9 else 'nmm' if  w3 == 6 and w4 == 6 else 'nmh' if w3 == 6 and w4 == 3
                else 'nhe' if w3 == 10 and w4 == 9 else 'nhm' if w3 == 10 and w4 == 6 else 'nhh' if w3 == 10 and w4 == 3
                else 'insane numbers')
        return mode
    
print(wmode())
            
           
        
    