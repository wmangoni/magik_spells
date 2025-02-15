class Card:
    def __init__(self, name, category, attack, defense, description):
        self.name = name
        self.category = category # Creature, Spell, Terrain, Artefact
        self.attack = attack
        self.defense = defense
        self.description = description

    def __str__(self):
        return (f"{self.name} ({self.category})\n"
                f"Attack: {self.attack}, Defense: {self.defense}\n"
                f"Description: {self.description}")