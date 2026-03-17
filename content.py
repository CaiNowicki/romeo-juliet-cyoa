def resolve_scene_text(scene_id, player_character, scene_data):
  """Return scene text or a placeholder hook for future content generation."""
  text = scene_data.get("text", "").strip()
  if text:
    return text
  return generate_placeholder_text(scene_id, player_character)


def generate_placeholder_text(scene_id, player_character):
  player_id = getattr(player_character, "character_id", player_character)
  return f"[TODO] Write scene text for scene_id={scene_id}, player={player_id}."


def generate_scene_text(scene_id, player_character, context=None):
  """Hook for later story generation (LLM or templating)."""
  return generate_placeholder_text(scene_id, player_character)
