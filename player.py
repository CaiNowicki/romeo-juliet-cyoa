"""Simple data model for the current player character.

This class centralizes all player state and behavior, which keeps the game loop
clean and makes saving/loading straightforward. As features grow (inventory,
relationships, flags, decision history), having a dedicated class prevents state
from scattering across unrelated functions.
"""

from dataclasses import dataclass, field


# dataclass auto-generates __init__, __repr__, and equality methods for data containers.
@dataclass
class PlayerCharacter:
  # Numeric id used to select character-specific scenes.
  character_id: int
  # Display name used in saves or UI text.
  name: str
  # Optional player-provided name for save files.
  save_name: str | None = None
  # Flexible flags for tracking decisions or conditions in the story.
  # Use default_factory to avoid shared mutable defaults across instances.
  flags: dict[str, bool] = field(default_factory=dict)
  # Track items the player collects over time.
  inventory: list[str] = field(default_factory=list)
  # Track relationship meters with other characters.
  relationships: dict[str, int] = field(default_factory=dict)
  # Record (scene_id, choice_index) for replay/debugging.
  decision_history: list[tuple[str, int]] = field(default_factory=list)

  def record_choice(self, scene_id, choice_index):
    self.decision_history.append((scene_id, choice_index))

  def add_item(self, item):
    if item not in self.inventory:
      self.inventory.append(item)

  def remove_item(self, item):
    if item in self.inventory:
      self.inventory.remove(item)

  def adjust_relationship(self, name, delta):
    self.relationships[name] = self.relationships.get(name, 0) + delta

  # @property makes this method accessible like a read-only attribute.
  @property
  def family(self):
    families = {
      1: "Capulet",
      2: "Montague",
      3: "Montague",
      4: "Capulet",
      5: "Capulet",
    }
    return families.get(self.character_id, "Unknown")

  # @property keeps these as computed, read-only booleans.
  @property
  def is_montague(self):
    return self.family == "Montague"

  # @property keeps these as computed, read-only booleans.
  @property
  def is_capulet(self):
    return self.family == "Capulet"

  def to_dict(self):
    return {
      "character_id": self.character_id,
      "name": self.name,
      "save_name": self.save_name,
      "flags": self.flags,
      "inventory": self.inventory,
      "relationships": self.relationships,
      "decision_history": self.decision_history,
    }

  # @classmethod receives the class (cls) instead of an instance; useful for alternate constructors.
  @classmethod
  def from_dict(cls, data):
    history = data.get("decision_history", [])
    normalized_history = [tuple(entry) for entry in history]
    return cls(
      data["character_id"],
      data["name"],
      data.get("save_name"),
      data.get("flags", {}),
      data.get("inventory", []),
      data.get("relationships", {}),
      normalized_history,
    )
