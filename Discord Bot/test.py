import wsav
import pickle
class test:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    def getID(self):
        return self.id
    def getX(self):
        return self.x
    def getY(self):
        return self.y

e = []
e.append(test(2, 2, 2))
e.append(test(2, 2, 2))
e.append(test(2, 2, 2))
e.append(test(2, 2, 2))

wsav.Save(e)
h = wsav.Load(e)
print(h)