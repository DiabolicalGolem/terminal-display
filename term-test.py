import os, sys
from blessings import Terminal

class Window:
    def __init__(self, x, y, w, h, border=False):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.border = border
    
    def wrap(self, text):
        words = text.split()
        
        wrap_array = [""]
        line = 0
        for word in words:
            if (len(wrap_array[line]) + len(word) + 1 ) <= self.w - (self.border*2):
                wrap_array[line] += " "+word
            else:
                line +=1
                wrap_array.append(word)

        for i in range(len(wrap_array) - self.border):
            wrap_array[i] = wrap_array[i].strip()

        return wrap_array[:self.h - (self.border*2)]

    def build(self, text=""):
        out = self.wrap(text)
        if self.border:
            out.insert(0,"┌"+"─"*(self.w-2)+"┐")
            for i in range(1,len(out)):
                out[i] = "│"+out[i]+" "*(self.w-len(out[i])-2)+"│"

                if len(out) < self.h-1:
                    out.append("│"+" "*(self.w-2)+"│")
            out.append("└"+"─"*(self.w-2)+"┘")
        else:
            pass
        return (self.x, self.y, out, self.border)

class Display:
    def __init__(self, name=""):
        self.term = Terminal()
        self.width = self.term.width
        self.height = self.term.height
        self.name = name
        self.windows = []
    
    def build_window(self, x, y, w, h, text="", border=False):
        window = Window(x, y, w, h, border)
        self.windows.append(window.build(text))

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
        
        # Draw windows
        if not self.windows:
            return

        for window in self.windows:
            for i in range(len(window[2])):
                with self.term.location(window[0], window[1]+i):
                    sys.stdout.write(window[2][i])
        sys.stdout.flush()


    def test(self):
        print(self.width, self.height)

d1 = Display("Display 1")
d1.build_window(20,10,20,20,"Testing Testing testing the limits of my word-wrap program. So far, its going well! Will it do one more?",True)
d1.build_window(0,5,20,10,"Testing Testing testing the limits of my word-wrap program. So far, its going well! Will it do one more? This is without borders")

d1.draw(border=True)
# d1.draw()
# d1.test()
input()
