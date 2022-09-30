from graphics import *


class DieView:
    # shows graphical representation of a 6 sided dice
    def __init__(self, win, center, size):
        # create a view of the die e.g. d1=DieView(myWin,Point(40,50),20) its centered at 40,50 and length of 20
        self.win = win
        self.background = "white"  # color of face
        self.foreground = "black"  # Thats for the pips
        self.psize = 0.1 * size  # radius of each pip
        hsize = size / 2.0  # size of die
        offset = 0.6 * hsize  # distance from center to other pips
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # create 7 circles
        self.pip1 = self.__makePip(cx - offset, cy - offset)
        self.pip2 = self.__makePip(cx - offset, cy)
        self.pip3 = self.__makePip(cx - offset, cy + offset)
        self.pip4 = self.__makePip(cx, cy)
        self.pip5 = self.__makePip(cx + offset, cy - offset)
        self.pip6 = self.__makePip(cx + offset, cy)
        self.pip7 = self.__makePip(cx + offset, cy + offset)

        # draw an initial value
        self.setValue(1)

    def __makePip(self, x, y):
        # Internal helper method to draw a pip at (x,y)
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        # set this to display value
        # turn all pips off
        self.pip1.setFill(self.background)
        self.pip2.setFill(self.background)
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background)
        self.pip5.setFill(self.background)
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        # turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)

