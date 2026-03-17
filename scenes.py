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
                    "next": "capulet_ball_prep"   # Triggers family conflict
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
                    "next": "capulet_ball"
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
                    "next": "capulet_ball"
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
                    "next": "capulet_ball"  # Attends ball, watches Romeo
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
                    "next": "capulet_ball"
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
                {"text": "Submit. Let them dress you for Paris.", "next": "capulet_ball"},
                {"text": "Sneak a dagger into your sleeve.", "next": "capulet_ball"}
            ]
        },
        2: {  # Romeo
            "text": "The Capulet hall buzzes with laughter. Masked, you scan the crowd—then see *her*. Juliet, radiant. But Tybalt’s glare burns from across the room.",
            "choices": [
                {"text": "Approach Juliet.", "next": "capulet_ball"},
                {"text": "Avoid her. This is madness.", "next": "capulet_ball"}
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
            "text": '''Romeo’s lovesick sighs are *painful*. Tybalt’s glare is *hilarious*. You could:
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

    # --- STUB SCENES (New Additions) ---
    # Romeo's solitary path
    "romeo_solitary": {
        2: {
            "text": "You storm into the night, leaving the revelry behind. The streets are empty, the stars cold. Rosaline’s face haunts you—but so does the thought of what might have been at the Capulet ball.",
            "choices": [
                {"text": "Return home, broken-hearted.", "next": "END"},
                {"text": "Seek Mercutio for distraction.", "next": "mercutio_provokes_tybalt"}
            ]
        }
    },

    # Mercutio provokes Tybalt
    "mercutio_provokes_tybalt": {
        3: {
            "text": "Tybalt’s face darkens as you saunter up. *'You fight as you sing, Mercutio—off-key,'* he sneers. The street empties. Do you:",
            "choices": [
                {"text": "Draw your sword.", "next": "street_brawl"},
                {"text": "Insult his house (no blades).", "next": "tybalt_fury"},
                {"text": "Laugh and walk away.", "next": "capulet_ball"}
            ]
        }
    },

    # Street brawl
    "street_brawl": {
        2: {  # Romeo (if present)
            "text": "Swords flash. Benvolio shouts for peace, but Tybalt’s blade is already singing. *'Draw, coward!'*—do you:",
            "choices": [
                {"text": "Fight Tybalt.", "next": "romeo_banished"},
                {"text": "Flee the scene.", "next": "capulet_ball_cautious"}
            ]
        },
        3: {  # Mercutio
            "text": "Tybalt’s blade is a silver arc. *'A scratch, a scratch!'*—but the wound is deep. Do you:",
            "choices": [
                {"text": "Curse the Capulets as you fall.", "next": "mercutio_death"},
                {"text": "Laugh it off (somehow).", "next": "capulet_ball"}
            ]
        },
        4: {  # Tybalt
            "text": "The Montague dogs cower. *'Peace? I hate the word as I hate hell.'*—do you press the attack?",
            "choices": [
                {"text": "Strike again!", "next": "romeo_banished"},
                {"text": "Withdraw (for now).", "next": "capulet_ball"}
            ]
        }
    },

    # Romeo banished
    "romeo_banished": {
        2: {
            "text": "The Prince’s decree is final: *'Banished.'* The word echoes. Verona is lost to you. Do you:",
            "choices": [
                {"text": "Flee to Mantua.", "next": "END"},
                {"text": "Hide in the monastery.", "next": "friar_laurence_help"}
            ]
        }
    },

    # Mercutio's death
    "mercutio_death": {
        3: {
            "text": "'*A plague o’ both your houses!*—the words taste of blood. The world dims. Your last thought: *Romeo will pay.*",
            "choices": [
                {"text": "Die cursing.", "next": "END"}
            ]
        }
    },

    # Paris patience
    "paris_patience": {
        5: {
            "text": "You bow to Capulet’s wisdom. *'Time is fleeting,'* but Juliet is worth the wait. For now, you’ll bide your time—and keep an eye on that Montague boy.",
            "choices": [
                {"text": "Attend the ball anyway (observe).", "next": "capulet_ball"},
                {"text": "Leave Verona on business.", "next": "END"}
            ]
        }
    },

    # Ball: Juliet and Paris
    "ball_juliet_paris": {
        1: {
            "text": "Paris’s grip is firm, his smile practiced. *'You honor me,'* he murmurs. Across the room, Romeo’s glare burns. The Nurse watches, arms crossed.",
            "choices": [
                {"text": "Smile and play along.", "next": "ball_paris_pleased"},
                {"text": "Stumble—'*I feel unwell!*'", "next": "ball_juliet_retreats"},
                {"text": "Whisper: *'I’d rather dance with a goat.'*", "next": "ball_paris_humiliated"}
            ]
        }
    },

    # Ball: Paris pleased
    "ball_paris_pleased": {
        5: {
            "text": "Juliet’s compliance warms you. *'She’ll come around,'* you think. Then you notice Romeo, lurking like a thief. Do you:",
            "choices": [
                {"text": "Ignore him (focus on Juliet).", "next": "capulet_ball"},
                {"text": "Confront him publicly.", "next": "ball_paris_confronts_romeo"}
            ]
        },
        1: {
            "text": "Paris preens. *'Charming,'* he says. You spot Romeo’s shadow near the balcony. The Nurse tugs your sleeve—'*A word, lamb.*'",
            "choices": [
                {"text": "Follow the Nurse.", "next": "ball_nurse_warns"},
                {"text": "Slip to the balcony.", "next": "balcony_soliloquy"}
            ]
        }
    },

    # Ball: Juliet retreats
    "ball_juliet_retreats": {
        1: {
            "text": "The crowd parts as you flee. *'Juliet!'*—Romeo’s voice? No, just the wind. The balcony beckons, quiet and dark.",
            "choices": [
                {"text": "Go to the balcony.", "next": "balcony_soliloquy"},
                {"text": "Find the Nurse.", "next": "ball_nurse_warns"}
            ]
        }
    },

    # Ball: Paris humiliated
    "ball_paris_humiliated": {
        5: {
            "text": "Your face burns. *'A goat?'* Juliet’s words cut deeper than any blade. The Montague boy smirks. Do you:",
            "choices": [
                {"text": "Demand an apology.", "next": "ball_paris_confronts_romeo"},
                {"text": "Storm out.", "next": "END"}
            ]
        }
    },

    # Ball: Juliet confronts Tybalt
    "ball_juliet_tybalt": {
        1: {
            "text": "Tybalt’s snarl falters. *'Cousin?'* You press: *'Why do you glare at our guests?'* His hand twitches toward his dagger.",
            "choices": [
                {"text": "Back down (nervously).", "next": "capulet_ball"},
                {"text": "Call for Lord Capulet.", "next": "ball_capulet_intervenes"}
            ]
        },
        4: {
            "text": "Juliet’s interference grates. *'You don’t understand,'* you hiss. But Capulet’s eye is on you now.",
            "choices": [
                {"text": "Apologize (grudgingly).", "next": "capulet_ball"},
                {"text": "Storm out.", "next": "street_brawl"}
            ]
        }
    },

    # Ball: Romeo meets Juliet
    "ball_romeo_juliet_meet": {
        2: {
            "text": "Juliet’s hand is warm in yours. *'You kiss by the book,'* she teases. Paris glares. Tybalt’s dagger is half-drawn.",
            "choices": [
                {"text": "Kiss her hand boldly.", "next": "first_kiss"},
                {"text": "Retreat (Tybalt’s watching).", "next": "capulet_ball"}
            ]
        },
        1: {
            "text": "This stranger’s touch sends a spark through you. *'Sir, you presume,'*—but you don’t pull away. The Nurse is going to *kill* you.",
            "choices": [
                {"text": "Let him kiss your hand.", "next": "first_kiss"},
                {"text": "Push him away (scandalized).", "next": "ball_slap"}
            ]
        }
    },

    # First kiss
    "first_kiss": {
        1: {
            "text": "His lips brush your knuckles. The world narrows to this moment. *'Sin from my lips?'*—but oh, it’s sweet.",
            "choices": [
                {"text": "Whisper: *'You may call me love.'*", "next": "balcony_soliloquy"},
                {"text": "Pull away (nervous).", "next": "capulet_ball"}
            ]
        },
        2: {
            "text": "Her fingers curl around yours. *'Pilgrim,'* she murmurs, *'you wrong your hand.'* The crowd fades. This is madness. This is everything.",
            "choices": [
                {"text": "Ask her name.", "next": "balcony_soliloquy"},
                {"text": "Flee (this is too dangerous).", "next": "romeo_solitary"}
            ]
        }
    },

    # Ball: Slap
    "ball_slap": {
        2: {
            "text": "Your cheek stings. The hall gasps. Tybalt’s laughter rings like a death knell.",
            "choices": [
                {"text": "Apologize (humiliated).", "next": "capulet_ball"},
                {"text": "Challenge Tybalt.", "next": "street_brawl"}
            ]
        }
    },

    # Ball: Mercutio distracts Tybalt
    "ball_mercutio_distraction": {
        3: {
            "text": "Tybalt’s scowl twists to confusion as you sweep him into a jig. *'A dance, coz!'* Romeo slips past, grinning. *'I owe you one,'* he mouths.",
            "choices": [
                {"text": "Keep dancing (chaos is fun).", "next": "capulet_ball"},
                {"text": "Trip Tybalt.", "next": "ball_tybalt_duel"}
            ]
        }
    },

    # Ball: Tybalt duels
    "ball_tybalt_duel": {
        4: {
            "text": "Steel sings. *'Draw, coward!'*—but Capulet’s roar cuts through: *'HOLD!'*—do you:",
            "choices": [
                {"text": "Obey (grudgingly).", "next": "capulet_ball"},
                {"text": "Strike anyway.", "next": "romeo_banished"}
            ]
        }
    },

    # Ball: Tybalt plots
    "ball_tybalt_plots": {
        4: {
            "text": "You’ll bide your time. But that Montague won’t leave alive. *'Patience, cousin,'* you mutter. The Nurse eyes you warily.",
            "choices": [
                {"text": "Find Juliet (warn her).", "next": "ball_tybalt_warns_juliet"},
                {"text": "Sharpen your dagger.", "next": "capulet_ball"}
            ]
        }
    },

    # Ball: Tybalt warns Juliet
    "ball_tybalt_warns_juliet": {
        1: {
            "text": "Tybalt’s voice is urgent. *'That boy is death, cousin. Stay away.'* You glance at Romeo—his smile is like sunlight.",
            "choices": [
                {"text": "Thank Tybalt (but ignore him).", "next": "balcony_soliloquy"},
                {"text": "Tell the Nurse.", "next": "ball_nurse_warns"}
            ]
        }
    },

    # Ball: Romeo drugged
    "ball_romeo_drugged": {
        2: {
            "text": "The world spins. *'Did someone spike my wine?'*—Juliet’s face blurs. *'Poison?'*—no, just Mercutio’s idea of a joke.",
            "choices": [
                {"text": "Stagger to the balcony.", "next": "balcony_eavesdrop"},
                {"text": "Collapse dramatically.", "next": "ball_mercutio_rosaline"}
            ]
        }
    },

    # Ball: Mercutio and Rosaline
    "ball_mercutio_rosaline": {
        3: {
            "text": "Rosaline’s laugh is sharp as your dagger. *'You’re no Romeo,'* she says. Across the room, Romeo sways—*drugged?*—while Juliet watches, fascinated.",
            "choices": [
                {"text": "Flirt harder.", "next": "capulet_ball"},
                {"text": "Abandon the game (Romeo needs help).", "next": "balcony_eavesdrop"}
            ]
        }
    },

    # Ball: Paris confronts Romeo
    "ball_paris_confronts_romeo": {
        5: {
            "text": "The Montague’s mask slips. *'You—'* Juliet’s eyes widen. *'Paris, no!'*—but the hall is watching now.",
            "choices": [
                {"text": "Demand his name.", "next": "ball_romeo_exposed"},
                {"text": "Back down (for Juliet).", "next": "ball_paris_possessive"}
            ]
        },
        2: {
            "text": "Paris’s grip on your arm is iron. *'You intrude, sir.'*—Juliet’s face is unreadable. Do you:",
            "choices": [
                {"text": "Apologize and leave.", "next": "romeo_solitary"},
                {"text": "Draw your sword.", "next": "street_brawl"}
            ]
        }
    },

    # Ball: Capulet intervenes
    "ball_capulet_intervenes": {
        7: {
            "text": "'*Enough!*—your voice booms. The Montague boy pales. *'Out, or I’ll have you seized!'*—but Juliet’s eyes are on the stranger.",
            "choices": [
                {"text": "Order Tybalt to stand down.", "next": "ball_capulet_orders"},
                {"text": "Let it go (for now).", "next": "capulet_ball"}
            ]
        }
    },

    # Ball: Capulet ignores
    "ball_capulet_ignores": {
        7: {
            "text": "You turn a blind eye. Let the youngsters sort it. But Tybalt’s scowl promises trouble later.",
            "choices": [
                {"text": "Drink more wine.", "next": "capulet_ball"},
                {"text": "Watch Romeo closely.", "next": "ball_romeo_exposed"}
            ]
        }
    },

    # Ball: Capulet orders
    "ball_capulet_orders": {
        7: {
            "text": "'*Tybalt, I say!*—he glares but sheathes his dagger. The Montague boy bows—*mockingly*—and slips away. Juliet’s cheeks are flushed.",
            "choices": [
                {"text": "Return to the party.", "next": "capulet_ball"},
                {"text": "Follow the boy.", "next": "balcony_eavesdrop"}
            ]
        }
    },

    # Ball: Romeo exposed
    "ball_romeo_exposed": {
        2: {
            "text": "The room stills. *'A Montague,'* someone gasps. Juliet’s hand flies to her mouth. Tybalt’s dagger is out. *'Seize him!'*—Capulet roars.",
            "choices": [
                {"text": "Flee.", "next": "romeo_banished"},
                {"text": "Draw your sword.", "next": "street_brawl"}
            ]
        }
    },

    # Balcony: Romeo eavesdrops
    "balcony_eavesdrop": {
        2: {
            "text": "Juliet’s voice floats down: *'O Romeo, Romeo...'*—your heart stops. She doesn’t know you’re here. Do you:",
            "choices": [
                {"text": "Reveal yourself.", "next": "balcony_first_confession"},
                {"text": "Listen longer (coward).", "next": "balcony_romeo_eavesdrops"},
                {"text": "Leave (this is wrong).", "next": "romeo_solitary"}
            ]
        }
    },

    # Balcony: Romeo eavesdrops (continued)
    "balcony_romeo_eavesdrops": {
        2: {
            "text": "She sighs, *'Wherefore art thou Romeo?'*—and you realize: *she doesn’t even know your name*. The irony stings. Do you:",
            "choices": [
                {"text": "Speak now.", "next": "balcony_first_confession"},
                {"text": "Sneak away (heartbroken).", "next": "romeo_solitary"}
            ]
        }
    },

    # Balcony: Romeo revealed
    "balcony_romeo_revealed": {
        1: {
            "text": "'*Who’s there?*'—a shadow moves. *'Romeo—'*—no, it can’t be. But his voice is raw: *'I take thee at thy word.'*",
            "choices": [
                {"text": "Send him away (dangerous).", "next": "romeo_banished"},
                {"text": "Let him stay (foolish).", "next": "balcony_first_confession"}
            ]
        }
    },

    # Balcony: Rose test
    "balcony_rose_test": {
        1: {
            "text": "The rose lands at his feet. A pause. Then: *'A rose by any other name...'*—his voice is soft. *'Would smell as sweet.'*",
            "choices": [
                {"text": "Invite him up.", "next": "balcony_first_confession"},
                {"text": "Retreat indoors (blushing).", "next": "capulet_ball"}
            ]
        }
    },

    # Friar Laurence help
    "friar_laurence_help": {
        2: {
            "text": "The friar’s cell is dim. *'Banished?'*—he strokes his beard. *'There’s more in this than we yet know.'*",
            "choices": [
                {"text": "Ask for his help.", "next": "marriage_plot"},
                {"text": "Leave Verona forever.", "next": "END"}
            ]
        }
    },

    # Marriage plot
    "marriage_plot": {
        2: {
            "text": "Friar Laurence’s plan is mad—but so is love. *'Go to Juliet’s chamber tonight.'*—the words send fire through you.",
            "choices": [
                {"text": "Agree (no turning back).", "next": "secret_marriage"},
                {"text": "Refuse (this is folly).", "next": "romeo_solitary"}
            ]
        }
    },

    # Secret marriage
    "secret_marriage": {
        1: {
            "text": "The friar’s voice echoes: *'For by your leaves, you shall not stay alone.'*—Romeo’s hand is warm in yours. This is madness. This is fate.",
            "choices": [
                {"text": "Say 'I do.'", "next": "END"},
                {"text": "Flee (last chance).", "next": "convent_escape"}
            ]
        }
    },

    # Convent escape
    "convent_escape": {
        1: {
            "text": "The convent walls are cold but safe. The Nurse’s voice echoes: *'He’s gone, lamb. It’s for the best.'*—but your heart knows otherwise.",
            "choices": [
                {"text": "Stay (become a nun).", "next": "END"},
                {"text": "Write to Romeo in Mantua.", "next": "secret_letters"}
            ]
        }
    },

    # Secret letters
    "secret_letters": {
        1: {
            "text": "The ink bleeds like your heart. *'My dearest love—'*—but the letter may never reach him. The Nurse hovers, suspicious.",
            "choices": [
                {"text": "Send it (hope).", "next": "END"},
                {"text": "Burn it (despair).", "next": "END"}
            ]
        }
    },

    # --- STUB SCENES (Placeholders to keep story links connected) ---
    "balcony_soliloquy": {
        1: {
            "text": "[TODO] Balcony soliloquy (Juliet).",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        },
        2: {
            "text": "[TODO] Balcony soliloquy (Romeo).",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },
    "balcony_first_confession": {
        1: {
            "text": "[TODO] First confession (Juliet).",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        },
        2: {
            "text": "[TODO] First confession (Romeo).",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },
    "ball_mercutio_provokes": {
        3: {
            "text": "[TODO] Mercutio provokes Tybalt.",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },
    "ball_nurse_warns": {
        1: {
            "text": "[TODO] The Nurse warns Juliet.",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        },
        6: {
            "text": "[TODO] The Nurse warns Juliet (Nurse perspective).",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },
    "ball_nurse_distracts": {
        6: {
            "text": "[TODO] The Nurse distracts Mercutio.",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },
    "ball_paris_possessive": {
        5: {
            "text": "[TODO] Paris grows possessive.",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },
    "ball_paris_capulet": {
        5: {
            "text": "[TODO] Paris speaks with Lord Capulet.",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },
    "capulet_ball_cautious": {
        2: {
            "text": "[TODO] Romeo retreats after the street brawl.",
            "choices": [
                {"text": "Return to the ball.", "next": "capulet_ball"},
                {"text": "End for now.", "next": "END"}
            ]
        }
    },

    # END scene
    "END": {
        1: {"text": "The stars go out one by one. What’s done is done.", "choices": []},
        2: {"text": "The road to Mantua is long. You wonder if you’ll ever see her again.", "choices": []},
        3: {"text": "Your laughter dies with you. *'A plague o’ both your houses.'*", "choices": []},
        4: {"text": "The feud claims another soul. Was it worth it?", "choices": []},
        5: {"text": "Juliet’s face haunts you. You should have been bolder.", "choices": []},
        6: {"text": "The Nurse’s warnings were right. Now it’s too late.", "choices": []},
        7: {"text": "The party ends. The young will learn—or they won’t.", "choices": []}
    }
}

START_SCENES = {
    1: "juliet_intro",      # Juliet starts in Act 1, Scene 3
    2: "romeo_melancholy",  # Romeo starts in Act 1, Scene 1
    3: "mercutio_taunts",   # Mercutio starts in Act 1, Scene 1
    4: "tybalt_fury",       # Tybalt starts in Act 1, Scene 1
    5: "paris_proposal"     # Paris starts in Act 1, Scene 2
}
