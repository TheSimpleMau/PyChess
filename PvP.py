# from tkinter import *
from Board import *
from Drag import *

blackRookQueen = 56
blackKnightQueen = 57
blackBishopQueen = 58
blackQueen = 59
blackKing = 60
blackRookKing = 61
blackKnightKing = 62
blackBishopKing = 63
blackPawns = [i for i in range(48,56)]

#White pieces
whiteRookQueen = 0
whiteKnightQueen = 1
whiteBishopQueen = 2
whiteQueen = 3
whiteKing = 4
whiteRookKing = 5
whiteKnightKing = 6
whiteBishopKing = 7
whitePawns = [i for i in range(8,16)]


class PVP(Board):

    def __init__(self,*args,**kargs) -> None:
        super().__init__(*args,**kargs)
        #colorPieceSide = initial position
        #Black pieces initial positions
        self.blackRookQueen = 56
        self.blackKnightQueen = 57
        self.blackBishopQueen = 58
        self.blackQueen = 59
        self.blackKing = 60
        self.blackRookKing = 61
        self.blackKnightKing = 62
        self.blackBishopKing = 63
        self.blackPawns = [i for i in range(48,56)]

        # self.blackPieces = [56,57,58,59,60,61,62,63,[i for i in range(48,56)]]

        #White pieces initial positions
        self.whiteRookQueen = 0
        self.whiteKnightQueen = 1
        self.whiteBishopQueen = 2
        self.whiteQueen = 3
        self.whiteKing = 4
        self.whiteRookKing = 5
        self.whiteKnightKing = 6
        self.whiteBishopKing = 7
        self.whitePawns = [i for i in range(8,16)]

        # self.whitePieces = [0,1,2,3,4,5,6,7,[i for i in range(8,16)]]
        
        #Creat board
        self.squares()
        self.title("PvP mode!")

        #Black pieces posisioning
        x_count = 50
        y_count = 50
        for piece in range(56,64):
            self.coso = Button(self,text=f"{piece}",height=1,width=1)
            self.coso.place(x=x_count,y=y_count)
            x_count+=100
        x_count = 50
        y_count = 150
        for piece in range(48,56):
            self.coso = Button(self,text=f"{piece}",height=1,width=1)
            self.coso.place(x=x_count,y=y_count)
            x_count+=100
    
        #White pieces posisioning
        x_count = 50
        y_count = 650
        for piece in range(8,16):
            self.coso = Button(self,text=f"{piece}",height=1,width=1)
            self.coso.place(x=x_count,y=y_count)
            x_count+=100
        x_count = 50
        y_count = 750
        for piece in range(8):
            self.coso = Button(self,text=f"{piece}",height=1,width=1)
            self.coso.place(x=x_count,y=y_count)
            x_count+=100
