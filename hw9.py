class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            raise ValueError
        self.x1 = x1; self.x2 = x2;
        self.y1 = y1; self.y2 = y2;
        self.lt = (x1, y1)
        self.rb = (x2, y2)

    def show(self):
        print(f"좌측 상단 꼭짓점이 {self.lt}이고, ", end="")
        print(f"우측 하단 꼭짓점이 {self.rb}인 사각형입니다.")

    def getWidth(self):
        width = self.x2 - self.x1
        return width

    def getHeight(self):
        height = self.y2 - self.y1
        return height

    def getArea(self):
        area = self.getWidth() * self.getHeight()
        return area

    def getPerimeter(self):
        perimeter = self.getWidth()*2 + self.getHeight()*2
        return perimeter

r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f"\n넓이는 {a}, 둘레는 {p}")
