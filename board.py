from xml.sax.handler import all_properties


class Square:
    def __init__(self,name,price,set,type,rent,next=None,prev=None):
        self.name=name
        self.price=price
        self.set=set
        self.type=type
        self.next=next
        self.prev=prev
        self.rent=rent
        self.is_full_set=False
        self.owner=None
class Board:
    def __init__(self,first_square:Square):
        self.first_square=first_square
    def add_square(self,new_square:Square):
        cur=self.first_square
        if not cur:
            self.first_square=new_square
        while cur.next:
            cur=cur.next
        cur.next=new_square
        new_square.prev=cur
    def make_circular(self):
        cur=self.first_square
        while cur.next:
            cur=cur.next
        cur.next=self.first_square
if __name__=='__main__':
    monopoly_board=Board(Square("Go!",None,None,"Go",None))
    monopoly_board.add_square(Square("Old Kent Road",60,'Brown',"property",2))
    monopoly_board.add_square(Square("Community chest", None,None,'chest',None))
    monopoly_board.add_square(Square("Whitechapel Road",60,"Brown","property",4))
    monopoly_board.add_square(Square("Income Tax",None,None,'tax',200))
    monopoly_board.add_square(Square("Kings Cross Station",200,'Station','property',None))
    monopoly_board.add_square(Square("The Angel Islington",100,'Blue','property',6))
    monopoly_board.add_square(Square("Chance",None,None,'chance',None))
    monopoly_board.add_square(Square("Euston Road",100,'Blue','property',6))
    monopoly_board.add_square(Square("Pentonville Road",120,'Blue','property',8))
    monopoly_board.add_square(Square("Visiting Jail",None,None,"no_action",None))
    monopoly_board.add_square(Square("Pall Mall",140,'Pink','property',10))
    monopoly_board.add_square(Square("Eletric Company",150,'Utility','property',None))
    monopoly_board.add_square(Square("Whitehall",140,'Pink','property',10))
    monopoly_board.add_square(Square("Northumberland Avenue",160,'Pink','property',12))
    monopoly_board.add_square(Square("Marylebone Station",200,'Station','property',None))
    monopoly_board.add_square(Square("Bow Street",180,"Orange","property",14))
    monopoly_board.add_square(Square("Community chest", None,None,'chest',None))
    monopoly_board.add_square(Square("Marlborough Street",180,"Orange","property",14))
    monopoly_board.add_square(Square("Vine Street",200,"Orange","property",16))
    monopoly_board.add_square(Square("Free Parking",None,None,"parking",None))
    monopoly_board.add_square(Square("Strand",220,'Red','property',18))
    monopoly_board.add_square(Square("Chance",None,None,'chance',None))
    monopoly_board.add_square(Square("Fleet Street",220,'Red','property',18))
    monopoly_board.add_square(Square("Trafalgar Square",240,'Red','property',20))
    monopoly_board.add_square(Square("Fenchurch Street Station",200,'Station','property',None))
    monopoly_board.add_square(Square("Leicester Square",260,'Yellow','property',22))
    monopoly_board.add_square(Square("Coventry Street",260,'Yellow','property',22))
    monopoly_board.add_square(Square("Water Works",150,'Utility','property',None))
    monopoly_board.add_square(Square("Piccadilly",280,'Yellow','Property',24))
    monopoly_board.add_square(Square("GO TO JAIL!",None,None,'jail',None))
    monopoly_board.add_square(Square("Regent Street",300,'Green','property',26))
    monopoly_board.add_square(Square("Oxford Street",300,'Green','property',26))
    monopoly_board.add_square(Square("Community chest", None,None,'chest',None))
    monopoly_board.add_square(Square("Bond Street",320,'Green','property',28))
    monopoly_board.add_square(Square("Liverpool Street Station",200,'Station','property',None))
    monopoly_board.add_square(Square("Chance",None,None,'chance',None))
    monopoly_board.add_square(Square("Park Lane",350,'DBlue','property',35))
    monopoly_board.add_square(Square("Super Tax",None,None,'tax',100))
    monopoly_board.add_square(Square("Mayfair",400,'DBlue','property',50))
    monopoly_board.make_circular()
    all_properties=['Old Kent Road','Whitechapel Road','Kings Cross Station','The Angel Islington','Euston Road','Pentonville Road','Pall Mall','Eletric Company','Whitehall','Northumberland Avenue','Marylebone Station','Bow Street','Marlborough Street','Vine Street','Strand','Fleet Street','Trafalgar Square','Fenchurch Street Station','Leicester Square','Coventry Street','Piccadilly','Regent Street','Oxford Street','Bond Street','Liverpool Street Station','Park Lane','Mayfair']


