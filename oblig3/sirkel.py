#Et program tegner en rød sirkel.
from ezgraphics import GraphicsWindow

win = GraphicsWindow(400,200)

c = win.canvas()

c.setOutline("red")
c.setFill(255, 0, 100)

c.setColor("red")

c.drawOval(45, 45, 90, 90)

win.wait()
