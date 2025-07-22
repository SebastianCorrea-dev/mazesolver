from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    
    c1 = Cell(win)
    c1.draw(50,100,50,100)

    c2 = Cell(win)
    c2.draw(125,175,50,200)

    c1.draw_move(c2)

    win.wait_for_close()
main()