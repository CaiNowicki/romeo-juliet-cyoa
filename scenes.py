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
    # --- CAPULET BALL (Core Scene) ---
    "capulet_ball": {
        # --- JULIET (ID: 1) ---
        1: {
            "text": "The hall shimmers with candlelight. Paris approaches, offering his hand for a dance. Across the room, a masked stranger (Romeo) watches you. The Nurse winks from the shadows, while Tybalt’s scowl deepens as he notices the Montague intruder.",
            "choices": [
                {
                    "text": "Dance with Paris (play the dutiful daughter).",
                    "next": "ball_juliet_paris",
                    "effects": {
                        "paris_trust": +1,
                        "romeo_jealousy": +1,  # Romeo sees this
                        "tybalt_rage": +1       # Tybalt disapproves of Montague presence
                    }
                },
                {
                    "text": "Slip away to the balcony for air.",
                    "next": "balcony_soliloquy",
                    "effects": {
                        "romeo_opportunity": True  # Triggers Romeo’s choice to follow
                    }
                },
                {
                    "text": "Confront Tybalt: *'Why do you glare so?'*",
                    "next": "ball_juliet_tybalt",
                    "hidden": True,  # Only appears if Tybalt’s rage > 2
                    "effects": {
                        "tybalt_rage": +2,
                        "capulet_attention": True  # Lord Capulet may intervene
                    }
                }
            ]
        },

        # --- ROMEO (ID: 2) ---
        2: {
            "text": "Juliet outshines every torch. But Tybalt’s voice cuts through the music: *'This, by his voice, should be a Montague.'* Mercutio grins from the wine table, ready to stir trouble. Paris has Juliet’s hand—do you act?",
            "choices": [
                {
                    "text": "Approach Juliet mid-dance (bold).",
                    "next": "ball_romeo_juliet_meet",
                    "effects": {
                        "juliet_intrigue": +2,
                        "tybalt_rage": +2,
                        "paris_jealousy": True
                    }
                },
                {
                    "text": "Wait near the balcony (patient).",
                    "next": "balcony_eavesdrop",
                    "effects": {
                        "juliet_curiosity": +1  # She may notice you later
                    }
                },
                {
                    "text": "Let Mercutio distract Tybalt while you slip closer.",
                    "next": "ball_mercutio_distraction",
                    "effects": {
                        "mercutio_loyalty": +1,
                        "tybalt_suspicion": +1
                    }
                }
            ]
        },

        # --- TYBALT (ID: 4) ---
        4: {
            "text": "A *Montague*. Romeo’s voice is unmistakable. Your hand strays to your dagger—but Lord Capulet’s order rings in your ears: *'Content thee, gentle coz, let him alone.'* Do you obey?",
            "choices": [
                {
                    "text": "Confront Romeo publicly.",
                    "next": "ball_tybalt_duel",
                    "effects": {
                        "capulet_anger": True,
                        "romeo_banished": True  # If duel happens
                    }
                },
                {
                    "text": "Watch and plot. *'I’ll not endure him.'*",
                    "next": "ball_tybalt_plots",
                    "effects": {
                        "tybalt_rage": +1,
                        "romeo_unaware": True  # Romeo doesn’t notice Tybalt’s focus
                    }
                },
                {
                    "text": "Warn Juliet: *'Cousin, that villain touches your hand.'*",
                    "next": "ball_tybalt_warns_juliet",
                    "hidden": True,  # Only if Tybalt’s loyalty to Juliet > 1
                    "effects": {
                        "juliet_wary": True,
                        "romeo_difficulty": +1
                    }
                }
            ]
        },

        # --- MERCUTIO (ID: 3) ---
        3: {
            "text": '''Romeo’s lovesick sighs are *painful*. Tybalt’s glare is *hilarious*. You could:/n
            - **Provoke Tybalt** (classic fun).
            - **Spike Romeo’s drink** (let’s see what happens).
            - **Flirt with Rosaline** (just to mess with him).''',
            "choices": [
                {
                    "text": "Taunt Tybalt: *'Tybalt, you rat-catcher, will you walk?'*",
                    "next": "ball_mercutio_provokes",
                    "effects": {
                        "tybalt_rage": +2,
                        "capulet_attention": True
                    }
                },
                {
                    "text": "Slip something into Romeo’s wine.",
                    "next": "ball_romeo_drugged",
                    "effects": {
                        "romeo_confusion": True,
                        "juliet_conflict": +1  # She notices Romeo’s odd behavior
                    }
                },
                {
                    "text": "Dance with Rosaline—*in front of Romeo*.",
                    "next": "ball_mercutio_rosaline",
                    "effects": {
                        "romeo_jealousy": +1,
                        "juliet_amused": True
                    }
                }
            ]
        },

        # --- PARIS (ID: 5) ---
        5: {
            "text": "Juliet’s hand is warm in yours, but her smile doesn’t reach her eyes. Across the room, a masked man (Romeo) stares. Do you assert your claim or play the gentleman?",
            "choices": [
                {
                    "text": "Pull Juliet closer: *'Ignore the rabble, my lady.'*",
                    "next": "ball_paris_possessive",
                    "effects": {
                        "juliet_resentment": +1,
                        "romeo_jealousy": +2
                    }
                },
                {
                    "text": "Excuse yourself to speak with Lord Capulet (strategic).",
                    "next": "ball_paris_capulet",
                    "effects": {
                        "capulet_approval": +1,
                        "juliet_relief": True
                    }
                },
                {
                    "text": "Confront the masked man: *'Sir, you stare too boldly.'*",
                    "next": "ball_paris_confronts_romeo",
                    "effects": {
                        "romeo_hostility": True,
                        "tybalt_ally": True  # Tybalt may back Paris
                    }
                }
            ]
        },

        # --- NURSE (ID: 6) ---
        6: {
            "text": """Juliet’s dancing with Paris, but that Montague boy (Romeo) is *ogling* her like a starved cat. Do you:
            - **Warn Juliet** (discreetly).
            - **Flirt with Mercutio** (distract the menfolk).
            - **Fetch Lord Capulet** (let him handle it).""",
            "choices": [
                {
                    "text": "Whisper to Juliet: *'That’s young Romeo—*dangerous*.'*",
                    "next": "ball_nurse_warns",
                    "effects": {
                        "juliet_wary": True,
                        "romeo_difficulty": +1
                    }
                },
                {
                    "text": "Drag Mercutio into a dance: *'Come, sir, your wit’s as sharp as your sword!'",
                    "next": "ball_nurse_distracts",
                    "effects": {
                        "mercutio_amused": True,
                        "tybalt_distracted": True
                    }
                },
                {
                    "text": "Tell Lord Capulet about the Montague intruder.",
                    "next": "ball_capulet_intervenes",
                    "effects": {
                        "capulet_anger": True,
                        "romeo_banished": True  # If Capulet acts
                    }
                }
            ]
        },

        # --- LORD CAPULET (ID: 7) ---
        7: {
            "text": """The feast is lively, but Tybalt’s scowl and that *Montague boy* (Romeo) sour the air. Do you:
            - **Ignore it** (let the youngsters sort it).
            - **Order Tybalt to stand down** (again).
            - **Publicly shame Romeo** (make an example).""",
            "choices": [
                {
                    "text": "Pretend not to notice. *'More light, you knaves!'",
                    "next": "ball_capulet_ignores",
                    "effects": {
                        "tybalt_rage": +1,
                        "romeo_opportunity": True
                    }
                },
                {
                    "text": "Growl at Tybalt: *'I say he shall be endured!'",
                    "next": "ball_capulet_orders",
                    "effects": {
                        "tybalt_resentment": +1,
                        "romeo_relief": True
                    }
                },
                {
                    "text": "Point at Romeo: *'Seize that villain!'",
                    "next": "ball_romeo_exposed",
                    "effects": {
                        "romeo_banished": True,
                        "juliet_desperation": +1
                    }
                }
            ]
        }
    },

    # --- BRANCHING SCENES (Examples) ---
    "ball_juliet_paris": {
        1: {
            "text": """Paris’s hand is clammy. *'You blush, lady,'* he murmurs. Across the room, Romeo’s jaw tightens. The Nurse coughs meaningfully. Do you:
            - **Lean into the dance** (play along).
            - **Stumble and pull away** ('*I’m unwell!*').
            - **Whisper to Paris: *'I’d rather dance with the cat.'*""",
            "choices": [
                {"text": "Lean in (for now).", "next": "ball_paris_pleased"},
                {"text": "Pull away sharply.", "next": "ball_juliet_retreats", "effects": {"paris_offended": True}},
                {"text": "Insult Paris subtly.", "next": "ball_paris_humiliated", "effects": {"paris_rage": +1}}
            ]
        }
    },

    "balcony_soliloquy": {
        1: {
            "text": "The night air cools your flushed cheeks. *'O Romeo, Romeo...'*—wait. *Did you say that aloud?* A rustle below. Someone’s there.",
            "choices": [
                {"text": "Call out: *'Who’s there?'*", "next": "balcony_romeo_revealed"},
                {"text": "Pretend you didn’t hear.", "next": "balcony_juliet_ignores"},
                {"text": "Throw a rose into the shadows (a test).", "next": "balcony_rose_test"}
            ]
        },
        2: {  # Romeo (if he followed)
            "text": """Her voice—*she spoke your name*. Do you:
            - **Step into the light**.
            - **Stay hidden (listen longer)**.
            - **Whisper a poem** (romantic or ridiculous).""",
            "choices": [
                {"text": "Reveal yourself.", "next": "balcony_first_confession"},
                {"text": "Stay silent.", "next": "balcony_romeo_eavesdrops"},
                {"text": "Recite: *'Lady, by yonder blessed moon I vow...'*", "next": "balcony_romeo_poem"}
            ]
        }
    },

    # ... (Additional branches like "ball_tybalt_duel", "ball_mercutio_provokes", etc.)

}

START_SCENES = {
    1: "juliet_intro",      # Juliet starts in Act 1, Scene 3
    2: "romeo_melancholy",  # Romeo starts in Act 1, Scene 1
    3: "mercutio_taunts",   # Mercutio starts in Act 1, Scene 1
    4: "tybalt_fury",       # Tybalt starts in Act 1, Scene 1
    5: "paris_proposal"     # Paris starts in Act 1, Scene 2
}
