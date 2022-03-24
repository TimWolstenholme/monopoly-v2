from board import *
class Player:
    def __init__(self):
        self.money=2000
        self.property=[]
        self.mortgages=[]
        self.in_jail=False
        self.board_locations=monopoly_board.first_square
        self.location_name=self.board_locations.name
class PlayerChain:
    def __init__(self,first_player):
        self.first_player=first_player
    def add_player(self,new_player:Player):
        cur=self.first_player
        while cur.next:
            cur=cur.next
        cur.next=new_player
    def make_circular(self):
        cur=self.first_player
        while cur.next:
            cur=cur.next
        cur.next=self.first_player

class Game:
    def __init__(self) -> None:
        pass