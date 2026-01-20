def main():
    # this is the main function of the program
    # everything runs from here
    print("Romeo & Juliet: A Choose-Your-Own-Adventure")
    print("This game will allow players to make choices that affect how the story unfolds.")
    print("Future versions will include branching paths, tracked decisions, and multiple endings.")

# Example variable assignments with explanation for data types
save_file_exists = False  # is there a save file? true/false answers can be booleans
# TODO: add save_file_check functionality to return true/false on the existence of a save file

romeo = dict()  # creating a variable to hold Romeo's status
# dictionary is like a table of key:value pairs.
juliet = dict()
# TODO: add characteristics as keys to character dictionaries

love_score = 0  # integer value representing how much Romeo and Juliet love each other
# initialized at 0 for a new game because they don't know each other yet

romeo_inventory = ["mask"]
juliet_inventory = []
# list variable for character inventories
# list of strings stores items as string value for each character


# Example of pseudocode conditional
# Hint: press ctrl+/ to comment or uncomment a block of code/pseudocode after it is written
# it may look more-or-less like code but won't run (yet)
# def(win_state)
# """ this function determines the win state of the game and runs the end_game function with the correct state """
# if romeo["has_dagger"] = true AND juliet["drank_poison"] = true:
#     print Romeo stabbed himself. Juliet is dead.
#     game_over(lose)
#
# else if juliet["drank_poison"] = false:
#   if love_score > 90:
#     print They kiss! They get married and run away together to live happily ever after!
#     game_over(win)
# TODO: create game_over function to mark save file as complete and close program



if __name__ == "__main__":
    # this function calls the main function when the script is run
    # this will work with whatever name you give the function
    main()

# also acceptable to skip function definitions, but the "main guard" is considered best practice

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

