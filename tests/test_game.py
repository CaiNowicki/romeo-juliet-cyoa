import unittest

import content
import main
from player import PlayerCharacter


class TestGame(unittest.TestCase):
  def test_apply_choice_end(self):
    # Minimal scene data for an "END" terminal choice.
    scenes = {
      "scene1": {
        1: {
          "text": "Done.",
          "choices": [{"text": "End", "next": "END"}],
        }
      }
    }
    # Use a real PlayerCharacter to exercise id-based lookups.
    player_character = PlayerCharacter(1, "Juliet")
    # Choosing option 1 should end the game and keep the same scene id.
    game_over, next_scene = main.apply_choice(1, "scene1", player_character, scenes)
    self.assertTrue(game_over)
    self.assertEqual(next_scene, "scene1")

  def test_apply_choice_next(self):
    # Minimal scene data for a non-terminal transition.
    scenes = {
      "scene1": {
        1: {
          "text": "Go.",
          "choices": [{"text": "Next", "next": "scene2"}],
        }
      }
    }
    # Use a real PlayerCharacter to exercise id-based lookups.
    player_character = PlayerCharacter(1, "Juliet")
    # Choosing option 1 should advance to a new scene without ending the game.
    game_over, next_scene = main.apply_choice(1, "scene1", player_character, scenes)
    self.assertFalse(game_over)
    self.assertEqual(next_scene, "scene2")

  def test_resolve_scene_text_placeholder(self):
    # Missing "text" should fall back to a placeholder that includes scene + player id.
    scene_data = {"choices": []}
    player_character = PlayerCharacter(2, "Romeo")
    text = content.resolve_scene_text("missing_scene", player_character, scene_data)
    self.assertIn("missing_scene", text)
    self.assertIn("player=2", text)

  def test_get_int_choice_reprompts(self):
    # Feed invalid input, then out-of-range, then a valid choice.
    inputs = iter(["x", "3", "2"])
    outputs = []

    def input_func():
      # Simulate user input without touching stdin.
      return next(inputs)

    def output_func(message):
      # Capture prompts for later assertions.
      outputs.append(message)

    choice = main.get_int_choice(2, input_func, output_func)
    self.assertEqual(choice, 2)
    self.assertTrue(any("Please enter a number between 1 and 2" in msg for msg in outputs))

  def test_show_scene_uses_resolver(self):
    # Provide empty text to force content resolution.
    scenes = {
      "scene1": {
        1: {
          "text": "",
          "choices": [{"text": "Next", "next": "END"}],
        }
      }
    }
    outputs = []

    def input_func():
      # Always choose the first option.
      return "1"

    def output_func(message):
      # Capture output to verify resolver output is printed.
      outputs.append(message)

    def resolver(scene_id, player_character, scene_data):
      # Custom resolver to prove it's used over raw scene text.
      return "RESOLVED"

    player_character = PlayerCharacter(1, "Juliet")
    choice = main.show_scene("scene1", player_character, input_func, output_func, scenes, resolver)
    self.assertEqual(choice, 1)
    self.assertEqual(outputs[0], "RESOLVED")

  def test_new_game_flow_return_to_menu(self):
    # Track whether main_gameplay_loop is invoked.
    calls = {"called": False}

    def input_func():
      # Choose "Return to main menu".
      return "6"

    def output_func(message):
      # Ignore output for this test.
      pass

    def fake_main_gameplay_loop(scene_id, player_character, input_func=input, output_func=print):
      # Mark if gameplay ever starts (it should not).
      calls["called"] = True

    original_main_gameplay_loop = main.main_gameplay_loop
    try:
      # Patch the gameplay loop to observe calls without running it.
      main.main_gameplay_loop = fake_main_gameplay_loop
      main.new_game_flow(input_func, output_func)
    finally:
      # Always restore the original function to avoid test leakage.
      main.main_gameplay_loop = original_main_gameplay_loop

    # Returning to menu should prevent gameplay from starting.
    self.assertFalse(calls["called"])

  def test_start_scene_select_uses_character_id(self):
    # Ensure the character id is used as the scene map key.
    player_character = PlayerCharacter(3, "Mercutio")
    start_scenes = {3: "scene_start"}
    scene_id = main.start_scene_select(player_character, start_scenes)
    self.assertEqual(scene_id, "scene_start")


if __name__ == "__main__":
  # Allow running this file directly for quick local checks.
  unittest.main()
