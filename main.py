def main():
  # this is the main function of the program
  # everything runs from here
  # print title and intro
  title()
  # display main menu
  main_menu_loop()
  # run main gameplay loop


def title():
  print("Romeo & Juliet: A Choose-Your-Own-Adventure")
  print("Welcome to Romeo & Juliet like you've never seen it before!")
  print("This game will allow players to make choices that affect how the story unfolds.")
  print("Future versions will include branching paths, tracked decisions, and multiple endings.")
  print("You can start a new game or load a saved game")

def load_game():
  """ loads the game from the game folder """
  # check if saved games folder contains a save file
  # open save file and check file integrity
  # load in game state from file
  # start game from appropriate point
  pass

def save_game():
  """ saves the game to the game folder """
  # converts game state to saveable format (CSV or JSON?)
  # saves file locally
  pass

def main_menu_loop():
  """ main menu """
  while True:
    print("1. New game")
    print("2. Load a saved game")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
      case 1:
        new_game_flow()
      case 2:
        load_game_flow()
      case 3:
        break
        # quit program

def new_game_flow():
  """ this function creates a new game """
  player_character = character_select_menu()
  # player character determines starting scene
  current_scene = start_scene_select()
  main_gameplay_loop(current_scene, player_character)

def load_game_flow():
  """ once game is loaded, function runs game from current state """
  # player_character = loaded_file.player_character
  # current_scene = loaded_file.current_scene
  # main_gameplay_loop(current_scene, player_character)
  pass

def character_select_menu():
  """ player character selection menu """
  print("Please choose a character:")
  print("1. Juliet")
  print("2. Romeo")
  print("3. Mercutio")
  print("4. Tybalt")
  print("5. Paris")
  print("6. Return to main menu")
  choice = int(input("Enter your choice: "))
  # error handling for choice goes here
  return choice

def start_scene_select():
  # select the first scene based on player character choice
  pass

def main_gameplay_loop(scene, player_character, game_over_flag):
  game_over_flag = False
  while not game_over_flag:
    player_choice = show_scene(scene, player_character)
    game_over_flag, scene = apply_choice(player_choice, scene)

def apply_choice(player_choice, scene):
  """ this function contains the logic for applying the player choices to the game state """
  # take in player choice and specific scene
  # determine where choice takes player next
  # return new scene and set game_over_flag to T/F as appropriate
  pass


def show_scene(scene, player_character):
  """ this function fetches the appropriate scene from the resources file """
  # load the correct scene file
  # find player character viewpoint in file
  # display appropriate scene and dialogue
  # display player choices from resource file
  # take in user choice
  # pull next scene identifier from resource file

if __name__ == "__main__":
  # this function calls the main function when the script is run
  main()


# also acceptable to skip function definitions, but the "main guard" is considered best practice
