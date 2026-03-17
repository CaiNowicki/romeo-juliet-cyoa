"""Instructor-level overview:

This module contains the main gameplay flow for the CLI CYOA. It is structured so
that input/output can be injected, which keeps the code testable and makes it easy
to swap the UI later (GUI/web) without rewriting core logic.
"""

import json
import random
import sys
from pathlib import Path

from scenes import SCENES, START_SCENES
from content import resolve_scene_text
from player import PlayerCharacter

# Sentinel used by the scene menu to request a save+exit.
SAVE_AND_EXIT = "__SAVE_EXIT__"

def main(input_func=input, output_func=print):
  # Inject input/output for unit tests or alternate UIs.
  # This keeps the "engine" independent of real stdin/stdout.
  # This is the main function of the program; everything runs from here.
  # Print title and intro.
  title(output_func)
  # Display main menu.
  main_menu_loop(input_func, output_func)
  # Run main gameplay loop.


def title(output_func=print):
  # Simple title card; split into a function so it can be reused or skipped in tests.
  output_func("Romeo & Juliet: A Choose-Your-Own-Adventure")
  output_func("Welcome to Romeo & Juliet like you've never seen it before!")
  output_func("This game will allow players to make choices that affect how the story unfolds.")
  output_func("Future versions will include branching paths, tracked decisions, and multiple endings.")
  output_func("You can start a new game or load a saved game")

def load_game(input_func=input, output_func=print, save_dir="saves"):
  """ loads the game from the game folder """
  # Locate save files, let the player pick one, then validate and deserialize.
  save_path = Path(save_dir)
  if not save_path.exists() or not save_path.is_dir():
    output_func("No saved games found.")
    return None
  save_files = sorted(save_path.glob("*.json"))
  if not save_files:
    output_func("No saved games found.")
    return None
  output_func("Select a saved game:")
  for i, save_file in enumerate(save_files, start=1):
    output_func(f"{i}. {save_file.name}")
  selection = get_int_choice(len(save_files), input_func, output_func)
  chosen = save_files[selection - 1]
  try:
    with chosen.open("r", encoding="utf-8") as handle:
      data = json.load(handle)
  except (OSError, json.JSONDecodeError):
    output_func("That save file could not be loaded.")
    return None
  if not _is_valid_save(data):
    output_func("That save file is missing required data.")
    return None
  # Rebuild a PlayerCharacter so the rest of the engine can proceed normally.
  player_character = PlayerCharacter.from_dict(data["player"])
  return player_character, data["current_scene"]


def _is_valid_save(data):
  # Minimal validation to avoid KeyErrors when loading user files.
  if not isinstance(data, dict):
    return False
  if "player" not in data or "current_scene" not in data:
    return False
  player = data["player"]
  if not isinstance(player, dict):
    return False
  if "character_id" not in player or "name" not in player:
    return False
  return True

def save_game(player_character, current_scene, input_func=input, output_func=print, save_dir="saves", filename=None):
  """ saves the game to the game folder """
  # Convert current state into a JSON file on disk.
  save_path = Path(save_dir)
  save_path.mkdir(parents=True, exist_ok=True)
  if not filename and player_character.save_name:
    filename = player_character.save_name
  if not filename:
    output_func("Enter a name for your save:")
    filename = input_func().strip()
  if not filename:
    output_func("Save cancelled.")
    return None
  if not filename.lower().endswith(".json"):
    filename = f"{filename}.json"
  # Keep the schema small and explicit for teaching and debugging.
  data = {
    "current_scene": current_scene,
    "player": player_character.to_dict(),
  }
  save_file = save_path / filename
  try:
    with save_file.open("w", encoding="utf-8") as handle:
      json.dump(data, handle, indent=2)
  except OSError:
    output_func("Save failed.")
    return None
  output_func(f"Saved game to {save_file.name}")
  return save_file

def main_menu_loop(input_func=input, output_func=print):
  """ main menu """
  while True:
    # Main menu is a simple loop so returning here is easy.
    output_func("1. New game")
    output_func("2. Load a saved game")
    output_func("3. Exit")
    choice = get_int_choice(3, input_func, output_func)
    match choice:
      case 1:
        new_game_flow(input_func, output_func)
      case 2:
        load_game_flow(input_func, output_func)
      case 3:
        end_game(output_func)

def get_int_choice(limit, input_func=input, output_func=print):
  """ this function gets the user choice and ensures it is a valid integer selection"""
  # Loop until the user provides a valid integer within the given range.
  while True:
    output_func("What do you choose?")
    try:
      choice = int(input_func())
      if 0 < choice <= limit:
        return choice
      else:
        output_func(f"Please enter a number between 1 and {limit}")
        continue
    except ValueError:
      output_func(f"Please enter a number between 1 and {limit}.")
      continue


def new_game_flow(input_func=input, output_func=print):
  """ this function creates a new game """
  # The character menu returns None if the player backs out.
  player_character = character_select_menu(input_func, output_func)
  if player_character is None:
    return
  output_func("Name your save file:")
  while True:
    save_name = input_func().strip()
    if save_name:
      break
    output_func("Please enter a non-empty name.")
  player_character.save_name = save_name
  # Player character determines starting scene.
  current_scene = start_scene_select(player_character)
  save_game(player_character, current_scene, input_func, output_func, filename=save_name)
  main_gameplay_loop(current_scene, player_character, input_func, output_func)

def load_game_flow(input_func=input, output_func=print):
  """ once game is loaded, function runs game from current state """
  # Returns None if no save is selected or the file is invalid.
  load_result = load_game(input_func, output_func)
  if load_result is None:
    return
  player_character, current_scene = load_result
  main_gameplay_loop(current_scene, player_character, input_func, output_func)

def character_select_menu(input_func=input, output_func=print):
  """ player character selection menu """
  # Small menu for choosing a character; returning None cancels.
  output_func("Please choose a character:")
  output_func("1. Juliet")
  output_func("2. Romeo")
  output_func("3. Mercutio")
  output_func("4. Tybalt")
  output_func("5. Paris")
  output_func("6. Return to main menu")
  choice = get_int_choice(6, input_func, output_func)
  if choice == 6:
    return None
  # Map choice numbers to names for clarity and to avoid magic numbers elsewhere.
  character_names = {
    1: "Juliet",
    2: "Romeo",
    3: "Mercutio",
    4: "Tybalt",
    5: "Paris",
  }
  return PlayerCharacter(choice, character_names[choice])

def start_scene_select(player_character, start_scenes=START_SCENES):
  # Use the character's id to pick the correct starting scene.
  # select the first scene based on player character choice
  return start_scenes[player_character.character_id]

def main_gameplay_loop(scene_id, player_character, input_func=input, output_func=print):
  # Core scene loop: show scene, apply choice, repeat until END or save/exit.
  game_over_flag = False
  while not game_over_flag:
    try:
      player_choice = show_scene(scene_id, player_character, input_func, output_func)
      if player_choice == SAVE_AND_EXIT:
        # Save the game and exit immediately.
        save_game(player_character, scene_id, input_func, output_func)
        end_game(output_func)
      # Store a running history of choices for replay/debugging.
      player_character.record_choice(scene_id, player_choice)
      game_over_flag, scene_id = apply_choice(player_choice, scene_id, player_character)
      autosave(player_character, scene_id, output_func=output_func)
    except KeyError:
      output_func("Sorry, that scene isn't written yet.")
      end_game(output_func)
  # Show a randomized ending scene before exiting.
  show_ending(input_func, output_func)
  end_game(output_func)

def apply_choice(player_choice, scene_id, player_character, scenes=SCENES):
  """ this function contains the logic for applying the player choices to the game state """
  # take in player choice and specific scene
  # determine where choice takes player next
  # return new scene and set game_over_flag to T/F as appropriate
  choice = scenes[scene_id][player_character.character_id]["choices"][player_choice - 1]
  if choice["next"] == "END":
    return True, "END"
  return False, choice["next"]


def show_scene(scene_id, player_character, input_func=input, output_func=print, scenes=SCENES, content_resolver=resolve_scene_text):
  """ this function fetches the appropriate scene from the resources file and gets the user choice for the next scene """
  # Resolve and print scene text, then list choices plus a "save and exit" option.
  scene_data = scenes[scene_id][player_character.character_id]
  output_func(content_resolver(scene_id, player_character, scene_data))
  choices = scene_data['choices']
  for i, choice in enumerate(choices, start=1):
    output_func(f"{i}. {choice['text']}")
  output_func(f"{len(choices) + 1}. Save and exit")
  user_choice = get_int_choice(len(choices) + 1, input_func, output_func)
  if user_choice == len(choices) + 1:
    return SAVE_AND_EXIT
  return user_choice

def show_ending(input_func=input, output_func=print, scenes=SCENES):
  """ show a random ending scene and wait for a final acknowledgement """
  end_variants = scenes.get("END", {})
  if not end_variants:
    output_func("Sorry, that ends the game!")
    return
  ending_scene = random.choice(list(end_variants.values()))
  output_func(ending_scene.get("text", "Sorry, that ends the game!"))
  output_func("1. Exit")
  get_int_choice(1, input_func, output_func)

def autosave(player_character, current_scene, output_func=print):
  if not player_character.save_name:
    return
  autosave_name = f"{player_character.save_name}_autosave"
  save_game(player_character, current_scene, output_func=output_func, filename=autosave_name)

def end_game(output_func=print, exit_func=sys.exit):
  """ this function ends the game """
  # Centralized exit so tests can stub out sys.exit if needed.
  output_func("See you next time!")
  exit_func()


if __name__ == "__main__":
  # this function calls the main function when the script is run
  main()


# also acceptable to skip function definitions, but the "main guard" is considered best practice
