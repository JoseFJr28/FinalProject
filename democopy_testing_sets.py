


import demo_vocablist_test_test


def words_used(word):
    catalog = set()
    for word in demo_vocablist_test_test:
        if word in catalog:
            return False
        else:
            catalog.append(input(word))
    
    

catalog = set()

def process_player_input(word):
    if word in demo_vocablist_test_test and word not in catalog:
        catalog.add(word)
        return True
    elif word in demo_vocablist_test_test and word in catalog:
        return False
    else:
        print("The word is not in the vocablist.")
        return None

while True:
    player_word = input("Enter a word: ")
    if player_word.lower() == "quit":
        break

    result = process_player_input(player_word)
    if result is None:
        print("Try again.")
    elif result:
        print("The word has been added to the catalog.")
    else:
        print("You have been eliminated.")
        break
