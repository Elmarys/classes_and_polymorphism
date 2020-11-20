from rectangle import Rectangle,Square,Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)
circle_1 = Circle(5)

print(square_1.get_area_square(),
      square_2.get_area_square())

shapes = [rect_1, rect_2, square_1, square_2, circle_1]

for shape in shapes:
    if isinstance(shape,Square):
        print(shape.get_area_square())
    elif isinstance(shape,Rectangle):
        print(shape.get_area())
    else:
        print(shape.get_area_circle())