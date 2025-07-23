from cell import Cell
import time
class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()

    def __create_cells(self):
        for col in range(0, self.__num_cols):
            self.__cells.append([])
            for row in range(0, self.__num_rows):
                cell = Cell(self.__win)
                self.__cells[col].append(cell)
                if self.__win != None:
                    self.__draw_cell(col, row)
  
    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        x2 = x1 + self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        y2 = y1 + self.__cell_size_y
        self.__cells[i][j].draw(x1, x2, y1, y2)
        self.__animate()
    
    def __animate(self):
        if self.__win != None:
            self.__win.redraw()
        time.sleep(0.05)