import random
import time
       
class Training:
    def __init__(self):
        self.l_3_5 = []
        self.l_5_8 = []
        self.l_9_15 = []
        with open("FinalProject/9-15.txt", "r") as f_9_15:
                for words in f_9_15:
                    self.l_9_15.append(words.split(", "))
        with open("FinalProject/5-8.txt", "r") as f_5_8:
                for words in f_5_8:
                    self.l_5_8.append(words.split(", "))
        with open("FinalProject/3-5.txt", "r") as f_3_5:
                for words in f_3_5:
                    self.l_3_5.append(words.split(", "))
    def mode():
        w_t = input("Would you like to practice with words or numbers (w or n)")
        if w_t == 'w':
            w1 = str(input("Would you like to memorize words with 3-5 letters, 6-8 letters, or 9-15 letters? Respond with 3, 6, or 9."))
            w2 = str(input("Would you like to memorize the word in 2 seconds, 5 seconds, or 8 seconds? Respond with 2, 5, or 8."))
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
    def training_exercise(self):
        keep = input("Would you like to start? Type y")
        count = 0
        wrong = 0
        if Training.mode == "wee":
            print(f"You chose an easy mode regarding both the count of letters and the time!")
            while keep != "n":
                word = random.choice(Training.l_3_5)
                print(f"Your word is {word}")
                time.sleep(8)
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
            return f"Nice session. You've got {count} words right and {wrong} words wrong! Keep practicing your memory training!"
        elif Training.mode == "nee":
            print(f"You chose an easy mode regarding both the count of numbers and the time!")
            while keep != "n":
                l5 = (['a','a', 'a', 'a', 'a'], ['a', 'a', 'a', 'a'], ['a', 'a', 'a']) 
                d = random.choice(l5)
                num = ''
                for i in d:
                    num += str(random.randint(0, 9))
                    cn = int(num)
                print(f"Your number is {cn}")
                time.sleep(9)
                print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                ans = input("What number did you see?")
                if ans == cn:
                    print(f"Good job! You got it right. The number is {cn}!")
                    count += 1
                else:
                    print(f"Nice try! The answer is {cn}.")
                    wrong += 1
                    keep = input("Would you like to keep going? y or n")
                return f"Nice session. You've answered {count+wrong} questions with {count} being correct and {wrong} being incorrect."
                    
                    
                
Training.training_exercise(Training.mode())
    
                
    