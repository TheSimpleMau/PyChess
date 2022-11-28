from tkinter import *
from PvP import *

def nada():
    #TEst
    pass

def displayMainWindow():
    #Display the main window with all the type of games
    mainWindow = Tk()
    mainWindow.geometry("800x800")
    mainWindow.title("PyChess!")
    titleLabel = Label(mainWindow,text="PyChess!")
    titleLabel.pack(pady=100)
    pvpButton = Button(mainWindow,text="Player vs Player mode",command=lambda: pvpMode(mainWindow))
    pvpButton.pack(pady=20)
    pvpButton = Button(mainWindow,text="Player vs AI mode")
    pvpButton.pack(pady=20)
    mainWindow.mainloop()

def pvpMode(window:Tk):
    #initialices the pvp mode
    window.destroy()
    # board = Board()
    pvp = PVP()
    pvp.mainloop()

if __name__ == '__main__':
    displayMainWindow()