class DiscardPile:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        discarded_card_names = ", ".join([str(card) for card in self.cards]) if self.cards else "Empty"
        return f"Discard Pile: [{discarded_card_names}]"