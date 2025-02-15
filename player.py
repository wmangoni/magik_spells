from card import Card

class Player:
    def __init__(self, name="Player"):
        self.name = name
        self.hand = []
        self.table = []

    def draw_from_deck(self, deck):
        drawn_card = deck.draw_card()
        if drawn_card:
            self.hand.append(drawn_card)
            print(f"{self.name} drew: {drawn_card}")
        else:
            print("Deck is empty, cannot draw!")

    def play_card_to_table(self, card_name):
        card_to_play = None
        for card in self.hand:
            if card.name == card_name:
                card_to_play = card
                break
        if card_to_play:
            self.hand.remove(card_to_play)
            self.table.append(card_to_play)
            print(f"{self.name} played {card_to_play} to the table.")
        else:
            print(f"{self.name} does not have '{card_name}' in hand.")

    def discard_card_from_hand(self, card_name, discard_pile):
        card_to_discard = None
        for card in self.hand:
            if card.name == card_name:
                card_to_discard = card
                break
        if card_to_discard:
            self.hand.remove(card_to_discard)
            discard_pile.append(card_to_discard)
            print(f"{self.name} discarded {card_to_discard} from hand.")
        else:
            print(f"{self.name} does not have '{card_name}' in hand to discard.")

    def __str__(self):
        hand_cards = ", ".join([str(card) for card in self.hand]) if self.hand else "Empty"
        table_cards = ", ".join([str(card) for card in self.table]) if self.table else "Empty"
        return f"{self.name}'s Hand: [{hand_cards}]  |  Table: [{table_cards}]"
