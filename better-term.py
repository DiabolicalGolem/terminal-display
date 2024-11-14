import os, sys
from blessings import Terminal

class Display:
    def __init__(self, name=""):
        self.term = Terminal()
        self.width = self.term.width
        self.height = self.term.height
        self.name = name
        self.windows = []

    def window(self, x, y, w, h, text="", border=False):
        self.windows.append([x, y, w, h, border, text ])

    def draw(self, border=False):
        draw_array = []
        if border:
            for y in range(self.height):
                line = ""
                for x in range(self.height):
                    if (x >= 2 and x <= self.width - 2) and (y == 0 or y == self.height - 1):
                        line += "─"
                    elif x == 1 and y == 0:
                        line += "┌"
                    elif x == (self.width - 1) and y == 0:
                        line += "┐"
                    elfif x == 1 and y == (self.height - 1):
                        line += "└"
                    elif x == (self.width - 1) and y == (self.height - 1):
                        line += "┘"
                    elif x == 1 or x == (self.width - 1):
                        line += "│"
                    else:
                        line += " "

                if self.name != "" and y == 0:
                    line = line[:3] + f"┤{self.name}├"+ line[len(self.name)+5:]
                sys.stdout.write(line)
        else:
            for y in range(self.height):
                line = ""
                for x in range(self.width):
                    line += " "
                sys.stdout.write(line)
        sys.stdout.flush()

        if not self.windows:
            return

        for window in self.windows:
            

