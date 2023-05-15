# Concentration 64
Concentration 64 is a fast-paced clapping game that is often played by children 
in the playground. However, the structure means that it can also be adapted for 
use as a learning activity or to spark discussion. As well as being known as 
Concentration 64, it can also be sung as Concentration 54. The rhyme is simple 
and sets out the rules of the game which is for each player to be able to name 
items in the chosen category with no repetition or hesitation. If the players 
are too slow in naming an item in the category that hasn’t been saying before, 
they lose! Once someone has lost, you simply choose a new person to recite the 
rhyme and choose a brand-new category. 

We also feature a Memory Training mode that provides a way to see how skilled
you are at memorizing words or numbers. The user is able to choose whether 
they memorize numbers or words, then they get to choose how much time
they get to memorize their selection and also the length. For example,
they can choose an option that'd give them 3 to 5, 6 to 8, or 9 to 15 letter words.


# File Justification
The following files 3-5.txt, 6-8.txt, and 9-15.txt are needed for the training 
feature that we provide for the game. It provides the list of of words.
CategoryList.json are needed to for the main game Concentration 64 to get the 
categories that are available for the Players to pick.

# How to run the program
1. In the command line you will type **python FinalProject.py CategoryList.json** (it's also important to make sure you're
in the FinalProject directory or else you may run into a file error)
2. Then you are prompted to the intro of the program that provides two options 
which is Option 1: Memory Training or Option 2: Concetration 64.
    - Option 1: Memory Training Chosen:
        - User will be prompted to select between the number or word mode, which they will do by putting the first letter.
        - Afterwards, they choose the time and length for their selection (options will be shown)
            - Instead of input validation if user messes up, a hidden mode activates with the keyword 'insane.' 
            This means the responses to the user input will be mean to the user (as a joke) because the user messed up.
            Otherwise, if the user answers perfectly fine and plays a standard mode, the input will be encouraging.
        - The user will be provided a letter or number based off the settings they selected. When time runs out (time.sleep()), 
        a bunch of new empty lines will appear, basically clearing the user's screen. The user will be asked what word or number
        they saw, and if they got the word correct, the correct tracker will increase otherwise the wrong tracker will increase.
        - The user will be asked if they want to continue, and will answer with the options provided (y/n).
        - When the user decides to answer with n, they'll be provided a summary of their statistics, which includes the mode played, questions answered, questions correct, percentage correct, and questions wrong.
            - If the user chose insane mode, and got 100%, the 'mean' input will actually be a little wholesome. However,
            the user has to answer more than 5 answers correctly, otherwise the input will be mean and no stats will be provided
    - Option 2: Concentration 64 chosen:
        - It will prompt 
    


