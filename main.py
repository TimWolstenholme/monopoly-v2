from board import *
class Player:
    def __init__(self,next=None):
        self.money=2000
        self.property=[]
        self.mortgages=[]
        self.in_jail=False
        self.board_locations=monopoly_board.first_square
        self.location_name=self.board_locations.name
        self.next=None
class PlayerChain:
    def __init__(self,first_player:Player):
        self.first_player=first_player
        self.cur_player=self.first_player
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
    def __init__(self,players:PlayerChain) -> None:
        self.end=False
        self.players=players
    def buy_property(self):
        self.players.cur_player.property.append(self.players.cur_player.board_locations.name)
        self.players.cur_player.money-=self.players.cur_player.board_locations.price
        print(f"{self.players.cur_player.board_locations} bought for {self.players.cur_player.board_locations.price}")
        all_properties.remove(self.players.cur_player.board_locations.name)
    def mortgage_property(self,property):
        self.players.cur_player.property.remove(property)
        self.players.cur_player.property.append(property)
        cur=monopoly_board.first_square
        while cur.name!=property:
            cur=cur.next
        property_mortgage_cost=cur.mortgage_price
        self.players.cur_player.money+=property_mortgage_cost

    
    
    
    def next_player(self):
        self.players.cur_player=self.players.cur_player.next
    

