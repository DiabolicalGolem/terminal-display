import os, sys

class Display:
    def __init__(self, name):
        self.width = os.get_terminal_size().columns
        self.height = os.get_terminal_size().lines
        self.name = name
    
    def window(self, x, y, w, h, text="", border=False):
        
        return

    def draw(self, border=False):
        draw_array = []
        if border:
            for y in range(self.height):
                line = ""
                for x in range(self.width):
                    if (x >= 2 and x <= self.width - 2) and (y == 0 or y == self.height - 1):
                        line += "─"
                    elif x == 1 and y == 0:
                        line += "┌"
                    elif x == (self.width - 1) and y == 0:
                        line += "┐"
                    elif x == 1 and y == (self.height - 1):
                        line += "└"
                    elif x == (self.width -1) and y == (self.height - 1):
                        line += "┘"
                    elif x == 1 or x == (self.width - 1):
                        line += "│"
                    else:
                        line += " "

                if y == 0:
                    line = line[:3] + f"┤{self.name}├"+ line[len(self.name)+5:]
                sys.stdout.write(line)
        sys.stdout.flush()


    def test(self):
        print(self.width, self.height)

d1 = Display("Display 1")
d1.draw(border=True)
# d1.test()
input()
