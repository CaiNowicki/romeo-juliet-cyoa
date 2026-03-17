"""Simple data model for the current player character.

We keep this as a small dataclass so it's easy to read and extend
with new fields (inventory, relationship meters, decision history, etc.).
"""

from dataclasses import dataclass, field


@dataclass
class PlayerCharacter:
  # Numeric id used to select character-specific scenes.
  character_id: int
  # Display name used in saves or UI text.
  name: str
  # Flexible flags for tracking decisions or conditions in the story.
  flags: dict[str, bool] = field(default_factory=dict)
