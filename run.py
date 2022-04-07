scales_dict = [{
    "scale": "Major",
    "index": [0, 2, 4, 5, 7, 9, 11]
}, {
    "scale": "Natural Minor",
    "index": [0, 2, 3, 5, 7, 8, 10]
}]

def welcome():
    """
    Welcomes the player and starts the game.
    """
    print("Welcome to ScaleTrainer 1.0 BETA\n"
          "\n"
          "If you wish to know your scales this game is for you.\n"
          "\n"
          "Choose the scale you wish to practice\n"
          "then the Game will randomize a key and you will be asked to enter\n"
          "the notes for that scale in a random key.\n"
          "\n"
          "\n"
          "\n"
          "Game instructions:\n"
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


welcome()
choose_scale()