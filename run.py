"""
import needed methods()
"""
from random import randint


def welcome():
    """
    Welcomes the player and starts or quits the game based on user input.
    User has to choose 'y' or 'n'. This is done using a try statement 
    in a while loop.
    """
    start_game = True
    print("Welcome to ScaleTrainer 1.0 BETA\n"
          "\n"
          "If you want to become a scale Wiz!!!\n"
          "This game will help you get there!\n"
          "\n"
          "Would you like to start the game?")
    print()
    while True:
        try:
            start_game = input("'y' to start. 'n' to quit: \n").upper()
            if start_game == "Y":
                print("OK! Let's GO!")
                print()
            elif start_game == "N":
                start_game = False
            else:
                raise ValueError()
            break
        except ValueError:
            print("Please choose 'y' or 'n'")
    return start_game


def user_name():
    """
    Get the users name and returns it to main function.
    The name has to be more than one character.
    """
    while True:
        try:
            name = input("Please enter your name: \n")
            print()
            if len(name) <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Your name has to be at least one character.")
            print()
            continue
    return name


def choose_scale(name):
    """
    Available scales inside a list of dictionaries.
    List is easy to update if more scales are to be added.
    The "index" is refering to  each notes in the given scale.

    User will choose a scale
    
    Function returns the scale and a scale index.
    """
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
    print(f"Hi {name}, What scale would you like to practice?\n")
    index = 1
    for scale in scales_dict:
        print(f"{index}. {scale.get('scale')}")
        index = index + 1
    print("")
    while True:
        try:
            user_input = int(input("Please choose scale: \n")) - 1
            if user_input < 0:
                raise IndexError()
            scale_notes_index = scales_dict[user_input].get("index")
            scale = scales_dict[user_input].get('scale')
            print(f"Your choice: {scale} scale")
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
    introduce a list of all notes available
    gets scale from user input and the random key and uses that as an
    offset to adjust scale to current key.
    returns a list of all notes in the chosen scale in the
    random key generated.
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
    Also print an illustration so that the player can visualy
    figure out the scale notes.
    The available notes list includes two octaves because if the 
    random key generated is not c
    the whole scale can not be covered by one octave starting from c.
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
    print(f"Random key: {key}")
    print("|   | |  | |   |   | |  | |  | |   |   | |  | |   |   | |  | |\n"
          "|   | |  | |   |   | |  | |  | |   |   | |  | |   |   | |  | |\n"
          "|   |_|  |_|   |   |_|  |_|  |_|   |   |_|  |_|   |   |_|  |_|\n"
          "|  C |  D |  E |  F |  G |  A |  B |  C |  D |  E |  F |  G |\n"
          "|____|____|____|____|____|____|____|____|____|____|____|____|")
    print()
    while True:
        try:
            print(f"Enter each note of the {key} {scale} scale\n"
                  "Separate the notes with a comma.\n"
                  "For example: c,d,e,f,g,a,b\n")
            guess = input("Enter Notes: \n").upper()
            user_list = guess.split(",")
            invalid_entries = []
            if user_list[-1] == "":
                user_list.pop()
            for note in user_list:
                if note in available_notes:
                    pass
                else:
                    invalid_entries.append(note)
            if len(invalid_entries) > 0:
                raise TypeError()
            if len(user_list) != len(scale_index) or len(invalid_entries) > 0:
                raise ValueError()
            break
        except TypeError:
            print(f"{invalid_entries} are not valid notes")
            print("Please enter only valid notes!")
            print(f"Valid notes are: {available_notes[0:12]}\n")
        except ValueError:
            print()
            print(f"Did you enter exactly {len(scale_index)} notes?")
            print("Are all the notes separated by a comma?\n")
            continue
    return user_list


def check_result(scale_notes, guess):
    """
    Takes notes included in chosen scale in random key and compares them
    to the users answer.
    The  user is shown the result.
    Containing
    Correct answer
    Player answer
    Correct notes
    wrong notes
    Missing notes
    A message based on the result.
    """
    print()
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
    print()
    if len(wrong_notes) == 0:
        print("congratulations you were 100% right")
    elif len(wrong_notes) <= 1:
        print("Only one wrong note. Good Job")
    elif len(wrong_notes) <= 3:
        print("Pretty good!")
        print("But you can do better!")
    else:
        print("We recomend much practise")
        print()


def main():
    """
    main function
    Includes quit message 
    Asks playr to continue or quit at the end of each loop.
    """
    run = welcome()
    while run:
        name = user_name()
        while run:
            scale = choose_scale(name)
            key = random_key()
            scale_notes = get_notes_for_scale(scale[0], key[1])
            guess = user_guess(scale[0], scale[1], key[0])
            check_result(scale_notes, guess)
            print("")
            print("Wanna go again?")
            contin = input("'y' for yes, any other key to quit: \n")
            if contin == "y":
                run = True
            else:
                run = False
    print("Sorry to see you go!!\n"
          "Hope to see you soon!\n"
          "Game will now quit...")


main()
