SCENES = {
    # --- JULIET'S FIRST SCENE (Act 1, Scene 3) ---
    "juliet_intro": {
        1: {  # Juliet (ID: 1)
            "text": "Your mother and the Nurse press you about marriage to Paris. Lady Capulet watches expectantly: *'What say you to my suit?'* The Nurse chuckles, *'An honor!'* But your stomach twists. This isn’t your choice.",
            "choices": [
                {
                    "text": "Agree to consider Paris (for now).",
                    "next": "capulet_ball_prep"  # Proceeds to ball prep
                },
                {
                    "text": "Refuse outright: *'I will not marry yet.'*",
                    "next": "juliet_rebellion"   # Triggers family conflict
                }
            ]
        }
    },

    # --- ROMEO'S FIRST SCENE (Act 1, Scene 1) ---
    "romeo_melancholy": {
        2: {  # Romeo (ID: 2)
            "text": "You mope in the sycamore grove, pining for Rosaline. Benvolio teases you: *'Forget her! Come to the Capulets’ ball—compare her to others.'* Mercutio’s laughter grates. Do you cling to sorrow or seek distraction?",
            "choices": [
                {
                    "text": "Go to the ball (what’s the worst that could happen?).",
                    "next": "capulet_ball_entry"
                },
                {
                    "text": "Storm off alone. *'Love is a smoke raised with the fume of sighs.'*",
                    "next": "romeo_solitary"    # Misses Juliet; focuses on Rosaline
                }
            ]
        }
    },

    # --- MERCUTIO'S FIRST SCENE (Act 1, Scene 1) ---
    "mercutio_taunts": {
        3: {  # Mercutio (ID: 3)
            "text": "Romeo’s lovesick whining is insufferable. *'You are a lover! Borrow Cupid’s wings and soar with them above common bound.'* You could mock him further—or drag him to the Capulet ball for sport.",
            "choices": [
                {
                    "text": "Goad Romeo into attending the ball.",
                    "next": "capulet_ball_entry"
                },
                {
                    "text": "Ditch Romeo. Seek trouble with Tybalt instead.",
                    "next": "mercutio_provokes_tybalt"
                }
            ]
        }
    },

    # --- TYBALT'S FIRST SCENE (Act 1, Scene 1) ---
    "tybalt_fury": {
        4: {  # Tybalt (ID: 4)
            "text": "Montagues in the street? Your hand flies to your sword. *'What, drawn and talk of peace? I hate the word.'* The fools don’t even flinch. Do you strike first or bide your time?",
            "choices": [
                {
                    "text": "Draw steel. *'Turn thee, Benvolio! Look upon thy death.'*",
                    "next": "street_brawl"      # Escalates feud early
                },
                {
                    "text": "Hold back—for now. *'I will withdraw, but this intrusion shall / Now seem sweet, convert to bitterest gall.'*",
                    "next": "capulet_ball_cautious"  # Attends ball, watches Romeo
                }
            ]
        }
    },

    # --- PARIS'S FIRST SCENE (Act 1, Scene 2) ---
    "paris_proposal": {
        5: {  # Paris (ID: 5)
            "text": "Lord Capulet hesitates: *'My child is yet a stranger in the world.'* But you’re patient. *'Younger than she are happy mothers made.'* Press the advantage or respect his caution?",
            "choices": [
                {
                    "text": "Insist: *'She’s old enough. Let me woo her tonight at the ball.'*",
                    "next": "capulet_ball_pursuit"
                },
                {
                    "text": "Withdraw gracefully. *'I’ll wait—but time is fleeting.'*",
                    "next": "paris_patience"     # Delays Juliet’s hand
                }
            ]
        }
    },

    # --- SHARED SCENES (Branching Points) ---
    "capulet_ball_prep": {
        1: {  # Juliet
            "text": "The Nurse fussing over your gown is suffocating. *'Wear this, no, this!’* You catch your reflection—a stranger. Do you play the part or rebel?",
            "choices": [
                {"text": "Submit. Let them dress you for Paris.", "next": "ball_paris_focus"},
                {"text": "Sneak a dagger into your sleeve.", "next": "ball_juliet_defiant"}
            ]
        },
        2: {  # Romeo
            "text": "The Capulet hall buzzes with laughter. Masked, you scan the crowd—then see *her*. Juliet, radiant. But Tybalt’s glare burns from across the room.",
            "choices": [
                {"text": "Approach Juliet.", "next": "first_kiss"},
                {"text": "Avoid her. This is madness.", "next": "romeo_retreat"}
            ]
        }
    },

}

START_SCENES = {
    1: "juliet_intro",      # Juliet starts in Act 1, Scene 3
    2: "romeo_melancholy",  # Romeo starts in Act 1, Scene 1
    3: "mercutio_taunts",   # Mercutio starts in Act 1, Scene 1
    4: "tybalt_fury",       # Tybalt starts in Act 1, Scene 1
    5: "paris_proposal"     # Paris starts in Act 1, Scene 2
}
