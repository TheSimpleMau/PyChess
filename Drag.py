from Board import Board
from PIL import Image, ImageTk, ImageGrab
from time import sleep


class Drag(Board):


    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        #To save the click on the piece that the user wants to move
        self.x_click = None
        self.y_click = None
        #To save the piece to move
        self.pieceToMove = None
        #piece = [ [x moves] , [y moves] , [x+y moves -> [x,y]]]
        self.King = [[100,-100],[100,-100],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Queen = [[100,-100],[100,-100],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Bishop = [[],[],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Knight = [[],[],[[200,100],[200,-100],[-200,-100],[-200,100],[100,200],[100,-200],[-100,-200],[-100,200]]]
        self.Rook = [[100,-100],[100,-100],[]]
        self.Pawn = None #Special case for pawn piece
        self.newPositions = list(self.initial_images_position)
        self.enemyPieces = []
        #To check all the legal moves
        self.bind("<Button 1>",self.legalMoves)
        #To move the actual piece
        self.bind("<Button 2>",self.movePiece)
    

    def reloadBoard(self):
        self.board.delete("all")
        self.squares()
        for piece in self.newPositions:
            self.board.create_image(piece[1][0],piece[1][1],image=self.images[piece[2]])

    def FENgenerator(self):
        x = 50
        y = 50
        for _ in range(8):
            while x < 800:
                self.board.create_rectangle(x,y,x+10,y+10,fill="cyan")
                x+=100
            x = 50
            y += 100


    def getSquareColor(self, event):
        x, y = self.winfo_rootx()+event.x, self.winfo_rooty()+event.y
        image = ImageGrab.grab((x, y, x+1, y+1)) # 1 pixel image
        return image.getpixel((0, 0))

    def getCenter(self,number):
        '''
        This function locates the center of the square where the user selects the piece to move
        '''
        if number > 100:
            return (int(str(number)[-3])*100)+50
        else:
            return 50


    def getClickOrigin(self,eventOrigin):
        '''
        This function locates the actual place where the usere click on the board
        '''
        self.x_click = eventOrigin.x
        self.y_click = eventOrigin.y


    def getPieceToMove(self,event):
        '''
        This function returns the actual piece that the user click on
        '''
        self.getClickOrigin(event)
        self.x_click = self.getCenter(self.x_click)
        self.y_click = self.getCenter(self.y_click)
        for piece in self.newPositions:
            x,y = piece[1]
            if x == self.x_click and y == self.y_click:
                return piece
        return None
        


    def displayMoves(self,currentPosition:list,moves:list,infinity:bool,pieceName:str):
        '''
        This function show to the user all the places where the piece can move
        '''
        self.enemyPieces = []
        def checkLegalMove(nextPosition):
            for position in self.newPositions:
                if nextPosition == position[1]:
                    if (position[0].isupper() and pieceName.isupper()) or (position[0].islower() and pieceName.islower()):
                        return [1,0]
                    elif (position[0].isupper() and pieceName.islower()) or (pieceName.isupper() and position[0].islower()):
                        return [0,1]
                    else:
                        return [0,0]
            return [0,0]

        def searchEnemyPiece(nextPosition):
            for enemyPiece in self.newPositions:
                if nextPosition == enemyPiece[1]:
                    return enemyPiece

        # To obtain the current x and y position of the piece
        currentX = currentPosition[0]
        currentY = currentPosition[1]
        #If the piece can move indefinitely by the board, then we need to creat loops to see how further can go
        if infinity:
            if len(moves[0]) != 0:
                for x in moves[0]:
                    plusX = int(x)
                    rectangleX = self.getCenter(currentX)-50
                    rectangleY = self.getCenter(currentY)-50
                    if x > 0:
                        while currentX+plusX < 800:
                            nextPosition = [currentX+plusX,currentY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX+100,rectangleY,rectangleX+200,rectangleY+100,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX+100,rectangleY,rectangleX+200,rectangleY+100,fill="#476042")
                                plusX+=int(x)
                                rectangleX+=100
                            else:
                                break
                    else:
                        while currentX+plusX > 0:
                            nextPosition = [currentX+plusX,currentY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX-100,rectangleY,rectangleX,rectangleY+100,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX-100,rectangleY,rectangleX,rectangleY+100,fill="#476042")
                                plusX+=int(x)
                                rectangleX-=100
                            else:
                                break
            if len(moves[1]) != 0:
                for y in moves[1]:
                    plusY = int(y)
                    rectangleX = self.getCenter(currentX)-50
                    rectangleY = self.getCenter(currentY)-50
                    if y > 0:
                        while currentY+plusY < 800:
                            nextPosition = [currentX,currentY+plusY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX,rectangleY+100,rectangleX+100,rectangleY+200 ,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX,rectangleY+100,rectangleX+100,rectangleY+200 ,fill="#476042")
                                plusY+=int(y)
                                rectangleY+=100
                            else:
                                break
                    else:
                        notLegalMove =False
                        while currentY+plusY > 0:
                            nextPosition = [currentX,currentY+plusY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX,rectangleY-100,rectangleX+100,rectangleY,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX,rectangleY-100,rectangleX+100,rectangleY,fill="#476042")
                                rectangleY-=100
                                plusY+=int(y)
                            else:
                                break
            if len(moves[2]) != 0:
                for x,y in moves[2]:
                    plusX = x
                    plusY = y
                    rectangleX = self.getCenter(currentX)-50
                    rectangleY = self.getCenter(currentY)-50
                    if x>0 and y>0:
                        notLegalMove = False
                        while (currentX+plusX and currentY+plusY) < 800:
                            nextPosition = [currentX+plusX,currentY+plusY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX+100,rectangleY+100,rectangleX+200,rectangleY+200,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX+100,rectangleY+100,rectangleX+200,rectangleY+200,fill="#476042")
                                plusX+=x
                                plusY+=y
                                rectangleX+=100
                                rectangleY+=100
                            else:
                                break
                    elif x>0 and y<0:
                        notLegalMove = False
                        while currentX+plusX < 800 and currentY+plusY > 0:
                            nextPosition = [currentX+plusX,currentY+plusY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX+100,rectangleY-100,rectangleX+200,rectangleY,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX+100,rectangleY-100,rectangleX+200,rectangleY,fill="#476042")
                                # self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
                                plusX+=x
                                plusY+=y
                                rectangleX+=100
                                rectangleY-=100
                            else:
                                break
                    elif x<0 and y<0:
                        notLegalMove = False
                        while currentX+plusX > 0 and currentY+plusY > 0:
                            nextPosition = [currentX+plusX,currentY+plusY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX-100,rectangleY-100,rectangleX,rectangleY,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX-100,rectangleY-100,rectangleX,rectangleY,fill="#476042")
                                plusX+=x
                                plusY+=y
                                rectangleX-=100
                                rectangleY-=100
                            else:
                                break
                    elif x<0 and y>0:
                        notLegalMove = False
                        while currentX+plusX > 0 and currentY+plusY < 800:
                            nextPosition = [currentX+plusX,currentY+plusY]
                            notLegalMove = checkLegalMove(nextPosition)
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 1:
                                    self.board.create_rectangle(rectangleX-100,rectangleY+100,rectangleX,rectangleY+200,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                                    break
                                self.board.create_rectangle(rectangleX-100,rectangleY+100,rectangleX,rectangleY+200,fill="#476042")
                                plusX+=x
                                plusY+=y
                                rectangleX-=100
                                rectangleY+=100
                            else:
                                break
        #If not, then we only iterate to one place
        else:
            if len(moves[0]) != 0:
                for x in moves[0]:
                    if currentX+x < 800 and currentX+x > 0:
                        rectangleX = self.getCenter(currentX)-50
                        rectangleY = self.getCenter(currentY)-50
                        nextPosition = [currentX+x,currentY]
                        notLegalMove = checkLegalMove(nextPosition)
                        if x>0:
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 0:
                                    self.board.create_rectangle(rectangleX+100,rectangleY,rectangleX+200,rectangleY+100,fill="#476042")
                                else:
                                    self.board.create_rectangle(rectangleX+100,rectangleY,rectangleX+200,rectangleY+100,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                        else:
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 0:
                                    self.board.create_rectangle(rectangleX-100,rectangleY,rectangleX,rectangleY+100,fill="#476042")
                                else:
                                    self.board.create_rectangle(rectangleX-100,rectangleY,rectangleX,rectangleY+100,fill="red")
                                    enemyPiece = searchEnemyPiece(nextPosition)
                                    self.enemyPieces.append(enemyPiece)
                                    self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
            if len(moves[1]) != 0:
                for y in moves[1]:
                    if currentY+y < 800 and currentY+y > 0:
                        rectangleX = self.getCenter(currentX)-50
                        rectangleY = self.getCenter(currentY)-50
                        nextPosition = [currentX,currentY+y]
                        notLegalMove = checkLegalMove(nextPosition)
                        if y>0:
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 0:
                                    self.board.create_rectangle(rectangleX,rectangleY+100,rectangleX+100,rectangleY+200,fill="#476042")
                                else:
                                    if pieceName.lower() != "p":
                                        self.board.create_rectangle(rectangleX,rectangleY+100,rectangleX+100,rectangleY+200,fill="red")
                                        enemyPiece = searchEnemyPiece(nextPosition)
                                        self.enemyPieces.append(enemyPiece)
                                        self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                        else:
                            if notLegalMove[0] == 0:
                                if notLegalMove[1] == 0:
                                    if pieceName.lower() != "p":
                                        self.board.create_rectangle(rectangleX,rectangleY-100,rectangleX+100,rectangleY,fill="#476042")
                                    else:
                                        self.board.create_rectangle(rectangleX,rectangleY-100,rectangleX+100,rectangleY,fill="#476042")
                                        for position in self.initial_images_position:
                                            if position[1] == currentPosition:
                                                self.board.create_rectangle(rectangleX,rectangleY-200,rectangleX+100,rectangleY-100,fill="#476042")
                                                break
                                        
                                else:
                                    if pieceName.lower() != "p":
                                        self.board.create_rectangle(rectangleX,rectangleY-100,rectangleX+100,rectangleY,fill="red")
                                        enemyPiece = searchEnemyPiece(nextPosition)
                                        self.enemyPieces.append(enemyPiece)
                                        self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
            if len(moves[2]) != 0:
                for x,y in moves[2]:
                    if currentX+x<800 and currentY+y<800:
                        rectangleX = self.getCenter(currentX)-50
                        rectangleY = self.getCenter(currentY)-50
                        nextPosition = [currentX+x,currentY+y]
                        notLegalMove = checkLegalMove(nextPosition)
                        if notLegalMove[0] == 0:
                            if notLegalMove[1] == 1:
                                self.board.create_rectangle(rectangleX+x,rectangleY+y,rectangleX+x+100,rectangleY+y+100,fill="red")
                                enemyPiece = searchEnemyPiece(nextPosition)
                                self.enemyPieces.append(enemyPiece)
                                self.board.create_image(nextPosition[0],nextPosition[1],image=self.images[enemyPiece[2]])
                            else:
                                if pieceName.lower() != "p":
                                    self.board.create_rectangle(rectangleX+x,rectangleY+y,rectangleX+x+100,rectangleY+y+100,fill="#476042")



    def legalMoves(self,event):
        '''
        This function show us the legal moves
        '''
        self.reloadBoard()
        piece = self.getPieceToMove(event)
        self.pieceToMove = self.getPieceToMove(event)
        if piece == None:
            print("No piece to move on legal moves")
            return None
        currentPosition = piece[1]
        if piece[0].lower() not in "nkp":
            if piece[0].lower() == "r":
                self.displayMoves(currentPosition,self.Rook,True,piece[0])
            elif piece[0].lower() == "b":
                self.displayMoves(currentPosition,self.Bishop,True,piece[0])
            else: #q
                self.displayMoves(currentPosition,self.Queen,True,piece[0])
        else:
            if piece[0].lower() == "n":
                self.displayMoves(currentPosition,self.Knight,False,piece[0])
            elif piece[0].lower() == "k":
                self.displayMoves(currentPosition,self.King,False,piece[0])
            else: #special case, pawn
                if piece[0].isupper():
                    self.Pawn = [ [], [-100], [[-100,-100],[100,-100]] ]
                else:
                    self.Pawn = [ [], [100], [[-100,100],[100,100]] ]
                self.displayMoves(currentPosition,self.Pawn,False,piece[0])


    def movePiece(self,event):
        squareClicked = self.getSquareColor(event)
        positionClickedCenter = [self.getCenter(event.x),self.getCenter(event.y)]
        # print(squareClicked)
        if squareClicked[0] != 77:
            if len(self.enemyPieces) != 0:
                pass
            else:
                return None
        if self.pieceToMove == None:
            print("No piece to move on move to piece")
            return None
        for enemyPiece in self.enemyPieces:
            if positionClickedCenter == enemyPiece[1]:
                for idx,pieceToDelete in enumerate(self.newPositions):
                    if pieceToDelete == enemyPiece:
                        break
                self.newPositions.pop(idx)
                # self.newPositions.pop(enemyPiece[2])
                # self.legalMoves(event)
                break
        newPosition = [self.pieceToMove[0],positionClickedCenter,self.pieceToMove[2]]
        for idx,piece in enumerate(self.newPositions):
            if newPosition[0] == piece[0] and self.pieceToMove[1] == piece[1]:
                break
        self.newPositions.pop(idx)
        self.newPositions.append(newPosition)
        self.reloadBoard()



if __name__ == '__main__':
    app = Drag()
    app.mainloop()