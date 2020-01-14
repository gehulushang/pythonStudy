'''
class Shape(object):
    pass

class Triangle(Shape):
    def draw(self):
        print("三角形")


class Square(Shape):
    def draw(self):
        print("正方形")


s1 = Triangle()
s2 = Square()

s1.draw()
s2.draw()

'''
class Shape(object):
    def draw(self):
        raise NotImplementedError


class Triangle(Shape):
    def draw(self):
        print("三角形")


class Square(Shape):
    def draw(self):
        print("正方形")

class ShapeFactory(object):
    def create(self, shape):
        if shape == 'Tri':
            return Triangle()
        elif shape == 'Squ':
            return Square()
        else:
            return None

fac = ShapeFactory()


obj = fac.create('Tri')

obj.draw()
