# From BG3SE\BG3Extender\GameDefinitions\Enumerations.inl
"""
BEGIN_ENUM(AbilityId, uint8_t)
    EV(None, 0)
    EV(Strength, 1)
    EV(Dexterity, 2)
    EV(Constitution, 3)
    EV(Intelligence, 4)
    EV(Wisdom, 5)
    EV(Charisma, 6)
    EV(Sentinel, 7)
END_ENUM()
"""

attribute_map = {
    "None": "0",
    "Strength": "1",
    "Dexterity": "2",
    "Constitution": "3",
    "Intelligence": "4",
    "Wisdom": "5",
    "Charisma": "6",
    "Sentinel": "7"
}

"""
BEGIN_ENUM(SkillId, uint8_t)
    EV(Deception, 0)
    EV(Intimidation, 1)
    EV(Performance, 2)
    EV(Persuasion, 3)
    EV(Acrobatics, 4)
    EV(SleightOfHand, 5)
    EV(Stealth, 6)
    EV(Arcana, 7)
    EV(History, 8)
    EV(Investigation, 9)
    EV(Nature, 10)
    EV(Religion, 11)
    EV(Athletics, 12)
    EV(AnimalHandling, 13)
    EV(Insight, 14)
    EV(Medicine, 15)
    EV(Perception, 16)
    EV(Survival, 17)
    EV(Invalid, 18)
    EV(Sentinel, 19)
END_ENUM()
"""

skill_map = {
    "Deception": "0",
    "Intimidation": "1",
    "Performance": "2",
    "Persuasion": "3",
    "Acrobatics": "4",
    "SleightOfHand": "5",
    "Stealth": "6",
    "Arcana": "7",
    "History": "8",
    "Investigation": "9",
    "Nature": "10",
    "Religion": "11",
    "Athletics": "12",
    "AnimalHandling": "13",
    "Insight": "14",
    "Medicine": "15",
    "Perception": "16",
    "Survival": "17",
    "Invalid": "18",
    "Sentinel": "19"
}

"""
BEGIN_ENUM(SpellSourceType, uint8_t)
    EV(Progression0, 0x0)
    EV(Progression1, 0x1)
    EV(Progression2, 0x2)
    EV(Boost, 0x3)
    EV(Shapeshift, 0x4)
    EV(SpellSet2, 0x5)
    EV(SpellSet, 0x6)
    EV(WeaponAttack, 0x7)
    EV(UnarmedAttack, 0x8)
    EV(Osiris, 0x9)
    EV(Anubis, 0xA)
    EV(Behavior, 0xB)
    EV(PartyPreset, 0xC)
    EV(EquippedItem, 0xD)
    EV(GameActionCreateSurface, 0xE)
    EV(AiTest, 0xF)
    EV(CreateExplosion, 0x10)
    EV(Spell, 0x11)
    EV(ActiveDefense, 0x12)
    EV(Learned, 0x13)
    EV(Progression, 0x14)
    EV(Unknown15, 0x15)
    EV(Unknown16, 0x16)
    EV(Unknown17, 0x17)
    EV(Unknown18, 0x18)
    EV(Unknown19, 0x19)
    EV(Unknown1A, 0x1A)
    EV(Sentinel, 0x1B)
END_ENUM()
"""

spell_source_map = {
    "Progression0": "0",
    "Progression1": "1",
    "Progression2": "2",
    "Boost": "3",
    "Shapeshift": "4",
    "SpellSet2": "5",
    "SpellSet": "6",
    "WeaponAttack": "7",
    "UnarmedAttack": "8",
    "Osiris": "9",
    "Anubis": "10",
    "Behavior": "11",
    "PartyPreset": "12",
    "EquippedItem": "13",
    "GameActionCreateSurface": "14",
    "AiTest": "15",
    "CreateExplosion": "16",
    "Spell": "17",
    "ActiveDefense": "18",
    "Learned": "19",
    "Progression": "20",
    "Unknown16": "22",
    "Unknown17": "21",
    "Unknown18": "21",
    "Unknown19": "21",
    "Unknown1A": "21",
    "Sentinel": "27"
}

"""
BEGIN_ENUM(SpellCooldownType, uint8_t)
    EV(Default, 0)
    EV(OncePerTurn, 1)
    EV(OncePerCombat, 2)
    EV(UntilRest, 3)
    EV(OncePerTurnNoRealtime, 4)
    EV(UntilShortRest, 5)
    EV(UntilPerRestPerItem, 6)
    EV(OncePerShortRestPerItem, 7)
END_ENUM()
"""

cooldown_type_map = {
    "Default": "0",
    "OncePerTurn": "1",
    "OncePerCombat": "2",
    "UntilRest": "3",
    "OncePerTurnNoRealtime": "4",
    "UntilShortRest": "5",
    "UntilPerRestPerItem": "6",
    "OncePerShortRestPerItem": "7"
}