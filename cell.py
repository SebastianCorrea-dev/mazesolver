from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
    
    def draw(self, x1, x2, y1, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self.__win.draw_line(line)
        
        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self.__win.draw_line(line)
        
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self.__win.draw_line(line)
        
        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self.__win.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        midpointOne_x = self.__x1 + abs(self.__x2 - self.__x1)//2
        midpointOne_y = self.__y1 + abs(self.__y2 - self.__y1)//2
        centerOne = Point(midpointOne_x, midpointOne_y)

        midpointTwo_x = to_cell.__x1 + abs(to_cell.__x2 - to_cell.__x1)//2
        midpointTwo_y = to_cell.__y1 + abs(to_cell.__y2 - to_cell.__y1)//2
        centerTwo = Point(midpointTwo_x, midpointTwo_y)

        line = Line(centerOne, centerTwo)
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"
        self.__win.draw_line(line, fill_color)