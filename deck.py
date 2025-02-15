from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []

    def create_standard_deck(self):
        # Example cards with categories, attack, defense, and descriptions
        card_data = [
            {"name": "Frontend Jr", "category": "Creature", "attack": 1, "defense": 1, "description": "Enthusiastic coder, still learning."},
            {"name": "Backend Master", "category": "Creature", "attack": 3, "defense": 2, "description": "Solid backend skills, reliable."},
            {"name": "Agile Spell", "category": "Spell", "attack": 0, "defense": 0, "description": "Boosts creature attack in short bursts."},
            {"name": "Firewall Terrain", "category": "Terrain", "attack": 0, "defense": 3, "description": "Protects your field, hard to break through."},
            {"name": "Keyboard Artefact", "category": "Artefact", "attack": 1, "defense": 0, "description": "Equipped creature gets a small attack buff."},
            {"name": "Coffee Spell", "category": "Spell", "attack": 1, "defense": 1, "description": "Gives a creature a temporary boost in both attack and defense."},
            {"name": "Cloud Terrain", "category": "Terrain", "attack": 1, "defense": 1, "description": "Provides balanced buffs to creatures in play."},
            {"name": "Server Artefact", "category": "Artefact", "attack": 2, "defense": 1, "description": "Greatly increases attack, slightly increases defense."},
            {"name": "Trainee Dev", "category": "Creature", "attack": 0, "defense": 2, "description": "Eager to learn, high potential for defense."},
            {"name": "Senior Architect", "category": "Creature", "attack": 4, "defense": 3, "description": "Master of systems design, very powerful."},
            {"name": "Debug Spell", "category": "Spell", "attack": 2, "defense": 0, "description": "Temporarily weakens opponent creatures."},
            {"name": "Cybersecurity Terrain", "category": "Terrain", "attack": 0, "defense": 4, "description": "Extremely robust defense, nearly impenetrable."},
            {"name": "Algorithm Artefact", "category": "Artefact", "attack": 3, "defense": 0, "description": "Massively boosts attack, no defense bonus."}
        ] # You can expand this list with more cards

        for card_info in card_data:
            card = Card(**card_info) # Create Card object using dictionary unpacking
            self.cards.append(card)

        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop(0)

    def __str__(self):
        return f"Deck with {len(self.cards)} cards"