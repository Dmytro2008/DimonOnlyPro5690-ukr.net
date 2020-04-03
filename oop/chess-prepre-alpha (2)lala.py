from abc import ABC, abstractmethod

#-------------------------Отримання ходу----------------------------------------------

class Human_Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def get_x_start(self):
        return self.x
    def get_y_start(self):
        return self.y
   
    def __sub__(self,other):
        return Human_Player(self.x-other.x,self.y-other.y)

current_position=Human_Player(int(input("Enter first coord(from):")),int(input("Enter second coord(from):"))) # Перша клітинка, яку обирає користувач
print("You choosed square",current_position.get_x_start(),current_position.get_y_start())
print("")
moving_to= Human_Player(int(input("Enter first coord(to):")),int(input("Enter second coord(to):")))

print("Figure is going to be moved to:",moving_to.get_x_start(),moving_to.get_y_start())
delta_move= moving_to - current_position
print("delta move:",delta_move.x,delta_move.y)



#-------------------------Класи Фігур(Пішак)----------------------------------------------


class Figure(ABC):     #абстрактний клас фігури (додай абстрактні методи, які потрібно буде перевизначити в конкретних класах)
    @property
    def price(self):
        return 0

    def move(self):
        pass
    
class Pawn(Figure):
    def __init__(self,current_x,current_y):
        self.current_x=current_x
        self.current_y=current_y
    @property
    def price(self):
        return 1
    moving_constantx=[0]  # додай можливість бити навхрест (можливо окремо)
    moving_constanty=[1,2] 




class King(Figure):
    def move(): #move повнен звертатися до дошки і тоді видавати moving constant
        return 0



class Rook(Figure):
    def __init__(self,current_x,current_y):
        self.current_x=current_x
        self.current_y=current_y
    @property
    def price(self):
        return 4
    moving_constantx=[0,1,2,3,4,5,6,7,8]  
    moving_constanty=[0,1,2,3,4,5,6,7,8]
    def move():
        return 0



class Knight(Figure):
    def __init__(self,current_x,current_y):
        self.current_x=current_x
        self.current_y=current_y
    @property
    def price(self):
        return 3
    def move():
        return 0
    moving_constantx = [-1,1]
    moving_constanty = [-2,2]
    


    
    
#-------------------------Інстансіація фігур(пішаки)----------------------------------------------

        
white_pawn1=Pawn(1,2)
white_pawn2=Pawn(2,2)
white_pawn3=Pawn(3,2)
white_pawn4=Pawn(4,2)
white_pawn5=Pawn(5,2)
white_pawn6=Pawn(6,2)
white_pawn7=Pawn(7,2)
white_pawn8=Pawn(8,2)

white_knight1=Knight(2,1)
white_knight2=Knight(7,1)


#knight
#-------------------------Дошка----------------------------------------------

class Board:
    pawns_list=[white_pawn1,white_pawn2,white_pawn3,white_pawn4,white_pawn5,white_pawn6,white_pawn7,white_pawn8] # список пішаків
    # мб створити окремий (двовимірний ?) список всієї дошки і вже на нього звертатися з класів фігур
    knights_list=[white_knight1, white_knight2]
    _n=8
    _m=8
    board_list=[]
    for i in range(_n):
        board_list.append([0] * _m)  #двомірний масив, заповнений нулями, далі додаються фігури
    for pawn in pawns_list:
        board_list[pawn.current_x-1][pawn.current_y-1]=pawn
    




#-------------------------Валідація----------------------------------------------

print("\n")
print("Pawn price is ",white_pawn1.price)


class Move:

    validated=False
    def validation_pawn():
        
        n=0
        is_pawn=False
        for i in Board.pawns_list: #якщо вибрана пішка ???
            n+=1
            if i.current_x==current_position.get_x_start():
                fixedx=n
                if Board.pawns_list[fixedx-1].current_y==current_position.get_y_start():
                    fixedy=Board.pawns_list[fixedx-1].current_y
                    print("You chosed pawn on x=",fixedx,"and y=",fixedy)
                    is_pawn=True
                    global x_id #id координат пішака
                    x_id=fixedx
                    global y_id 
                    y_id=fixedy
                    break
        if is_pawn==False:
            print("No pawn chosen!")

        
        if delta_move.x in Pawn.moving_constantx and delta_move.y in Pawn.moving_constanty:
            validated=True
        else:
            validated=False    
        return validated

    def validation_knight():
        n=0
        is_knight = False
        for i in Board.knights_list:
            n+=1
            if i.current_x==current_position.get_x_start():
                fixedx=n
                if Board.knights_list[fixedx-1].current_y == current_position.get_y_start():
                    fixedy = Board.knights_list[fixedx-1].current_y
                    print("You chosed knight on x=", fixedx, "and y=", fixedy)
                    is_knight=True
                    global x_id
                    x_id = fixedx
                    global y_id
                    y_id = fixedy
                    break
        if is_knight == False:
                print("No knight chosen!")
        if delta_move.x in Knight.moving_constantx and delta_move.y in Knight.moving_constanty:
            validated=True
        else:
            validated=False
        return validated



    
if Move.validation_knight()==True:
    print("This turn is correct!")
    Board.knights_list[x_id-1]=Knight(x_id+delta_move.x,y_id+delta_move.y)
    print("This knight is moved to",Board.knights_list[x_id-1].current_x,Board.knights_list[x_id-1].current_y)
else:
    print("This turn is incorrect")

if Move.validation_pawn()==True:
    print("This turn is correct!")
    Board.pawns_list[x_id-1]=Pawn(x_id,y_id+delta_move.y) # зміна положення пішака, при правильному ході Achtung! Працюватиме лише, коли пішак не змінює х-ї координати
    print("This pawn is moved to",Board.pawns_list[x_id-1].current_x,Board.pawns_list[x_id-1].current_y)
else:
    print("This turn is incorrect") # В такому випадку потрібно знову звернутись до користувача ???




#--------------------------Сміття---------------------------------------------






'''
print("---HEIL POROSHENKO---")
print("-----   |")
print("    |   |")
print("    |   |")
print("---------")
print("|   |    ")
print("|   |    ")
print("|   -----")
print("-----SIEG HIEL----")
'''
