from board import *
from random import randint
class Player:
    def __init__(self,name,next=None):
        self.name=name
        self.money=2000
        self.property=[]
        self.mortgages=[]
        self.in_jail=False
        self.board_locations=monopoly_board.first_square
        self.location_name=self.board_locations.name
        self.next=None
        self.jail_count=0
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
    def remove_player(self,node):
        cur=node
        while cur.next.next!=node:
            cur=cur.next
        cur.next=cur.next.next


class Game:
    def __init__(self,players:PlayerChain) -> None:
        self.end=False
        self.players=players
    def buy_property(self):
        self.players.cur_player.property.append(self.players.cur_player.board_locations)
        self.players.cur_player.money-=self.players.cur_player.board_locations.price
        print(f"{self.players.cur_player.location_name} bought for {self.players.cur_player.board_locations.price}")
        all_properties.remove(self.players.cur_player.board_locations.name)
    def mortgage_property(self,property):
        self.players.cur_player.property.remove(property)
        self.players.cur_player.property.append(property)
        cur=monopoly_board.first_square
        while cur.name!=property:
            cur=cur.next
        property_mortgage_cost=cur.mortgage_price
        self.players.cur_player.money+=property_mortgage_cost
    def move(self):
        total_roll=randint(1,6)+randint(1,6)
        for i in range(total_roll):
            self.players.cur_player.board_locations=self.players.cur_player.board_locations.next

    def go_to_jail(self):
        self.players.cur_player.in_jail=True
       
    def leave_jail(self):
        if self.players.cur_player.jail_count<3:
            d1=randint(1,6)
            d2=randint(1,6)
            if d1==d2:
                self.players.cur_player.in_jail=False
                for i in range(d1+d2):
                    self.players.cur_player.board_locations=self.players.cur_player.board_locations.next
                    self.players.cur_player.jail_count=0
            else:
                self.players.cur_player.jail_count+=1
        else:
            self.players.cur_player.money-=50
            self.move()
    def check_player_number(self):
        cur=self.players.cur_player
        cur:Player=cur.next
        while cur!=self.players.cur_player:
            if cur.money ==0 and len(cur.property)==0:
                self.players.remove_player(cur)
                print(f"{self.players.cur_player.name} is eliminated as they have no non morgadged propeties or money")
        first=self.players.cur_player
        cur=first.next
        if cur==first:
            return True
        return False

    
    
    def next_player(self):
        self.players.cur_player=self.players.cur_player.next
    

