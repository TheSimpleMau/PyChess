from Board import Board
from PIL import Image, ImageTk
from time import sleep


class Drag(Board):


    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        #To save the click on the piece that the user wants to move
        self.x_click = None
        self.y_click = None
        #To save the image of the piece to move
        self.move_image = None
        #piece = [ [x moves] , [y moves] , [x+y moves -> [x,y]]]
        self.King = [[100,-100],[100,-100],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Queen = [[100,-100],[100,-100],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Bishop = [[],[],[[100,100],[-100,-100],[100,-100],[-100,100]]]
        self.Knight = [[],[],[[200,100],[200,-100],[-200,-100],[-200,100],[100,200],[100,-200],[-100,-200],[-100,200]]]
        self.Rook = [[100,-100],[100,-100],[]]
        self.Pawn = None #Special case for pawn piece 
        #To move the actual piece
        self.bind("<Button 1>",self.movePiece)


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
        for piece in self.initial_images_position:
            x,y = piece[1]
            if x == self.x_click and y == self.y_click:
                return piece


    def displayMoves(self,currentPosition:list,moves:list,infinity:bool,idxOfImage:int):
        '''
        This function show to the user all the places where the piece can move
        '''
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
                        notLegalMove = False
                        while currentX+plusX < 800:
                            nextPosition = [currentX+plusX,currentY]
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
                                self.board.create_rectangle(rectangleX+100,rectangleY,rectangleX+200,rectangleY+100,fill="#476042")
                                plusX+=int(x)
                                rectangleX+=100
                            else:
                                break
                    else:
                        notLegalMove = False
                        while currentX+plusX > 0:
                            nextPosition = [currentX+plusX,currentY]
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
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
                        notLegalMove = False
                        while currentY+plusY < 800:
                            nextPosition = [currentX,currentY+plusY]
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
                                self.board.create_rectangle(rectangleX,rectangleY+100,rectangleX+100,rectangleY+200 ,fill="#476042")
                                plusY+=int(y)
                                rectangleY+=100
                            else:
                                break
                    else:
                        notLegalMove =False
                        while currentY+plusY > 0:
                            nextPosition = [currentX,currentY+plusY]
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
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
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
                                self.board.create_rectangle(rectangleX+100,rectangleY+100,rectangleX+200,rectangleY+200,fill="#476042")
                                # self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
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
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
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
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
                                self.board.create_rectangle(rectangleX-100,rectangleY-100,rectangleX,rectangleY,fill="#476042")
                                # self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
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
                            for position in self.initial_images_position:
                                if nextPosition == position[1]:
                                    notLegalMove = True
                            if not notLegalMove:
                                self.board.create_rectangle(rectangleX-100,rectangleY+100,rectangleX,rectangleY+200,fill="#476042")
                                # self.board.create_image(currentX+plusX,currentY+plusY,image=self.images[idxOfImage])
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
                    notLegalMove = False
                    if currentX+x < 800 and currentX+x > 0:
                        rectangleX = self.getCenter(currentX)-50
                        rectangleY = self.getCenter(currentY)-50
                        nextPosition = [currentX+x,currentY]
                        for position in self.initial_images_position:
                            if nextPosition == position[1]:
                                notLegalMove = True
                        if x>0 and not notLegalMove:
                            self.board.create_rectangle(rectangleX+100,rectangleY,rectangleX+200,rectangleY+100,fill="#476042")
                        elif x<0 and not notLegalMove:
                            self.board.create_rectangle(rectangleX-100,rectangleY,rectangleX,rectangleY+100,fill="#476042")
                        else:
                            continue
            if len(moves[1]) != 0:
                for y in moves[1]:
                    notLegalMove = False
                    if currentY+y < 800 and currentY+y > 0:
                        rectangleX = self.getCenter(currentX)-50
                        rectangleY = self.getCenter(currentY)-50
                        nextPosition = [currentX,currentY+y]
                        for position in self.initial_images_position:
                            if nextPosition == position[1]:
                                notLegalMove = True
                        if y>0 and not notLegalMove:
                            self.board.create_rectangle(rectangleX,rectangleY+100,rectangleX+100,rectangleY+200,fill="#476042")
                        elif y<0 and not notLegalMove:
                            self.board.create_rectangle(rectangleX,rectangleY-100,rectangleX+100,rectangleY,fill="#476042")
                        else:
                            continue
            if len(moves[2]) != 0:
                for x,y in moves[2]:
                    notLegalMove = False
                    if currentX+x<800 and currentY+y<800:
                        rectangleX = self.getCenter(currentX)-50
                        rectangleY = self.getCenter(currentY)-50
                        nextPosition = [currentX+x,currentY+y]
                        for position in self.initial_images_position:
                            if nextPosition == position[1]:
                                notLegalMove = True
                        if not notLegalMove:
                            self.board.create_rectangle(rectangleX+x,rectangleY+y,rectangleX+x+100,rectangleY+y+100,fill="#476042")
                        else:
                            continue
                        # self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
                    
                    ######################################################################
                    #### CHECK IF THIS PART WORKS WHIOUT ALL THE CODE BELOW COMMENTED ####
                    ######################################################################
                    # elif currentX+x<800 and currentY+y>0:
                    #     pass
                        # self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
                        # self.board.create_rectangle(rectangleX,rectangleY,rectangleX,rectangleY,fill="#476042")
                    # elif currentX+x>0 and currentY+y>0:
                    #     pass
                        # self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
                        # self.board.create_rectangle(rectangleX,rectangleY,rectangleX,rectangleY,fill="#476042")
                    # elif currentX+x>0 and currentY+y<800:
                    #     pass
                        # self.board.create_image(currentX+x,currentY+y,image=self.images[idxOfImage])
                        # self.board.create_rectangle(rectangleX,rectangleY,rectangleX,rectangleY,fill="#476042")


    def legalMoves(self,event):
        '''
        This function show us the legal moves that could move the piece
        '''
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
        '''
        Function to move the piece
        '''
        # piece = self.getPieceToMove(event)
        self.legalMoves(event)




if __name__ == '__main__':
    app = Drag()
    app.mainloop()