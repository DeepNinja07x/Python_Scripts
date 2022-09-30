from graphics import *


class Button:
    """activated() and deactivated() and clicked(p) is a method that returns if the user pressed within the required area"""

    def __init__(self, win, center, width, height, label):
        """Create rectangular button e.g qb=Button(myWin,centerPoint,width,height,'Quit')"""
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()

        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h

        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgrey")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        """return true if active and inside p"""
        return (
            self.active
            and self.xmin <= p.getX() <= self.xmax
            and self.ymin <= p.getY() <= self.ymax
        )  # use return when you change an already set variable/variables

    def getLabel(self):
        """label of the string"""
        return self.label.getText()  # here as well

    def activate(self):
        """sets button to active"""
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        """sets button to unactive"""
        self.label.setFill("darkgray")
        self.rect.setWidth(1)
        self.active = False

