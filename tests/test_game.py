"""Instructor-level overview:

These tests focus on the game loop's decision logic, the IO boundaries, and save/load
behavior. The game is intentionally written with injectable input/output functions,
so tests can simulate user choices and capture printed text without touching real
stdin/stdout. This keeps tests deterministic and fast.

We choose these tests because they cover:
1) Branching logic (END vs. next scene).
2) Content resolution (placeholder text hooks).
3) Input validation and reprompting.
4) Scene display behavior and resolver usage.
5) Menu and start-scene selection flow.
6) Save/load correctness and error handling.
"""

import json
import os
import tempfile
import unittest

import content
import main
from player import PlayerCharacter


class TestGame(unittest.TestCase):
  # Each test uses small, in-memory scene dictionaries or temp directories
  # to isolate behavior and avoid dependencies on the real scene file.
  def test_apply_choice_end(self):
    # Verify END choices stop the game and move to the END scene id.
    scenes = {
      "scene1": {
        1: {
          "text": "Done.",
          "choices": [{"text": "End", "next": "END"}],
        }
      }
    }
    # Use a real PlayerCharacter to exercise id-based scene lookups.
    player_character = PlayerCharacter(1, "Juliet")
    game_over, next_scene = main.apply_choice(1, "scene1", player_character, scenes)
    self.assertTrue(game_over)
    self.assertEqual(next_scene, "END")

  def test_apply_choice_next(self):
    # Verify non-END choices advance to a new scene and continue play.
    scenes = {
      "scene1": {
        1: {
          "text": "Go.",
          "choices": [{"text": "Next", "next": "scene2"}],
        }
      }
    }
    # Use a real PlayerCharacter to exercise id-based scene lookups.
    player_character = PlayerCharacter(1, "Juliet")
    game_over, next_scene = main.apply_choice(1, "scene1", player_character, scenes)
    self.assertFalse(game_over)
    self.assertEqual(next_scene, "scene2")

  def test_resolve_scene_text_placeholder(self):
    # If a scene has no text, the resolver should produce a placeholder
    # that mentions the scene id and player id to aid content writing.
    scene_data = {"choices": []}
    player_character = PlayerCharacter(2, "Romeo")
    text = content.resolve_scene_text("missing_scene", player_character, scene_data)
    self.assertIn("missing_scene", text)
    self.assertIn("player=2", text)

  def test_get_int_choice_reprompts(self):
    # Simulate invalid input, out-of-range input, then a valid choice.
    # This demonstrates reprompting and input validation behavior.
    inputs = iter(["x", "3", "2"])
    outputs = []

    def input_func():
      # Simulate user input without touching real stdin.
      return next(inputs)

    def output_func(message):
      # Capture prompts for later assertions.
      outputs.append(message)

    choice = main.get_int_choice(2, input_func, output_func)
    self.assertEqual(choice, 2)
    self.assertTrue(any("Please enter a number between 1 and 2" in msg for msg in outputs))

  def test_show_scene_uses_resolver(self):
    # Provide empty text to force content resolution, then ensure the
    # resolver's output is printed instead of raw scene data.
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
    # Verify that choosing "Return to main menu" stops the new game flow
    # and does not call the gameplay loop.
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

  def test_save_game_writes_file(self):
    # Save to a temporary directory with a provided filename, then
    # assert the file contents match the expected schema.
    with tempfile.TemporaryDirectory() as temp_dir:
      player_character = PlayerCharacter(
        1,
        "Juliet",
        "slot1",
        flags={"vowed": True},
        inventory=["letter"],
        relationships={"Romeo": 2},
        decision_history=[("juliet_intro", 1)],
      )
      save_file = main.save_game(
        player_character,
        "juliet_intro",
        input_func=lambda: "ignored",
        output_func=lambda message: None,
        save_dir=temp_dir,
        filename="slot1",
      )
      self.assertIsNotNone(save_file)
      self.assertTrue(os.path.exists(save_file))
      with open(save_file, "r", encoding="utf-8") as handle:
        data = json.load(handle)
      self.assertEqual(data["current_scene"], "juliet_intro")
      self.assertEqual(data["player"]["character_id"], 1)
      self.assertEqual(data["player"]["name"], "Juliet")
      self.assertEqual(data["player"]["save_name"], "slot1")
      self.assertEqual(data["player"]["inventory"], ["letter"])
      self.assertEqual(data["player"]["relationships"]["Romeo"], 2)

  def test_save_game_cancelled_on_blank_name(self):
    # Blank filename should cancel the save and return None.
    with tempfile.TemporaryDirectory() as temp_dir:
      player_character = PlayerCharacter(1, "Juliet")
      result = main.save_game(
        player_character,
        "juliet_intro",
        input_func=lambda: "   ",
        output_func=lambda message: None,
        save_dir=temp_dir,
      )
      self.assertIsNone(result)

  def test_load_game_reads_file(self):
    # Load a known save file from a temporary directory and verify
    # the PlayerCharacter and current scene are reconstructed.
    with tempfile.TemporaryDirectory() as temp_dir:
      data = {
        "current_scene": "romeo_melancholy",
        "player": {
          "character_id": 2,
          "name": "Romeo",
          "save_name": "romeo_run",
          "flags": {"met_juliet": True},
          "inventory": ["mask"],
          "relationships": {"Juliet": 3},
          "decision_history": [["romeo_melancholy", 1]],
        },
      }
      save_path = os.path.join(temp_dir, "slot1.json")
      with open(save_path, "w", encoding="utf-8") as handle:
        json.dump(data, handle)

      player_character, current_scene = main.load_game(
        input_func=lambda: "1",
        output_func=lambda message: None,
        save_dir=temp_dir,
      )
      self.assertEqual(current_scene, "romeo_melancholy")
      self.assertEqual(player_character.character_id, 2)
      self.assertEqual(player_character.name, "Romeo")
      self.assertEqual(player_character.save_name, "romeo_run")
      self.assertTrue(player_character.flags["met_juliet"])
      self.assertEqual(player_character.inventory, ["mask"])
      self.assertEqual(player_character.relationships["Juliet"], 3)
      self.assertEqual(player_character.decision_history, [("romeo_melancholy", 1)])

  def test_load_game_no_saves(self):
    # Missing or empty saves directory should return None (no crash).
    with tempfile.TemporaryDirectory() as temp_dir:
      result = main.load_game(
        input_func=lambda: "1",
        output_func=lambda message: None,
        save_dir=os.path.join(temp_dir, "missing"),
      )
      self.assertIsNone(result)

      result = main.load_game(
        input_func=lambda: "1",
        output_func=lambda message: None,
        save_dir=temp_dir,
      )
      self.assertIsNone(result)

  def test_load_game_invalid_save(self):
    # Invalid saves should return None and not crash.
    with tempfile.TemporaryDirectory() as temp_dir:
      save_path = os.path.join(temp_dir, "slot1.json")
      with open(save_path, "w", encoding="utf-8") as handle:
        handle.write("{ not valid json")

      result = main.load_game(
        input_func=lambda: "1",
        output_func=lambda message: None,
        save_dir=temp_dir,
      )
      self.assertIsNone(result)

  def test_is_valid_save_missing_fields(self):
    # Missing required keys or wrong types should fail validation.
    self.assertFalse(main._is_valid_save(None))
    self.assertFalse(main._is_valid_save({}))
    self.assertFalse(main._is_valid_save({"player": {}}))
    self.assertFalse(main._is_valid_save({"current_scene": "x"}))
    self.assertFalse(main._is_valid_save({"player": "nope", "current_scene": "x"}))
    self.assertFalse(main._is_valid_save({"player": {"character_id": 1}, "current_scene": "x"}))
    self.assertFalse(main._is_valid_save({"player": {"name": "Juliet"}, "current_scene": "x"}))

  def test_show_ending_uses_random_variant(self):
    # Ensure show_ending prints the randomly selected ending text and waits for exit.
    outputs = []

    def output_func(message):
      outputs.append(message)

    def input_func():
      return "1"

    def fake_choice(items):
      return items[0]

    original_choice = main.random.choice
    try:
      main.random.choice = fake_choice
      main.show_ending(
        input_func,
        output_func,
        scenes={
          "END": {
            1: {"text": "Ending one.", "choices": []},
            2: {"text": "Ending two.", "choices": []},
          }
        },
      )
    finally:
      main.random.choice = original_choice

    self.assertTrue(any(msg == "Ending one." for msg in outputs))

  def test_show_ending_fallback_when_missing(self):
    # If no END variants exist, show a generic ending message.
    outputs = []

    def output_func(message):
      outputs.append(message)

    main.show_ending(
      input_func=lambda: "1",
      output_func=output_func,
      scenes={"END": {}},
    )

    self.assertTrue(any("Sorry, that ends the game!" in msg for msg in outputs))

  def test_main_gameplay_loop_calls_show_ending(self):
    # Full-loop test: reaching END should trigger show_ending before exit.
    calls = {"ending_called": False}

    def fake_show_ending(input_func, output_func, scenes=main.SCENES):
      calls["ending_called"] = True

    def fake_end_game(output_func=print, exit_func=print):
      # Replace hard exit with a no-op for testing.
      pass

    def fake_show_scene(scene_id, player_character, input_func=input, output_func=print, scenes=main.SCENES, content_resolver=None):
      # Always return the first choice.
      return 1

    def fake_apply_choice(player_choice, scene_id, player_character, scenes=main.SCENES):
      # Force the loop to end by returning END.
      return True, "END"

    player_character = PlayerCharacter(1, "Juliet")

    original_show_ending = main.show_ending
    original_end_game = main.end_game
    original_show_scene = main.show_scene
    original_apply_choice = main.apply_choice
    try:
      main.show_ending = fake_show_ending
      main.end_game = fake_end_game
      main.show_scene = fake_show_scene
      main.apply_choice = fake_apply_choice
      main.main_gameplay_loop("start", player_character, input_func=lambda: "1", output_func=lambda message: None)
    finally:
      main.show_ending = original_show_ending
      main.end_game = original_end_game
      main.show_scene = original_show_scene
      main.apply_choice = original_apply_choice

    self.assertTrue(calls["ending_called"])


if __name__ == "__main__":
  # Allow running this file directly for quick local checks.
  unittest.main()
