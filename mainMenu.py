import sys
from tkinter import *

"""This ia the code for the main menu for the D3 Robot Game. IT NEEDS THHESE MODULES IN ORDER TO WORK:
Text1.png, moreInfo.py, FinalCode.py"""

########################################################################################################################
class Menu:
    def __init__(self, root):
        self.root = root
        
        root.title("D3 Virtual Robot game")

        #All text should be written in Fixedsys.
        
        self.label = Label(self.root, text = "D3 VIRTUAL ROBOT", font = ("Fixedsys", 32), bg = "#666666",fg = "white")
        self.label.pack()
        
        self.frame = Frame (self.root)
        self.frame.pack(fill = BOTH, expand = True)

        self.button1 = Button(self.frame, text = "Play", font=("Fixedsys", 18),bg = "green", command = self.play)
        self.button2 = Button(self.frame, text = "More info", font=("Fixedsys", 18),bg = "blue", command = self.info)
        self.button3 = Button(self.frame, text = "Quit", font=("Fixedsys", 18),bg = "red", command = self.close)
        self.button4 = Button(self.frame, text = "Another Game", font=("Fixedsys", 18),bg = "yellow", command = self.game)

        self.button3.pack(side = BOTTOM)
        self.button4.pack(side = BOTTOM)
        self.button2.pack(side = BOTTOM)
        self.button1.pack(side = BOTTOM)

        self.label = Label(self.root, font = ("Fixedsys"), bg = "green")
        self.label.pack(fill = BOTH, expand = True)

    #Another game
    def game(self):
        sys.exit(main())
    #Exit   
    def close(self):
        sys.exit() 
    #Play
    def play(self):
        import FinalCode

         ##########   importing the actual game.   ########## 
        
    #More information
    def info(self):
        import moreInfo

         ##########   importing the more information module.   ########## 
        

def main():
    root = Tk()
    root.geometry("%dx%d" % (600, 400))
    gui = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    sys.exit(main())

