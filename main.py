import tkinter as tk
from card import Card
from deck import Deck
from player import Player
from discard_pile import DiscardPile

class CardGameGUI:
    def __init__(self, root):
        self.root = root
        root.title("IT-Dev-Oh! Card Game")

        # Game elements (from your logic)
        self.game_deck = Deck()
        self.game_deck.create_standard_deck()

        print("--- Deck Contents ---")
        for card in self.game_deck.cards:
            print(card) # Now printing a card will show more info
            print("-" * 20) # Separator

        self.player1 = Player("Yugi")
        self.player2 = Player("Kaiba") # Let's just focus on player 1 for GUI initially
        self.discard_pile = DiscardPile()

        # Initial hand for player 1 (for testing)
        for _ in range(5): # Draw 5 cards
            self.player1.draw_from_deck(self.game_deck)

        # --- GUI Layout ---
        self.hand_label = tk.Label(root, text="Hand:")
        self.hand_label.pack()

        self.hand_cards_frame = tk.Frame(root) # Frame to hold hand card frames
        self.hand_cards_frame.pack()

        self.table_label = tk.Label(root, text="Table:")
        self.table_label.pack()

        self.table_cards_frame = tk.Frame(root) # Frame to hold table card frames
        self.table_cards_frame.pack()

        self.draw_button = tk.Button(root, text="Draw Card", command=self.draw_card_action)

        self.hand_cards_frame = tk.Frame(root, bg="yellow")  # Force yellow background for hand frame
        self.hand_cards_frame.pack()

        self.table_label = tk.Label(root, text="Table:")
        self.table_label.pack()

        self.table_cards_frame = tk.Frame(root, bg="orange") # Force orange background for table frame
        self.table_cards_frame.pack()

        self.draw_button.pack()

        self.update_display()


    def draw_card_action(self):
        self.player1.draw_from_deck(self.game_deck)
        self.update_display() # Update the display after drawing


    def update_display(self):
        # --- Update Hand Display ---
        # Clear existing card frames in hand_frame
        for widget in self.hand_cards_frame.winfo_children():
            widget.destroy() # Remove old card frames

        print("--- Hand Cards ---")
        for card in self.player1.hand:
            self.create_card_frame(card, self.hand_cards_frame) # Create and add card frame to hand_frame

        # --- Update Table Display ---
        # Clear existing card frames in table_frame
        for widget in self.table_cards_frame.winfo_children():
            widget.destroy()

        print("--- Table Cards ---")
        for card in self.player1.table:
            self.create_card_frame(card, self.table_cards_frame) # Create and add card frame to table_frame


    def create_card_frame(self, card, parent_frame):
        card_button = tk.Button(parent_frame,
                                 relief=tk.RAISED,
                                 borderwidth=2, # Make border thicker to see it
                                 command=lambda c=card: self.play_card_from_hand_action(c),
                                 padx=10, pady=10, width=10, height=5,
                                 bg="lightblue",  # Force background color
                                 fg="darkgreen") # Force foreground (text) color
        card_button.pack(side=tk.LEFT, padx=5, pady=5)

        name_label = tk.Label(card_button, text=card.name)
        name_label.pack(pady=(5, 0))

        if card.category == "Creature":
            atk_def_frame = tk.Frame(card_button)
            atk_def_frame.pack(pady=(0, 5))

            atk_label = tk.Label(atk_def_frame, text=f"ATK: {card.attack}")
            atk_label.pack(side=tk.LEFT, padx=(0, 10))

            def_label = tk.Label(atk_def_frame, text=f"DEF: {card.defense}")
            def_label.pack(side=tk.LEFT)
        else:
            desc_label = tk.Label(card_button, text=card.description, wraplength=100, justify=tk.LEFT)
            desc_label.pack(pady=(0, 5), padx=5)

        return card_button


    def play_card_from_hand_action(self, card_to_play):
        if card_to_play in self.player1.hand: # Check if card is still in hand (important!)
            self.player1.play_card_to_table(card_to_play.name) # Use card name to play
            self.update_display() # Update the GUI
        else:
            print(f"Card '{card_to_play.name}' is no longer in hand.") # Handle case where card is not in hand anymore (e.g., already played)

def main():
    root = tk.Tk()
    game_gui = CardGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()