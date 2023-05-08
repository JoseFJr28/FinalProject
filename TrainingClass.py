import random
import time
import re
 

class TrainingMemory():
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
            mode = ('nee' if w3 == str(3) and w4 == str(9) else 'nem' if w3 == str(3) and w4 == str(6) else 'neh' if w3 == str(3) and w4 == str(3) 
                    else 'nme' if w3 == str(6) and w4 == str(9) else 'nmm' if  w3 == str(6) and w4 == str(6) else 'nmh' if w3 == str(6) and w4 == str(3)
                    else 'nhe' if w3 == str(10) and w4 == str(9) else 'nhm' if w3 == str(10) and w4 == str(6) else 'nhh' if w3 == str(10) and w4 == str(3)
                    else 'insane numbers')
            return mode

    def file(mode):
        l_3_5 = []
        l_6_8 = []
        l_9_15 = []
        if re.search("^w.", mode):
            if mode[1] == 'h':
                with open("9-15.txt", "r") as f_9_15:
                    for words in f_9_15:
                        l_9_15.extend(words.split(", "))
                        return l_9_15
            elif mode[1] == 'm':
                with open("6-8.txt", "r") as f_6_8:
                    for words in f_6_8:
                        l_6_8.extend(words.split(", "))
                        return l_6_8
            elif mode[1] == 'e':
                with open("3-5.txt", "r") as f_3_5:
                    for words in f_3_5:
                        l_3_5.extend(words.split(", "))
                        return l_3_5
        elif mode == 'insane words':
            with open("9-15.txt", "r") as f_9_15:
                for words in f_9_15:
                    l_9_15.extend(words.split(", "))
            with open("6-8.txt", "r") as f_6_8:
                for words in f_6_8:
                    l_6_8.extend(words.split(", "))
            with open("3-5.txt", "r") as f_3_5:
                for words in f_3_5:
                    l_3_5.extend(words.split(", "))
            combined = []
            combined.extend(l_9_15)
            combined.extend(l_6_8)
            combined.extend(l_3_5)
            return combined
        else:
            return None

    def training_exercise(mode):
        keep = input("Would you like to start? Type (y/n)")
        count = 0
        wrong = 0

        # print statements indicating the mode
        if mode[1] == 'e':
            (print(f"Your mode is easy.") if mode[2] == 'e' 
            else print(f"Your mode is easy with a medium emphasis on time.") if mode[2] == 'm' 
            else print(f"Your mode is easy with a hard emphasis on time."))
        elif mode[1] == 'm':
            (print(f"Your mode is medium with an easy emphasis on time.") if mode[2] == 'e' 
            else print(f"Your mode is medium.") if mode[2] == 'm' 
            else print(f"Your mode is medium with a hard emphasis on time."))
        elif mode[1] == 'h':
            (print(f"Your mode is hard with an easy emphasis on time.") if mode[2] == 'e' 
            else print(f"Your mode is hard with a medium emphasis on time.") if mode[2] == 'm' 
            else print(f"Your mode is hard."))
        else:
            print("You have messed up while inputting your responses to the prior questions about difficulty mode and time.")
            print("As a result, you've automatically been signed up for insane mode lol, do better")


        if mode[0] == 'n' or mode == 'insane numbers':
            n5 = ([1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1])
            n9 = ([1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]) 
            n11 =([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
            insanen = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            insanen.extend(n5)
            insanen.extend(n9)
            insanen.extend(n11) 
            
            while keep != "n":
                number = ''
                digits = (random.choice(n5) if mode[1] == 'e' else random.choice(n9) if mode[1] == 'm'
                            else random.choice(n11) if mode[1] == 'h' else random.choice(insanen))
                for i in digits:
                    number += str(random.randint(0, 9))
                printed_number = int(number)
                print(f"The number is {printed_number}.")
                if mode[2] == 'e':
                    time.sleep(9)
                elif mode[2] == 'm':
                    time.sleep(6)
                elif mode[2] == 'h':
                    time.sleep(3)
                else:
                    time.sleep(random.randint(2,12))
                print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                answer = int(input("What number did you see?"))
                
                if mode != "insane numbers":
                    if answer == printed_number:
                        print(f"Good job! You got it right!")
                        print(f"\n")
                        count += 1
                        keep = input("Would you like to keep going? (y/n)")
                    else:
                        print(f"Nice try! The answer is {printed_number}")
                        print(f"\n")
                        wrong += 1
                        keep = input("Would you like to keep going? (y/n)")
                else:
                    if answer == printed_number:
                        print("FRAUD ALERT. You got extremely lucky; I just want you know that. \n")
                        count += 1
                        keep = input("I really hope you quit! It's excruciating watching you hahahahahhahahaha. Are you still going? (y/n)")
                    else:
                        print(f"HAHA you suck. The correct number is {printed_number}, but even with a lot of practice, you wouldn't be able to get that. \n")
                        wrong += 1
                        keep = input("You should quit, you're not going to get anywhere. Are you going to continue? (y/n)")
        else:
            l = TrainingMemory.file(mode)     
            while keep != "n":
                word = random.choice(l)
                print(f"Your word is {word}")
                if mode[2] == 'e':
                    time.sleep(8)
                elif mode[2] == 'm':
                    time.sleep(5)
                elif mode[2] == 'h':
                    time.sleep(2)
                else:
                    time.sleep(random.randint(1,3))
                print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                ans = str(input("What word did you see?"))
                if ans == word:
                    if mode != 'insane words':
                        print(f"Good job! You got it right!")
                        keep = input("Would you like to keep going? (y/n)")
                    else:
                        print(f"Aren't you a lucky bastard. Won't happen again.")
                        keep = input("I hope you quit. Are you going to continue? (y/n)")
                    count += 1
                else:
                    if mode != 'insane words':
                        print(f"Aw, nice try! You can still do this! Keep practicing! The correct answer was {word}.")
                        keep = input("Would you like to keep going? (y/n)")
                    else:
                        print(f"HAHA, not surprised. ")
                        keep = input("PLEASE QUIT, the sight of failure makes me want to throw up. Are you going to continue (y/n)?")
                    wrong += 1

        if mode[0] == 'w' or mode[0] == 'n':
            print("\n")
            print(f"Nice session. Make sure to keep practicing!")
            print(f"Here are your stats: \n")
            print(f"Mode: {mode}")
            print(f"Guessed correct: {count}")
            print(f"Guessed incorrect: {wrong}")
            print(f"Percentage and total: {round(((count)/(count+wrong))*100, 2)}% correct, {count+wrong} words/numbers \n")
            print("Have a great day!")
        else:
            print("\n")
            if (count) / (count + wrong) == 1 and count > 5:
                print(f"You know what. I'll give it to you, you did an ok job.")
                time.sleep(1)
                print(f"Actually, you probably cheated but I couldn't care less to find out. you're not that important.")
                print(f"You got {count} words/numbers right.")
            elif (count) / (count + wrong) == 1 and count < 6:
                print(f"wtf was the point of 'training' when you barely did anything. garbage work ethic. i'm not going to give you any stats, get out of here.")
            else:
                print(f"Finally you're done. I knew you were gonna quit soon. It was unbearable watching you try.")
                print(f"Here are your crappy stats: \n")
                print(f"Mode: {mode}")
                print(f"Lucky Guess(es): {count}")
                print(f"Expected Incorrect Guesses: {wrong}")
                print(f"Percentage and total: {round(((count)/(count+wrong))*100, 2)}% correct, {count+wrong} words/numbers")
    

    



        
    