class Card:
    def __init__(self, value, suit):
        syms = {'D': '\u2666', 'H': '\u2665', 'S': '\u2660', 'C': '\u2663'}
        faces = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        self.suit = suit
        self.value = value
        self.visible = False
        if value in faces.keys():
            self.name = faces[value] + syms[suit]
        else:
            self.name = str(value) + syms[suit]
        if suit == 'D' or suit == 'H':
            self.color = 'r'
        else:
            self.color = 'b'

    def print_name(self):
        if self.visible:
            return '[' + (' ' if self.value !=10 else '') + self.name + ']'
        else:
            return '[xxx]'

    # Checks if this card can be moved on top of a given end stack card
    def is_valid_move(self, target, stack_type):
        if stack_type == 'm':
            return (target.color != self.color) and (self.value == target.value-1)
        else:
            return (target.suit == self.suit) and (self.value == target.value+1)
