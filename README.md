# romeo-juliet-cyoa
# Romeo &amp; Juliet: A Text-Based Choose-Your-Own-Adventure 

## Overview
This project is a text-based, command-line choose-your-own-adventure (CYOA) game based on key decision points in Shakespeare’s *Romeo and Juliet*. The player will make choices as different characters, which will affect how the story unfolds.

## Project Goals
The goal of this project is to explore how branching narratives can be modeled using variables and conditional logic in Python.

## Planned Features
- Player choices that branch the story at key moments
- Tracking player decisions that affect later outcomes
- Multiple possible endings based on choices
- Clear separation between story content and game logic
- Ability to restart or replay the game

## Tools
- Python 3.12
- PyCharm IDE
- GitHub for version control


## Current Status and Plans
- Minimal runnable script exists and executes successfully
- Core variables and data structures are defined
- Conditional logic is planned but not fully implemented

This project is in an early planning phase. 
The focus at this time is scaffolding the project and mapping out the initial program logic. 

The game will rely on conditional logic to determine story progression and endings.

(NOTE: you need to provide only one of the mapping types - pseudocode OR descriptive)

Example of descriptive conditional
choice: load a new game or open a save file
does save file exist? yes -> load save file, no -> start new game
Functionality to implement: ability to start a new game, create a game save file, and load a save file



## Data Model and State

The program will track game state using a combination of variables representing characters, progress, and player decisions.

### Boolean Values
- `save_file_exists` (`bool`)  
  Tracks whether a saved game file exists. Boolean values are appropriate here because the answer is strictly yes/no and will be used to control branching logic at program start.

### Numeric Values
- `love_score` (`int`)  
  Represents the relationship strength between Romeo and Juliet. This value will change over time based on player decisions and will influence story outcomes.

### Structured Data
- `romeo` and `juliet` (`dict`)  
  Dictionaries are used to store character-specific state such as items, flags, and story-related attributes. This allows character data to grow flexibly as new features are added.

### Collections
- `romeo_inventory` and `juliet_inventory` (`list[str]`)  
  Lists are used to track items held by each character. Lists allow items to be added or removed as the story progresses.


