def hangman(word):
    wrong = 0
    stages = [" ",
              "__________                    ",
              "|                                      ",
              "|                  |                  ",
              "|                  0                  ",
              "|                /|\                ",
              "|                 /\                 ",
              "|                                      ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Hangman Game")
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("Guess a letter: ")
    if guess in letters:
        cind = rleters.index(guess)
        board[cind] = char
        rletters[cind] = "$"
    else:
        wrong += 1
    print((" ".join(board)))
    print('\n'.join(stages[0: wrong_guesses + 1]))

hangman("kot")
