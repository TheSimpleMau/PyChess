from Board import Board
from PIL import Image, ImageTk
from time import sleep

class Drag(Board):

    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        self.x_click = None
        self.y_click = None
        self.move_image = None
        #piece = [ [x moves] , [y moves] , [x+y moves -> [x,y]]]
        self.King = [[100,-100],[100,-100],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Queen = [[100,-100],[100,-100],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Bishop = [[],[],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Knight = [[],[],[[200,100],[200,-100],[-200,-100],[-200,100],[100,200],[100,-200],[-100,-200],[-100,200]]]
        self.Rook = [[100,-100],[100,-100],[]]
        self.Pawn = None #Special case for pawn piece
        self.bind("<Button 1>",self.movePiece)

    def getCenter(self,number):
        if number > 100:
            return (int(str(number)[-3])*100)+50
        else:
            return 50

    def getClickOrigin(self,eventOrigin):
        self.x_click = eventOrigin.x
        self.y_click = eventOrigin.y

    def getPieceToMove(self,event):
        self.getClickOrigin(event)
        self.x_click = self.getCenter(self.x_click)
        self.y_click = self.getCenter(self.y_click)
        for piece in self.initial_images_position:
            x,y = piece[1]
            if x == self.x_click and y == self.y_click:
                return piece

    def displayMoves(self,currentPosition:list,moves:list,infinity:bool,idxOfImage:int):
        currentX = currentPosition[0]
        currentY = currentPosition[1]
        if infinity:
            if len(moves[0]) != 0:
                for x in moves[0]:
                    plusX = int(x)
                    if x > 0:
                        while currentX+plusX < 800:
                            self.board.create_image(currentX+plusX,currentY,image=self.images[idxOfImage])
                            plusX+=int(x)
                    else:
                        while currentX+plusX > 0:
                            self.board.create_image(currentX+plusX,currentY,image=self.images[idxOfImage])
                            plusX+=int(x)
            if len(moves[1]) != 0:
                for y in moves[1]:
                    plusY = int(y)
                    if y > 0:
                        while currentY+plusY < 800:
                            self.board.create_image(currentX,currentY+plusY,image=self.images[idxOfImage])
                            plusY+=int(y)
                    else:
                        while currentY+plusY > 0:
                            self.board.create_image(currentX,currentY+plusY,image=self.images[idxOfImage])
                            plusY+=int(y)
            if len(moves[2]) != 0:
                for x,y in moves[2]:
                    plusX = x
                    plusY = y
                    if x>0 and y>0:
                        while (currentX+plusX and currentY+plusY) < 800:
                            self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
                            plusX+=x
                            plusY+=y
                    elif x>0 and y<0:
                        while currentX+plusX < 800 and currentY+plusY > 0:
                            self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
                            plusX+=x
                            plusY+=y
                    elif x<0 and y<0:
                        while currentX+plusX > 0 and currentY+plusY > 0:
                            self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
                            plusX+=x
                            plusY+=y
                    elif x<0 and y>0:
                        while currentX+plusX > 0 and currentY+plusY < 800:
                            self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
                            plusX+=x
                            plusY+=y
        else:
            if len(moves[0]) != 0:
                for x in moves[0]:
                    if currentX+x < 800 and currentX+x > 0:
                        self.board.create_image(currentX+x,currentY,image=self.images[idxOfImage])
            if len(moves[1]) != 0:
                for y in moves[1]:
                    if currentY+y < 800 and currentY+y > 0:
                        self.board.create_image(currentX,currentY+y,image=self.images[idxOfImage])
            
            if len(moves[2]) != 0:
                for x,y in moves[2]:
                    if currentX+x<800 and currentY+y<800:
                        self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
                    elif currentX+x<800 and currentY+y>0:
                        self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
                    elif currentX+x>0 and currentY+y>0:
                        self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
                    elif currentX+x>0 and currentY+y<800:
                        self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
            



                # canvas.create_oval(x, y, x, y, width = 0, fill = 'white')

    def legalMoves(self,event):
        piece = self.getPieceToMove(event)
        currentPosition = piece[1]
        if piece[0].lower() not in "nkp":
            if piece[0].lower() == "r":
                self.displayMoves(currentPosition,self.Rook,True,piece[2])
            elif piece[0].lower() == "b":
                self.displayMoves(currentPosition,self.Bishop,True,piece[2])
            else: #q
                self.displayMoves(currentPosition,self.Queen,True,piece[2])
        else:
            if piece[0].lower() == "n":
                self.displayMoves(currentPosition,self.Knight,False,piece[2])
            elif piece[0].lower() == "k":
                self.displayMoves(currentPosition,self.King,False,piece[2])
            else: #special case, pawn
                if piece[0] == "P":
                    self.Pawn = [ [], [-100], [[-100,-100],[100,-100]] ]
                else:
                    self.Pawn = [ [], [100], [[-100,100],[100,100]] ]
                self.displayMoves(currentPosition,self.Pawn,False,piece[2])



    def movePiece(self,event):
        piece = self.getPieceToMove(event)
        self.legalMoves(event)
        # self.move_image = self.images[piece[2]]
        # self.move_image = self.board.create_image(event.x,event.y,image=self.move_image)
            
        # self.move_image = ImageTk.PhotoImage(Image.open(f"./imgs/{}"))




if __name__ == '__main__':
    app = Drag()
    app.mainloop()