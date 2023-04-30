def main():
    filenames = ['categories1.json', 'categories2.json']
    categories = load_words(filenames)

    players = [ComputerPlayer()] + [HumanPlayer(f'Human {i}') for i in range(1, 3)]

    while True:
        print("Choose a category:", ', '.join(categories.keys()))
        category = input().strip()

        if category not in categories:
            print("Invalid category. Please choose from the list.")
            continue

        for player in players:
            if isinstance(player, ComputerPlayer):
                word = player.choose_word(category, categories)
                print(f"{player.name} chose: {word}")
            else:
                word = player.choose_word()

            if player.is_eliminated(word):
                print(f"{player.name} is eliminated!")
                return
            else:
                player.update_used_words(word)

if __name__ == '__main__':
    main()
