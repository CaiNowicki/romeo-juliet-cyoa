import sys
from scenes import SCENES, START_SCENES

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
    choice = get_int_choice(3)
    match choice:
      case 1:
        new_game_flow()
      case 2:
        load_game_flow()
      case 3:
        end_game()

def get_int_choice(limit):
  """ this function gets the user choice and ensures it is a valid integer selection"""
  while True:
    print("What do you choose?")
    try:
      choice = int(input())
      if 0 < choice <= limit:
        return choice
      else:
        print(f"Please enter a number between 1 and {limit}")
        continue
    except ValueError:
      print(f"Please enter a number between 1 and {limit}.")
      continue




def new_game_flow():
  """ this function creates a new game """
  player_character = character_select_menu()
  # player character determines starting scene
  current_scene = start_scene_select(player_character)
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
  choice = get_int_choice(6)
  return choice

def start_scene_select(player_character):
  # select the first scene based on player character choice
  return START_SCENES[player_character]

def main_gameplay_loop(scene_id, player_character):
  game_over_flag = False
  while not game_over_flag:
    try:
      player_choice = show_scene(scene_id, player_character)
      game_over_flag, scene_id = apply_choice(player_choice, scene_id, player_character)
    except KeyError:
      print("Sorry, that scene isn't written yet.")
      end_game()
  # add logic here to check ENDINGS for the player_choice & scene_id combo
  print("Sorry, that ends the game!")
  end_game()

def apply_choice(player_choice, scene_id, player_character):
  """ this function contains the logic for applying the player choices to the game state """
  # take in player choice and specific scene
  # determine where choice takes player next
  # return new scene and set game_over_flag to T/F as appropriate
  choice = SCENES[scene_id][player_character]["choices"][player_choice-1]
  if choice["next"] == "END":
    return True, scene_id
  return False, choice["next"]


def show_scene(scene_id, player_character):
  """ this function fetches the appropriate scene from the resources file and gets the user choice for the next scene """
  scene_data = SCENES[scene_id][player_character]
  print(scene_data["text"])
  choices = scene_data['choices']
  for i, choice in enumerate(choices, start=1):
    print(f"{i}. {choice["text"]}")
  user_choice = get_int_choice(len(choices))
  return user_choice

def end_game():
  """ this function ends the game """
  print("See you next time!")
  sys.exit()


if __name__ == "__main__":
  # this function calls the main function when the script is run
  main()


# also acceptable to skip function definitions, but the "main guard" is considered best practice
