# class Game
#   attributes:
#   player_character
#   current_scene
#   game_over_flag
#   scenes (SceneLibrary)
#   characters (CharacterLibrary)
#
#   methods:
#   run():
#   title()
#   main_menu_loop()
#
#   title():
#   print intro text
#
#   main_menu_loop():
#   while True:
#     show menu
#     choice = get menu input
#     if choice == "NEW GAME": new_game_flow()
#     if choice == "LOAD_GAME": load_game_flow()
#     if choice == "EXIT": exit()
#
#   new_game_flow():
#   player_character_choice = character_select_menu()
#   if player_character_choice == "RETURN TO MENU": return
#   player_character = characters.create(player_character_choice)
#   current_scene = player_character.start_scene
#
#   load_game_flow():
#   fill in later
#
#   character_select_menu():
#   show character list
#   return character_choice
#
#   main_gameplay_loop():
#   game_over_flag = False
#   while not game_over_flag:
#     player_choice = show_scene()
#     game_over_flag, current_scene = apply_choice(player_choice)
#
#   show_scene():
#   scene = scenes.get(current_scene, player_character)
#   display scene text
#   display choices
#   return player_choice
#
#   apply_choice(player_choice):
#   determine next scene
#   if next_scene == "END": return True, current_scene
#   else: return False, next_scene
#
#
# class SceneLibrary:
#   attributes:
#   scenes (nested by scene_id -> character_id)
#
#   methods:
#
#   get(scene_id):
#   return scene_object
#
# class Scene:
#   attributes:
#   scene_id
#   text
#   choices (list of class Choice instances)
#
# class Choice:
#     attributes:
#     text
#     next_scene
#
# class PlayerCharacter:
#   attributes:
#   id
#   name
#   inventory
#   start_scene
#
