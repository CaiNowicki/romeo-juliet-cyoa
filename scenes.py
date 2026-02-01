SCENES = {
  "scene_1": {
    1: {  # Juliet
      "text": "You step onto the balcony, the night air cool.",
      "choices": [
        {"text": "Look out into the street", "next": "scene_2"},
        {"text": "Return inside", "next": "END"}
      ]
    },
    2: {  # Romeo
      "text": "You hide in the orchard shadows, heart pounding.",
      "choices": [
        {"text": "Call up to the balcony", "next": "scene_2"},
        {"text": "Slip away quietly", "next": "END"}
      ]
    },
    3: {  # Mercutio
      "text": "You arrive with a grin, sword at your side.",
      "choices": [
        {"text": "Joke with friends", "next": "END"},
        {"text": "Head inside", "next": "scene_2"}
      ]
    },
    4: {  # Tybalt
      "text": "You sense the Capulets are watching.",
      "choices": [
        {"text": "Confront them", "next": "END"},
        {"text": "Stay cautious", "next": "scene_2"}
      ]
    },
    5: {  # Paris
      "text": "You consider your duty and your heart.",
      "choices": [
        {"text": "Seek Juliet", "next": "scene_2"},
        {"text": "Speak to her father", "next": "END"}
      ]
    }
  }
}

START_SCENES = { # characters have different start scenes but right now they're all the same
    1: "scene_1",
    2: "scene_1",
    3: "scene_1",
    4: "scene_1",
    5: "scene_1",
}