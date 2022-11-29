from tkinter import *
from PIL import Image, ImageTk
from os import listdir


#Class to make the board
class Board(Tk):

    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args,**kargs)
        self.geometry("800x800")
        self.resizable(False,False)
        self.board = Canvas(self)
        self.board.pack(fill="both",expand=1)
        self.name_images = listdir("./imgs")
        self.name_images = self.name_images[0:2] + self.name_images[3:]
        self.initial_images_position = []
        self.images = []
        for i in self.name_images:
            if i[0] != '.':
                self.images.append(ImageTk.PhotoImage(Image.open("./imgs/"+i).resize((100,100))))
        # self.img = Image.open("wk.png").resize((100,100))
        # self.img = self.img.convert("P")
        # print(self.img.mode)
        # self.img = ImageTk.PhotoImage(self.img)
        self.squares()
        self.pieces()
        # self.bind("<Button 1>",self.move)

    def squares(self):
        '''
        This function creat the squares of the board
        '''
        for x in range(8):
            for y in range(8):
                if (x+y)%2 == 0:
                    self.board.create_rectangle(x*100,y*100,(x+1)*100,(y+1)*100,fill="white")
                else:
                    self.board.create_rectangle(x*100,y*100,(x+1)*100,(y+1)*100,fill="gray")


    def FENreader(self,notation):
        pass


    def pieces(self) -> None:
        '''
        This function places the pieces on the board
        '''
        # save the index of each pieces in the variable "self.images"
        all_pieces = []
        for idx,i in enumerate(self.name_images):
            if i[0] == "b":
                if i[1] == "r":
                    all_pieces.append(("r",idx))
                elif i[1] == "n":
                    all_pieces.append(("n",idx))
                elif i[1] == "b":
                    all_pieces.append(("b",idx))
                elif i[1] == "k":
                    all_pieces.append(("k",idx))
                elif i[1] == "q":
                    all_pieces.append(("q",idx))
                elif i[1] == "p":
                    all_pieces.append(("p",idx))
            else:
                if i[0] == "R":
                    all_pieces.append(("R",idx))
                elif i[0] == "N":
                    all_pieces.append(("N",idx))
                elif i[0] == "B":
                    all_pieces.append(("B",idx))
                elif i[0] == "K":
                    all_pieces.append(("K",idx))
                elif i[0] == "Q":
                    all_pieces.append(("Q",idx))
                elif i[0] == "P":
                    all_pieces.append(("P",idx))

        x = 50
        y = 50
        # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        for letter in fen:
            if letter == "/":
                x = 50
                y += 100
            elif letter == "8":
                continue
            for piece in all_pieces:
                if letter == piece[0]:
                    self.initial_images_position.append([piece[0],[x,y],piece[1]])
                    self.board.create_image(x,y,image=self.images[piece[1]])
                    x+=100
                    break

        # x = 50
        # y = 50
        # for idx,i in enumerate(self.name_images):
        #     if i[0] == "b" and i[1] != "p":
        #         # self.pieces(self.images[idx],x,y)
        #         self.board.create_image(x,y,image=self.images[idx])
        #         x+=100



if __name__ == '__main__':
    app = Board()
    print(app.initial_images_position)
    app.mainloop()