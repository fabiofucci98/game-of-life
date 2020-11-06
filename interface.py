from tkinter import *
from tkinter.font import Font
from game import *


class Interface(object):

    def __init__(self):
        self.game = Game()
        self.create_interface()
        self.root.mainloop()

    def create_interface(self):
        # create root
        self.root = Tk()
        self.root.title("Game of life")
        self.root.resizable(False, False)

        # create frame
        self.frame = Frame(self.root, width=720, height=780)
        self.frame.pack()

        # create canvas
        self.canvas = Canvas(self.frame, width=720, height=780)
        self.canvas.bind("<Button-1>", self.change_color_on_click)
        self.canvas.pack()

        # create custom font for buttons
        font = Font(size=20)

        # create start button, height = 42 width = 168
        start_button = Button(self.frame, text="START", width=10,
                              height=1, command=self.start_game)
        start_button.place(x=40, y=720)
        start_button['font'] = font
        self.start_button = start_button

        # create stop button, height = 42 width = 168
        stop_button = Button(self.frame, text="STOP", width=10,
                             height=1, command=self.stop_game)

        stop_button.place(x=276, y=720)
        stop_button['font'] = font
        self.stop_button = stop_button

        # create reset button, height = 42 width = 168
        reset_button = Button(self.frame, text="RESET", width=10,
                              height=1, command=self.reset_game)
        reset_button.place(x=512, y=720)
        reset_button['font'] = font
        self.reset_button = reset_button

        # create grid
        self.rectangles = []
        x = 20
        for i in range(self.game.grid_height):
            self.rectangles.append([])
            y = 20
            for j in range(self.game.grid_lenght):
                rect = self.canvas.create_rectangle(
                    x, y, x+20, y+20, fill="white")
                self.rectangles[i].append(rect)
                y += 20
            x += 20

    def start_game(self):
        if not self.game.is_playing:
            self.game.is_playing = True
            self.play()
            self.game.is_playing = False

    def stop_game(self):
        if self.game.is_playing:
            self.game.is_playing = False

    def reset_game(self):
        # reset game state
        self.game.is_playing = False
        # reset game grid
        for i in range(self.game.grid_height):
            for j in range(self.game.grid_lenght):
                self.canvas.itemconfig(self.rectangles[i][j], fill="white")

    def change_color_on_click(self, event):
        if self.game.is_playing:
            return
        if event.x < 20 or event.x > 700 or event.y < 20 or event.y > 700:
            return
        x = int((event.x - event.x % 10)/20-1)
        y = int((event.y - event.y % 10)/20-1)
        try:
            if self.canvas.itemcget(self.rectangles[x][y], "fill") == "black":
                self.canvas.itemconfig(self.rectangles[x][y], fill="white")
            else:
                self.canvas.itemconfig(self.rectangles[x][y], fill="black")

        except IndexError:
            return

    def play(self):
        grid = []
        for i in range(self.game.grid_height):
            grid.append([])
            for j in range(self.game.grid_lenght):
                color = self.canvas.itemcget(self.rectangles[j][i], "fill")
                state = 0 if color == "white" else 1
                grid[i].append(state)
        self.game.set_grid(grid)
        for grid in self.game.play():
            self.root.after(200, self.update(grid))
            self.root.update()

    def update(self, grid):
        for i in range(self.game.grid_height):
            for j in range(self.game.grid_lenght):
                color = "black" if grid[i][j] == 1 else "white"
                self.canvas.itemconfig(
                    self.rectangles[j][i], fill=color)
