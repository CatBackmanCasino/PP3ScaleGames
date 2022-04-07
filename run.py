"""
import needed methods()
"""
from random import randint

scales_dict = [{
    "scale": "Major",
    "index": [0, 2, 4, 5, 7, 9, 11]
}, {
    "scale": "Natural Minor",
    "index": [0, 2, 3, 5, 7, 8, 10]
}, {
    "scale": "Harmonic Minor",
    "index": [0, 2, 3, 5, 7, 8, 11]
}, {
    "scale": "Dorian",
    "index": [0, 2, 3, 5, 7, 9, 10]
}, {
    "scale": "Lydian",
    "index": [0, 2, 4, 6, 7, 9, 11]
}]


def welcome():
    """
    Welcomes the player and starts the game.
    """
    start_game = True
    print("Welcome to ScaleTrainer 1.0 BETA\n"
          "\n"
          "If you wish to know your scales this game is for you.\n"
          "\n"
          "Choose the scale you wish to practice\n"
          "then the Game will randomize a key and you will be asked to enter\n"
          "the notes for that scale in a random key.\n"
          "Would you like to start game?")
    start_game = input("y/n: ")
    if start_game == "y":
        print("OK! Let's GO!")
        start_game = True
    else:
        start_game = False
    return start_game


def instructions():
    """
    Gives player instructions
    """

    print("Game instructions:\n"
          "1. Choose scale\n"
          "2. Enter all the notes of that scale in the key provided\n"
          "3. Your result is shown\n"
          "4. play again!"
          "\n")


def choose_scale():
    """
    let user choose scale
    returns the scale and a scale index
    """
    print("What scale would you like to practice?")
    index = 1
    for scale in scales_dict:
        print(f"{index}. {scale.get('scale')}")
        index = index + 1
    print("")
    while True:
        try:
            user_input = int(input("Please choose scale: ")) - 1
            scale_notes_index = scales_dict[user_input].get("index")
            scale = scales_dict[user_input].get('scale')
            print(f"You Choose the {scale} scale")
            break
        except IndexError:
            num_scales = len(scales_dict)
            print(f"Please enter a number between 1 and {num_scales}")
            continue
        except ValueError:
            print("Input has to be one single number")
            continue

    return [scale_notes_index, scale]


def random_key():
    """
    generates a random key and returns a key and a key index
    :return:
    """
    list_of_keys = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B"]
    key_index = randint(0, 11)
    key = list_of_keys[key_index]
    return [key.upper(), key_index]


def get_notes_for_scale(scale, key_index):
    """
    generates a list of all notes included in the list.
    gets scale from user input and the random key_index and uses that as an
    offset to adjust scale to current key.
    """
    available_notes = [
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "B",
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#",
        "A",
        "A#",
        "A"]
    key_offset = key_index
    notes = [available_notes[index + key_offset] for index in scale]
    return notes


def user_guess(scale_index, scale, key):
    """
    takes users answer, converts it to a list and compares it to scale_notes
    """
    print(f"Enter all the {len(scale_index)} notes of the {key} {scale} scale")
    print("|   | |  | |   |   | |  | |  | |   |\n"
          "|   | |  | |   |   | |  | |  | |   |\n"
          "|   | |  | |   |   | |  | |  | |   |\n"
          "|  C |  D |  E |  F |  G |  A |  B |\n"
          "|____|____|____|____|____|____|____|")

    while True:
        try:
            guess = input("enter each note separated by ',': ").upper()
            user_list = guess.split(",")
            if len(user_list) != len(scale_index):
                raise ValueError()
            break
        except ValueError:
            print(f"Did you enter exactly {len(scale_index)} notes?")
            print("Are all the notes separated by a comma?")
            continue

    return user_list


def check_result(scale_notes, guess):
    """
    takes two parameters and compares them.
    if the notes in the users guess (guess parameter) are all in the scale
     (scale_notes)
    it will print a congratulations message
    if not it will tell you the wrong notes and the notes missing
    """
    print(f"The notes in this scale are: {scale_notes}")
    print()
    print(f"Your answer: {guess}")
    print()
    correct_notes = []
    wrong_notes = []
    missing_notes = []
    for note in guess:
        note = note.upper()
        if note in scale_notes:
            correct_notes.append(note)
        else:
            wrong_notes.append(note)

    for note in scale_notes:
        note = note.upper()
        if note in guess:
            pass
        else:
            missing_notes.append(note)
    print(f"Correct Notes: {correct_notes}")
    print(f"Wrong Notes: {wrong_notes}")
    print(f"Missing Notes: {missing_notes}")
    if len(wrong_notes) == 0:
        print("congratulations you were 100% right")
    elif len(wrong_notes) <= 1:
        print("Only one wrong note. Good Job")
    elif len(wrong_notes) <= 3:
        print("Pretty good!")
        print("But you can do better!")
    else:
        print("We recomend much practise")


def main():
    """
    main function
    """
    run = welcome()
    while run:
        instructions()
        choose_scale()
        scale = choose_scale()
        key = random_key()
        scale_notes = get_notes_for_scale(scale[0], key[1])
        guess = user_guess(scale[0], scale[1], key[0])
        check_result(scale_notes, guess)
        print("")
        print("Wanna go again?")
        contin = input("'y' for yes, any other key to quit: ")
        if contin == "y":
            run = True
        else:
            print("Good Job!!\n"
                  "Hope to see you soon again")
            run = False
    return run


main()

