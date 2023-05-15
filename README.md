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
feature that we provide for the game. It provides the list of of words and 
numbers for the feature to work.
CategoryList.json is  needed to for the main game Concentration 64 to get the 
categories that are available for the Players to pick.
Disclaimer: The words in the files must be given as they are provided, meaning 
that in this program spelling is highly important and if its plural or not. 
Apologies in advance

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
        - You have a prompt greeting for the game and ask for a simple yes, Y, or 
          no, N. If you choose Y
        - It will prompt you to choose how many players you will have. Minimum is 2
         and maximum is 4. You need two physical players to play
        - Then we ask for the players name
        - Then we ask if you would like a point advantage. This is for kids to be 
          involved in the game and if someone is has a very high ego and can beat 
          you with a point advantage.
          - Yes would ask how many points you would like given from 1-10
          - No will have a defualt score of 0
        - Now we proceed with the nursery rhyme and choose your category from
          the available options we provide.
        - You keep providing words until the last person is in the game as the 
          winner
        - If you say N then we just have you we prompt a good by message.
        - If you provide something that is not a Y or N prompts you with a set
         message to make sure to leave a 5 star rating on Yelp.

## The troubleshooting errors that still need fixing
We tried implementing the leaderboard as best as we could but everytime we were 
unable to implement it. However we do have it in the code to show that we tried.

## Attribution Table

|          Method/Function          |Primary Author|Techniques Demonstrated|
| --------------------------------- | ------------ | --------------------- |
|Player/Concentration _repr_()      |     John     |     Magic Methods     |
|Player __init__()                  |     John     |   Optional Parameters |
|Concentration Round_start()        |     Jose     |      Composition      |
|Concentration Round_start()        |     Jose     |       json.load       |
|TrainingMemory file()              |   Adithya    |      with open()      |
|TrainingMemory training_exercise() |   Adithya    |f-strings w expressions|
|argeparse                          |      Mo      |     ArgumentParse     |
|Concentration convert_dict()       |      Mo      |  List comprehension   |
|Concentration check_words          |    Melissa   |    Set Operations     |
|Concentration Is_there_a_winner    |    Melissa   | Conditional Expression|

### Reference List for the Terms

Frimpong, Francis, et al. “List of Fruits: 100+ Fruit Names in English with Pictures • 7ESL.” 7ESL, 7 Feb. 2023, 7esl.com/fruits-vocabulary-english/

Learn to Play, bicyclecards.com/how-to-play. Accessed 14 May 2023. 

Proballers. “NBA Players List (2010-2011).” Proballers, www.proballers.com/basketball/league/3/nba/players/2010. Accessed 14 May 2023.
