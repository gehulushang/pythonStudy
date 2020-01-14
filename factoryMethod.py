class AbstractShape(object):
    def __init__(self, info):
        self.info = info

    def draw(self):
        raise NotImplementedError


class Triangle(AbstractShape):
    def draw(self):
        print("三角形")

    def pri(self):
        print(self.info)


class Square(AbstractShape):
    def draw(self):
        print("正方形")

    def pri(self):
        print(self.info)


class AbstractFactory(object):
    def create(self):
        pass


class TriangleFactory(AbstractFactory):
    info = "triFactory"

    def create(self):
        return Triangle(self.info)


class SquareFactory(AbstractFactory):
    info = "squFactory"

    def create(self):
        return Square(self.info)


squareFactory = SquareFactory()
triangleFactory = TriangleFactory()

print(squareFactory.info)
print(triangleFactory.info)

square = squareFactory.create()
triangle = triangleFactory.create()

square.draw()
square.pri()
triangle.draw()
triangle.pri()

