from abc import ABC, abstractmethod
import math

#-------------------------Визначення користувацької виключної ситуації---------------


class Error(Exception):   #"Базовий" клас для інших виключних ситуацій
   pass

class NoFigureSelectedError(Error):
    pass
class NotDeskIndexError(Error):
    pass
class MoveError(Error):
    pass
class AmbiguityError(Error):
   pass
class SameSquareError(Error):
   pass

#-------------------------Клас "Отримання ходу"----------------------------------------------


class IPlayer:
    def get_x_start(self):
        return self.x
    def get_y_start(self):
        return self.y


class Human_Player(IPlayer):
    
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

   
    def __sub__(self,other):
        return Human_Player(self.x-other.x,self.y-other.y)








#-------------------------Класи Фігур(Пішак і Тура)----------------------------------------------


class Figure(ABC):
    @abstractmethod
    def price(self):
        return 0
    @abstractmethod
    def move_x():
        pass
    @abstractmethod
    def move_y():    
        pass


    
class Pawn(Figure):
    def __init__(self,current_x,current_y,colour):
        self.current_x=current_x
        self.current_y=current_y
        self.colour=colour
    @property
    def price(self):
        return 1
    def move_x():
        return [0]  # додай можливість бити навхрест (можливо окремо)
    def move_y():
        return [1,2] ### Як зробити для у != 2 ???


class Rook(Figure):
    def __init__(self,current_x,current_y,colour):
        self.current_x=current_x
        self.current_y=current_y
        self.colour=colour
    @property
    def price(self):
        return 4
    def move_x():
        return [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
    def move_y():    
        return [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]

class Knight(Figure):
    def __init__(self, current_x, current_y,colour):
        self.current_x = current_x
        self.current_y = current_y
        self.colour=colour
    @property
    def price(self):
        return 3
    def move_x():
        return [-2,-1,1,2]
    def move_y():
        return [-2,-1,1,2]
class Queen(Figure):
    def __init__(self, current_x, current_y,colour):
        self.current_x = current_x
        self.current_y = current_y
        self.colour=colour
    @property
    def price(self):
        return 7
    def move_x():
        return [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
    def move_y():
        return [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]


class King(Figure):

    def __init__(self, current_x, current_y, colour):
        self.current_x = current_x
        self.current_y = current_y
        self.colour = colour
    def move_x():
        pass

    def move_y():
        pass

    def price():
        pass

class Bishop(Figure):
    def __init__(self, current_x, current_y, colour):
        self.current_x = current_x
        self.current_y = current_y
        self.colour = colour
    def move_x():
        pass
    def move_y():
        pass
    @property
    def price(self):
        return 3








    
    
#-------------------------Інстансіація фігур----------------------------------------------

        
white_pawn1=Pawn(1,2,"white")
white_pawn2=Pawn(2,2,"white")
white_pawn3=Pawn(3,2,"white")
white_pawn4=Pawn(4,2,"white")
white_pawn5=Pawn(5,2,"white")
white_pawn6=Pawn(6,2,"white")
white_pawn7=Pawn(7,2,"white")
white_pawn8=Pawn(8,2,"white")

white_rook1=Rook(1,1,"white")
white_rook2=Rook(8,1,"white")

white_knight1=Knight(2,1,"white")
white_knight2=Knight(7,1,"white")

white_queen=Queen(4,1,"white")

white_king = King(5, 1, "white")

white_bishop1 = Bishop(3, 1, "white")
white_bishop2 = Bishop(6, 1, "white")



black_pawn1=Pawn(1,7,"black")
black_pawn2=Pawn(2,7,"black")
black_pawn3=Pawn(3,7,"black")
black_pawn4=Pawn(4,7,"black")
black_pawn5=Pawn(5,7,"black")
black_pawn6=Pawn(6,7,"black")
black_pawn7=Pawn(7,7,"black")
black_pawn8=Pawn(8,7,"black")

black_rook1=Rook(1,8,"black")
black_rook2=Rook(8,8,"black")

black_knight1=Knight(2,8,"black")
black_knight2=Knight(7,8,"black")

black_queen=Queen(4,8,"black")

black_king = King(5, 8, "black")

black_bishop1 = Bishop(3, 8, "black")
black_bishop2 = Bishop(6, 8, "black")





#-------------------------Дошка----------------------------------------------

class Board:
   pawns_list=[white_pawn1,white_pawn2,white_pawn3,white_pawn4,white_pawn5,white_pawn6,white_pawn7,white_pawn8,black_pawn1,black_pawn2,black_pawn3,black_pawn4,black_pawn5,black_pawn6,black_pawn7,black_pawn8] # список пішаків
   rooks_list=[white_rook1,white_rook2,black_rook1,black_rook2]
   knights_list=[white_knight1, white_knight2,black_knight1,black_knight2]
   queens_list=[white_queen,black_queen]
   kings_list = [white_king, black_king]
   bishop_list = [white_bishop1, white_bishop2, black_bishop1, black_bishop2]
   # окремий двовимірний список всієї дошки і вже на нього звертатися з класів фігур
   _n=8
   _m=8
   board_list=[]
   for i in range(_n):
       board_list.append([0] * _m)  #двомірний масив, заповнений нулями, далі додаються фігури
   for pawn in pawns_list:
       board_list[pawn.current_x-1][pawn.current_y-1]=pawn
   for rook in rooks_list:
       board_list[rook.current_x-1][rook.current_y-1]=rook
   for knight in knights_list:
       board_list[knight.current_x-1][knight.current_y-1]=knight
   for queen in queens_list:
       board_list[queen.current_x-1][queen.current_y-1]=queen
   for king in kings_list:
       board_list[king.current_x - 1][king.current_y - 1] = king
   for bishop in bishop_list:
       board_list[bishop.current_x - 1][bishop.current_y - 1] = bishop

   def Visualise_board(): #не приведено до принципу відкритості-замкненості
      print("----------------------------------------------------------")
      for row in Board.board_list:
         for elem in row:
            if isinstance(elem,Pawn):
               if elem.colour=="white":
                  print("PW",end=' ')
               else:
                  print("PB",end=' ')
            if isinstance(elem,Rook):
               if elem.colour=="white":
                  print("RW",end=' ')
               else:
                  print("RB",end=' ')
            if isinstance(elem,Knight):
               if elem.colour=="white":
                  print("KW",end=' ')
               else:
                  print("KB",end=' ')
            if isinstance(elem,Queen):
               if elem.colour=="white":
                  print("QW",end=' ')
               else:
                  print("QB",end=' ')
                  
            if isinstance(elem, King):
                if elem.colour == "white":
                    print("KW",end=' ')
                else:
                    print("KB",end=' ')
            if isinstance(elem, Bishop):
                if elem.colour == "white":
                    print("BW",end=' ')
                else:
                    print("BB",end=' ')
            if elem ==0:
               print("0", end=' ')
         print()
      print("----------------------------------------------------------")

   def Visualise_restored():
      print("----------------------------------------------------------")
      for row in Board.board_list:
         for elem in row:
            if elem=='P':
               print("PW",end=' ')
            if elem=='B':
               print("BW",end=' ')
            if elem=='$':
               print("KiW",end=' ')
            if elem=='K':
               print("KW",end=' ')
            if elem=='Q':
               print("QW",end=' ')
            if elem=='R':
               print("RW",end=' ')
            if elem=='p':
               print("PB",end=' ')
            if elem=='b':
               print("BB",end=' ')
            if elem=='%':
               print("KiB",end=' ')
            if elem=='k':
               print("KB",end=' ')
            if elem=='q':
               print("QB",end=' ')
            if elem=='r':
               print("RB",end=' ')
            if elem == '0':
               print("0", end=' ')
         print()
      print("----------------------------------------------------------")
#--------------------Класи "Збереження"-------------------------------------------


class Singleton:
    current_player_white=True
   
    endgame=False
   
    def game_loop(self):
      Singleton.current_player_white = not Singleton.current_player_white
      return Singleton.current_player_white


    _singleton = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._singleton: # not None - це True
            cls._singleton = super(Singleton,cls).__new__(cls, *args, **kwargs)
        return cls._singleton
    
game_manager = Singleton()
      

class Saver(Board): #PW -- PB, KW -- KB ...
   def save():
      f = open('file_save.txt', 'w')
      for row in Saver.board_list:  #не приведено до відкритості-замкненості
         for elem in row:
            if isinstance(elem,Pawn):
               if elem.colour=='white':
                  f.write("P")
               if elem.colour=='black':
                  f.write("p")
            if isinstance(elem,Rook):
               if elem.colour=='white':
                  f.write("R")
               if elem.colour=='black':
                  f.write("r")
            if isinstance(elem,Knight):
               if elem.colour=='white':
                  f.write("K")
               if elem.colour=='black':
                  f.write("k")
            if isinstance(elem,Queen):
               if elem.colour=='white':
                  f.write("Q")
               if elem.colour=='black':
                  f.write("q")
            if isinstance(elem,King):
               if elem.colour=='white':
                  f.write("$")
               if elem.colour=='black':
                  f.write("%")
            if isinstance(elem,Bishop):
               if elem.colour=='white':
                  f.write("B")
               if elem.colour=='black':
                  f.write("b")
            if elem ==0:
               f.write("0")
         f.write("\n")
      f.close()
      f1 = open('player_save.txt', 'w')
      if game_manager.current_player_white==True:
         f1.write("1")
      else:
         f1.write("0")

class Restorer(Board):
   def restore_board():
      f = open("file_save.txt")
      count_lines=0
      count_rows=0

      for line in f:
          for elem in line:
              if elem != '\n':
                  Board.board_list[count_lines][count_rows] = elem
                  if count_rows!=7:
                      count_rows+=1
                  else:
                      count_rows = 0
          count_lines+=1
          if count_lines == 8:
              break
      f.close()



#-------------------------Клас Валідації----------------------------------------------


class Move:

    validated=False
    def validation_pawn():
        
        n=0
        is_pawn=False
        for pawn in Board.pawns_list: #якщо вибрана пішка
            
            if pawn.current_x==current_position.get_x_start():
                fixedx=pawn.current_x
                if Board.pawns_list[n].current_y==current_position.get_y_start():
                    fixedy=Board.pawns_list[n].current_y
                    print("You chosed pawn on x=",fixedx,"and y=",fixedy)
                    global x_id #id координат пішака
                    x_id=fixedx
                    global y_id 
                    y_id=fixedy
                    if (game_manager.current_player_white==True and Board.board_list[x_id-1][y_id-1].colour=='white') or (game_manager.current_player_white==False and Board.board_list[x_id-1][y_id-1].colour=='black'): #Чи збігаються кольори ?
                       is_pawn=True
                       print("Matching colour picked!")
                    else:
                       print("No match!!!")
                    break
            n+=1
        if is_pawn==False:
            print("No pawn chosen!")

        if game_manager.current_player_white==True: #в залежності, чий зараз хід
           if (delta_move.x in Pawn.move_x() and delta_move.y in Pawn.move_y()) and is_pawn==True:
               validated=True
           else:
               validated=False
        else:
           if (-delta_move.x in Pawn.move_x() and -delta_move.y in Pawn.move_y()) and is_pawn==True:
               validated=True
           else:
               validated=False    
        return validated
    
    def validation_rook():

        n=0
        is_rook=False
        for rook in Board.rooks_list:

            if rook.current_x==current_position.get_x_start():
                fixedx=rook.current_x
                if Board.rooks_list[n].current_y==current_position.get_y_start():
                    fixedy=Board.rooks_list[n].current_y
                    print("You chosed rook on x=",fixedx,"and y=",fixedy)
                    global x_id
                    x_id=fixedx
                    global y_id
                    y_id=fixedy
                    if (game_manager.current_player_white==True and Board.board_list[x_id-1][y_id-1].colour=='white') or (game_manager.current_player_white==False and Board.board_list[x_id-1][y_id-1].colour=='black'): #Чи збігаються кольори ?
                       is_rook=True
                       print("Matching colour picked!")
                    else:
                       print("No match!!!")
                    break
            n+=1
        if is_rook==False:
            print("No rook chosen!")

        if ((delta_move.x in Rook.move_x() and delta_move.y==0) or (delta_move.x == 0 and delta_move.y in Rook.move_y())) and is_rook==True:
            validated=True
        else:
            validated=False
        return validated

    def validation_knight():
        n=0
        is_knight = False
        for knight in Board.knights_list:  # якщо вибрана пішка
            if knight.current_x == current_position.get_x_start():
                fixedx = knight.current_x
                if Board.knights_list[n].current_y == current_position.get_y_start():
                    fixedy = Board.knights_list[n].current_y
                    print("You chosed knight on x=", fixedx, "and y=", fixedy)
                    is_knight = True
                    global x_id  # id координат пішака
                    x_id = fixedx
                    global y_id
                    y_id = fixedy
                    if (game_manager.current_player_white==True and Board.board_list[x_id-1][y_id-1].colour=='white') or (game_manager.current_player_white==False and Board.board_list[x_id-1][y_id-1].colour=='black'): #Чи збігаються кольори ?
                       is_knight=True
                       print("Matching colour picked!")
                    else:
                       print("No match!!!")
                    break
            n += 1
        if is_knight == False:
            print('No knight chosen')

        if (delta_move.x in Knight.move_x() and delta_move.y in Knight.move_y()) and is_knight == True:
            print('good')
            validated = True
        else:
            validated = False

        return validated

    def validation_queen():

        n = 0
        is_queen = False
        for queen in Board.queens_list:

            if queen.current_x == current_position.get_x_start():
                fixedx = queen.current_x
                if Board.queens_list[n].current_y == current_position.get_y_start():
                    fixedy = Board.queens_list[n].current_y
                    print("You chosed queen on x=", fixedx, "and y=", fixedy)
                    is_queen = True
                    global x_id
                    x_id = fixedx
                    global y_id
                    y_id = fixedy
                    break
            n += 1
        if is_queen == False:
            print("No queen chosen!")

        if ((delta_move.x in Queen.move_x() and delta_move.y == 0) or (
                delta_move.x == 0 and delta_move.y in Rook.move_y()) or (
                math.fabs(delta_move.x)==math.fabs(delta_move.y) )) and is_queen == True:
            validated = True
        else:
            validated = False
        return validated

    def validation_bishop():
        bishopb = False
        k = 0
        for bishop in Board.bishop_list:
            if bishop.current_x == current_position.get_x_start():
                global x_id
                x_id = bishop.current_x
                if Board.bishop_list[k].current_y == current_position.get_y_start():
                    global y_id
                    y_id = Board.bishop_list[k].current_y
                    print("Bishop picked")
                    if (game_manager.current_player_white==True and Board.board_list[x_id-1][y_id-1].colour=='white') or (game_manager.current_player_white==False and Board.board_list[x_id-1][y_id-1].colour=='black'):
                       print("Matching colour picked!")
                       bishopb = True
                    else:
                       print("No match!!!")
                    break
            k += 1
        if (bishopb == True and abs(delta_move.x) == abs(delta_move.y)):
            return True

        else:
            return False
    def validation_king():
        kingb = False
        k = 0
        for king in Board.kings_list:
            if king.current_x == current_position.get_x_start():
                global x_id
                x_id = king.current_x
                if Board.kings_list[k].current_y == current_position.get_y_start():
                    global y_id
                    y_id = Board.kings_list[k].current_y
                    print("King picked")
                    if (game_manager.current_player_white==True and Board.board_list[x_id-1][y_id-1].colour=='white') or (game_manager.current_player_white==False and Board.board_list[x_id-1][y_id-1].colour=='black'):
                       kingb = True
                       print("Matching colour picked!")
                    else:
                        print("No match!!!")
                    break
            k += 1
        if ((abs(delta_move.x) == 1 or abs(delta_move.x) == 0) and (
                abs(delta_move.y == 1) or abs(delta_move.y) == 0) and kingb == True):
            return True
        else:
            return False
      
#----------------------------------------Обробка ходу ----------------


not_restored = int(input("If you want to start a new game -- print 1. If you want to restore game -- print 0: "))    
while game_manager.endgame==False: #цикл гри



   if not_restored==1:   
      endloop=False  
      while endloop==False:   # цикл одного ходу (обробка виключних ситуацій)
         try:
            current_position=Human_Player(int(input("Enter first coord(from):")),int(input("Enter second coord(from):"))) # Перша клітинка, яку обирає користувач
            print("You choosed square",current_position.get_x_start(),current_position.get_y_start())
            print("")
            moving_to= Human_Player(int(input("Enter first coord(to):")),int(input("Enter second coord(to):"))) # Друга клітинка, яку обирає користувач

            print("Figure is going to be moved to:",moving_to.get_x_start(),moving_to.get_y_start())
            delta_move= moving_to - current_position   # Різниця, між обраними клітинками
            print("delta move:",delta_move.x,delta_move.y)



            if delta_move.x==delta_move.y==0:   # Виключні ситуації однакової клітинки і виходу за межі дошки
               raise SameSquareError
            if current_position.get_x_start()>=9 or current_position.get_x_start()<=0 or moving_to.get_y_start()>=9 or moving_to.get_y_start()<=0:         
               raise NotDeskIndexError
               endloop=True

            
            
            if Move.validation_pawn()==True:   #знаходження id пішака в списку пішаків за його координатами
               pawn_id=0
               for pawn in Board.pawns_list:
                  if pawn.current_x == x_id and pawn.current_y == y_id:
                     break
                  pawn_id += 1


            if Move.validation_rook()==True:   #знаходження id тури в списку турів за його координатами
               rook_id=0
               for rook in Board.rooks_list:
                  if rook.current_x == x_id and rook.current_y == y_id:
                     break
                  rook_id += 1
               print(rook_id)

               x_max_unoccupied_minus=0
               x_max_unoccupied_plus=0
               y_max_unoccupied_minus=0
               y_max_unoccupied_plus=0
               delta_move_y_board=[]
               delta_move_x_board=[]

               for y_elem in range(Board.rooks_list[rook_id].current_y-1,0,-1):#  отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по у, у відємному напрямі
                  if Board.board_list[Board.rooks_list[rook_id].current_x-1][y_elem-1] == 0:
                     y_max_unoccupied_minus-=1
                  else:
                     break
               delta_move_y_board.append(y_max_unoccupied_minus)

               for y_elem in range(Board.rooks_list[rook_id].current_y,len(Board.board_list)): #отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по у, у додатньому напрямі
                  if Board.board_list[Board.rooks_list[rook_id].current_x-1][y_elem] == 0:
                     y_max_unoccupied_plus+=1
                  else:
                     break
               delta_move_y_board.append(y_max_unoccupied_plus)
               print("Posible to move in range (y) is ",delta_move_y_board,"Delta move y is ", delta_move.y)


               
               for x_elem in range(Board.rooks_list[rook_id].current_x-1,0,-1): #  отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по x, у відємному напрямі
                  if Board.board_list[x_elem-1][Board.rooks_list[rook_id].current_y-1] == 0:
                     x_max_unoccupied_minus-=1
                     print(x_max_unoccupied_minus)
                  else:
                     break

               delta_move_x_board.append(x_max_unoccupied_minus)
               for x_elem in range(Board.rooks_list[rook_id].current_x,len(Board.board_list)): #отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по x, у додатньому напрямі
                  if Board.board_list[x_elem][Board.rooks_list[rook_id].current_y-1] == 0:
                     x_max_unoccupied_plus+=1
                  else:
                     break
               delta_move_x_board.append(x_max_unoccupied_plus)
               print("Posible to move in range (x) is ",delta_move_x_board,"Delta move x is ", delta_move.x)

            if Move.validation_knight()==True:   #знаходження id konya в списку koney за його координатами
               knight_id=0
               for knight in Board.knights_list:
                  if knight.current_x == x_id and knight.current_y == y_id:
                     break
                  knight_id += 1
               print(knight_id)


            if Move.validation_queen()==True:   #знаходження id konya в списку koney за його координатами
               queen_id=0
               for queen in Board.queens_list:
                  if queen.current_x == x_id and queen.current_y == y_id:
                     break
                  queen_id += 1
               print(queen_id)
               x_max_unoccupied_minus=0
               x_max_unoccupied_plus=0
               y_max_unoccupied_minus=0
               y_max_unoccupied_plus=0
               delta_move_y_board=[]
               delta_move_x_board=[]

               for y_elem in range(Board.queens_list[queen_id].current_y - 1, 0,-1):  # отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по у, у відємному напрямі
                   if Board.board_list[Board.queens_list[queen_id].current_x - 1][y_elem - 1] == 0:
                       y_max_unoccupied_minus -= 1
                   else:
                       break
               delta_move_y_board.append(y_max_unoccupied_minus)

               for y_elem in range(Board.queens_list[queen_id].current_y, len(Board.board_list)):  # отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по у, у додатньому напрямі
                   if Board.board_list[Board.queens_list[queen_id].current_x - 1][y_elem] == 0:
                       y_max_unoccupied_plus += 1
                   else:
                       break
               delta_move_y_board.append(y_max_unoccupied_plus)
               print("Posible to move in range (y) is ", delta_move_y_board, "Delta move y is ", delta_move.y)

               for x_elem in range(Board.queens_list[queen_id].current_x - 1, 0,-1):  # отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по x, у відємному напрямі
                   if Board.board_list[x_elem - 1][Board.queens_list[queen_id].current_y - 1] == 0:
                       x_max_unoccupied_minus -= 1
                       print(x_max_unoccupied_minus)
                   else:
                       break

               delta_move_x_board.append(x_max_unoccupied_minus)
               for x_elem in range(Board.queens_list[queen_id].current_x, len(Board.board_list)):  # отримання максимально можливої, незайнятої фігурами, кількості клітин, які може пройти тура по x, у додатньому напрямі
                   if Board.board_list[x_elem][Board.queens_list[queen_id].current_y - 1] == 0:
                       x_max_unoccupied_plus += 1
                   else:
                       break
               delta_move_x_board.append(x_max_unoccupied_plus)
               print("Posible to move in range (x) is ", delta_move_x_board, "Delta move x is ", delta_move.x)

            if Move.validation_king() == True:
                king_id = 0
                for king in Board.kings_list:
                    if king.current_x == x_id and king.current_y == y_id:
                        break
                    king_id += 1
                print(king_id)


            if Move.validation_bishop() == True:
                bishop_id = 0
                for bishop in Board.bishop_list:
                    if bishop.current_x == x_id and bishop.current_y == y_id:
                        break
                    bishop_id += 1
                print(bishop_id)

                xy_max_unoccupied_minus = 0
                xy_max_unoccupied_plus = 0
                xplusyminus_max_unoccupied_minus = 0
                xminusyplus_max_unoccupied_plus = 0
                delta_move_xy_plus_board = []
                delta_move_xy_minus_board = []
                delta_move_x_plus_y_minus_board = []
                delta_move_x_minus_y_plus_board = []
                for y_elem in range(Board.bishop_list[bishop_id].current_y - 1, 0, -1):  # x-> -, y-> -
                    for x_elem in range(Board.bishop_list[bishop_id].current_x - 1, 0, -1):
                        if y_elem == x_elem:
                            if Board.board_list[x_elem][y_elem] == 0:
                                xy_max_unoccupied_minus += 1
                            else:
                                break
                delta_move_xy_minus_board.append(0)
                delta_move_xy_minus_board.append(xy_max_unoccupied_minus)
                for y_elem in range(Board.bishop_list[bishop_id].current_y - 1, len(Board.board_list)):
                    for x_elem in range(Board.bishop_list[bishop_id].current_x - 1, len(Board.board_list)):
                        if x_elem == y_elem:
                            if Board.board_list[x_elem][y_elem] == 0:
                                xy_max_unoccupied_plus += 1
                            else:
                                break
                delta_move_xy_plus_board.append(0)
                delta_move_xy_plus_board.append(xy_max_unoccupied_plus)
                for y_elem in range(Board.bishop_list[bishop_id].current_y - 1, 0, -1):
                    for x_elem in range(Board.bishop_list[bishop_id].current_x - 1, len(Board.board_list)):
                        if x_elem == y_elem:
                            if Board.board_list[x_elem][y_elem] == 0:
                                xplusyminus_max_unoccupied_minus += 1
                            else:
                                break
                delta_move_x_plus_y_minus_board.append(0)
                delta_move_x_plus_y_minus_board.append(xplusyminus_max_unoccupied_minus)
                for y_elem in range(Board.bishop_list[bishop_id].current_y - 1, len(Board.board_list)):
                    for x_elem in range(Board.bishop_list[bishop_id].current_x - 1, 0, -1):
                        if x_elem == y_elem:
                            if Board.board_list[x_elem][y_elem] == 0:
                                xminusyplus_max_unoccupied_plus += 1
                            else:
                                break
                delta_move_x_minus_y_plus_board.append(0)
                delta_move_x_minus_y_plus_board.append(xminusyplus_max_unoccupied_plus)



            


               
            if Move.validation_pawn()==True: # Хід пішака
               
               print("Pawn validated to move!")
               try:
                  if game_manager.current_player_white==True:
                     if Board.board_list[moving_to.get_x_start()-1][moving_to.get_y_start()-1]==0: 
                        Board.pawns_list[pawn_id]=Pawn(moving_to.get_x_start(),moving_to.get_y_start(),Board.pawns_list[pawn_id].colour)# зміна положення пішака, при правильному ході 
                        Board.board_list[current_position.get_x_start()-1][current_position.get_y_start()-1]=0
                        Board.board_list[moving_to.get_x_start()-1][moving_to.get_y_start()-1]=Board.pawns_list[pawn_id] #зміна положення пішака на дошці
                        endloop=True
                     else:
                        raise AmbiguityError
                  else:
                     if Board.board_list[moving_to.get_x_start()-1][moving_to.get_y_start()-1]==0:
                        Board.pawns_list[pawn_id]=Pawn(moving_to.get_x_start(),moving_to.get_y_start(),Board.pawns_list[pawn_id].colour)# зміна положення пішака, при правильному ході, для чорних
                        Board.board_list[current_position.get_x_start()-1][current_position.get_y_start()-1]=0
                        Board.board_list[moving_to.get_x_start()-1][moving_to.get_y_start()-1]=Board.pawns_list[pawn_id] #зміна положення пішака на дошці
                        endloop=True
                     else:
                        raise AmbiguityError
               except IndexError:
                  print("Error!!! Out of desk")



                  
            elif Move.validation_rook()==True:  # Хід тури

                  if (delta_move.y in range(delta_move_y_board[0],delta_move_y_board[1]+1) and delta_move.y != 0 and delta_move.x==0) or(delta_move.x in range(delta_move_x_board[0],delta_move_x_board[1]+1) and delta_move.x != 0 and delta_move.y==0) :
                     print("Rook validated")
                     Board.rooks_list[rook_id]=Rook(moving_to.get_x_start(),moving_to.get_y_start(),Board.rooks_list[rook_id].colour)# зміна положення тури, при правильному ході 
                     Board.board_list[current_position.get_x_start()-1][current_position.get_y_start()-1]=0
                     Board.board_list[moving_to.get_x_start()-1][moving_to.get_y_start()-1]=Board.rooks_list[rook_id]
                  else:
                     raise MoveError
                  endloop=True
            elif Move.validation_queen()==True:

                  if (delta_move.y in range(delta_move_y_board[0],delta_move_y_board[1]+1) and delta_move.y != 0 and delta_move.x==0) or(delta_move.x in range(delta_move_x_board[0],delta_move_x_board[1]+1) and delta_move.x != 0 and delta_move.y==0) or (math.fabs(delta_move.x)==math.fabs(delta_move.y)):
                     print("Queen validated to move")
                     Board.queens_list[queen_id]=Queen(moving_to.get_x_start(),moving_to.get_y_start(),Board.queens_list[queen_id].colour)# зміна положення тури, при правильному ході
                     Board.board_list[current_position.get_x_start()-1][current_position.get_y_start()-1]=0
                     Board.board_list[moving_to.get_x_start()-1][moving_to.get_y_start()-1]=Board.queens_list[queen_id]
                  else:
                     raise MoveError
                  endloop=True
            elif Move.validation_knight()==True:

                  print("Knight validated to move")
                  try:
                      if game_manager.current_player_white == True:
                          if Board.board_list[moving_to.get_x_start() - 1][moving_to.get_y_start() - 1] == 0:
                              Board.knights_list[knight_id] = Knight(moving_to.get_x_start(), moving_to.get_y_start(),Board.knights_list[knight_id].colour)  # зміна положення konya, при правильному ході
                              Board.board_list[current_position.get_x_start() - 1][current_position.get_y_start() - 1] = 0
                              Board.board_list[moving_to.get_x_start() - 1][moving_to.get_y_start() - 1] =Board.knights_list[knight_id]  # зміна положення konya на дошці
                              endloop = True
                          else:
                              raise AmbiguityError
                      else:
                          if Board.board_list[moving_to.get_x_start() - 1][moving_to.get_y_start() - 1] == 0:
                              Board.knights_list[knight_id] = Knight(moving_to.get_x_start(), moving_to.get_y_start(),Board.knights_list[knight_id].colour)  # зміна положення konya, при правильному ході, для чорних
                              Board.board_list[current_position.get_x_start() - 1][current_position.get_y_start() - 1] = 0
                              Board.board_list[moving_to.get_x_start() - 1][moving_to.get_y_start() - 1] =Board.knights_list[knight_id]  # зміна положення konya на дошці
                              endloop = True
                          else:
                              raise AmbiguityError
                  except IndexError:
                      print("Error!!! Out of desk")
            elif Move.validation_king() == True:
                print("Moving KIng")
                Board.kings_list[king_id] = King(moving_to.get_x_start(), moving_to.get_y_start(),
                                                 Board.kings_list[king_id].color)
                Board.board_list[current_position.get_x_start() - 1][current_position.get_y_start() - 1] = 0
                Board.board_list[moving_to.get_x_start() - 1][moving_to.get_y_start() - 1] = Board.kings_list[king_id]
                endloop = True
            elif Move.validation_bishop() == True:
                if (delta_move.x < 0 and delta_move.y < 0 and abs(delta_move.x) in delta_move_xy_minus_board) or (
                        delta_move.x > 0 and delta_move.y > 0 and delta_move.x in delta_move_xy_plus_board) or (
                        delta_move.x > 0 and delta_move.y < 0 and delta_move.x in delta_move_x_plus_y_minus_board) or (
                        delta_move.x < 0 and delta_move.y > 0 and delta_move.y in delta_move_x_minus_y_plus_board):
                    print("Moving bishop")
                    Board.bishop_list[bishop_id] = Bishop(moving_to.get_x_start(), moving_to.get_y_start(),
                                                          Board.bishop_list[bishop_id].color)
                    Board.board_list[current_position.get_x_start() - 1][current_position.get_y_start() - 1] = 0
                    Board.board_list[moving_to.get_x_start() - 1][moving_to.get_y_start() - 1] = Board.bishop_list[
                        bishop_id]
                else:
                    raise MoveError
                endloop = True
         

         
            

         except AmbiguityError:
            print("Error!!! There is another figure, occupying this square")
         except NotDeskIndexError:
            print("Error!!! Pick index in range from 1 to 8")
         except NoFigureSelectedError:
            print("Error!!! You haven`t selected any figure. Pick one!")
         except MoveError:
            print("Moving Error!!!")
         except SameSquareError:
            print("Error!!! You chosed same square")


         Board.Visualise_board()
         game_manager.game_loop()
         Saver.save()

   if not_restored==0:
      Restorer.restore_board()
      Board.Visualise_restored()
      break

#- - - - - - - - - - - - - Зображення дошки,збереження і зміна гравця- - - - - - - - - - - - - - - -




#--------------------------Сміття---------------------------------------------






'''
print("-----HEIL POROSHENKO----")
print("        _               ")
print("       / /\             ")
print("      / / /             ")
print("     / / /   _          ")
print("    /_/ /   / /\        ")
print("    \ \ \  / /  \       ")
print("     \ \ \/ / /\ \      ")
print("  _   \ \ \/ /\ \ \     ")
print("/_/\   \_\  /  \ \ \    ")
print("\ \ \  / /  \   \_\/    ")
print(" \ \ \/ / /\ \          ")
print("  \ \ \/ /\ \ \         ")
print("   \ \  /  \ \ \        ")
print("    \_\/   / / /        ")
print("          / / /         ")
print("         /_/ /          ")
print("         \_\/           ")
print("-------SIEG HIEL--------")
'''
