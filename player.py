from dataclasses import dataclass, field


@dataclass
class PlayerCharacter:
  character_id: int
  name: str
  flags: dict[str, bool] = field(default_factory=dict)
