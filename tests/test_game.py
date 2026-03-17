import unittest

import content
import main
from player import PlayerCharacter


class TestGame(unittest.TestCase):
  def test_apply_choice_end(self):
    scenes = {
      "scene1": {
        1: {
          "text": "Done.",
          "choices": [{"text": "End", "next": "END"}],
        }
      }
    }
    player_character = PlayerCharacter(1, "Juliet")
    game_over, next_scene = main.apply_choice(1, "scene1", player_character, scenes)
    self.assertTrue(game_over)
    self.assertEqual(next_scene, "scene1")

  def test_apply_choice_next(self):
    scenes = {
      "scene1": {
        1: {
          "text": "Go.",
          "choices": [{"text": "Next", "next": "scene2"}],
        }
      }
    }
    player_character = PlayerCharacter(1, "Juliet")
    game_over, next_scene = main.apply_choice(1, "scene1", player_character, scenes)
    self.assertFalse(game_over)
    self.assertEqual(next_scene, "scene2")

  def test_resolve_scene_text_placeholder(self):
    scene_data = {"choices": []}
    player_character = PlayerCharacter(2, "Romeo")
    text = content.resolve_scene_text("missing_scene", player_character, scene_data)
    self.assertIn("missing_scene", text)
    self.assertIn("player=2", text)

  def test_get_int_choice_reprompts(self):
    inputs = iter(["x", "3", "2"])
    outputs = []

    def input_func():
      return next(inputs)

    def output_func(message):
      outputs.append(message)

    choice = main.get_int_choice(2, input_func, output_func)
    self.assertEqual(choice, 2)
    self.assertTrue(any("Please enter a number between 1 and 2" in msg for msg in outputs))

  def test_show_scene_uses_resolver(self):
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
      return "1"

    def output_func(message):
      outputs.append(message)

    def resolver(scene_id, player_character, scene_data):
      return "RESOLVED"

    player_character = PlayerCharacter(1, "Juliet")
    choice = main.show_scene("scene1", player_character, input_func, output_func, scenes, resolver)
    self.assertEqual(choice, 1)
    self.assertEqual(outputs[0], "RESOLVED")

  def test_new_game_flow_return_to_menu(self):
    calls = {"called": False}

    def input_func():
      return "6"

    def output_func(message):
      pass

    def fake_main_gameplay_loop(scene_id, player_character, input_func=input, output_func=print):
      calls["called"] = True

    original_main_gameplay_loop = main.main_gameplay_loop
    try:
      main.main_gameplay_loop = fake_main_gameplay_loop
      main.new_game_flow(input_func, output_func)
    finally:
      main.main_gameplay_loop = original_main_gameplay_loop

    self.assertFalse(calls["called"])

  def test_start_scene_select_uses_character_id(self):
    player_character = PlayerCharacter(3, "Mercutio")
    start_scenes = {3: "scene_start"}
    scene_id = main.start_scene_select(player_character, start_scenes)
    self.assertEqual(scene_id, "scene_start")


if __name__ == "__main__":
  unittest.main()
