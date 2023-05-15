# Concentration 64
Concentration 64 is a fast-paced clapping game that is often played by children 
in the playground. However, the structure means that it can also be adapted for 
use as a learning activity or to spark discussion. As well as being known as 
Concentration 64, it can also be sung as Concentration 54. The rhyme is simple 
and sets out the rules of the game which is for each player to be able to name 
items in the chosen category with no repetition or hesitation. If the players 
are too slow in naming an item in the category that hasn’t been saying before, 
they lose! Once someone has lost, you simply choose a new person to recite the 
rhyme and choose a brand-new category. We also feature a Memory Training mode 
that provides a way to see how good you really are at memorizing words.


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
1. In the command line you will type **python FinalProject.py CategoryList.json**

# The ideal run for the program
1. After the commoand line is provided to run the program, which is given above,
you will be prompted to the intro of the program that provides two options 
which is Option 1: Memory Training or Option 2: Concetration 64. You must choose 
either 1 or 2 
    - Option 1: Memory Traingin Chosen
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

    

