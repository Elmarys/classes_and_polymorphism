class Reqtangle():
    def __init__ (self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def print_parameters (self):
        return Reqtangle.__name__ + str((self.x, self.y, self.width, self.height))

rectangle_1 = Reqtangle(5,4,3,2)
print(rectangle_1.print_parameters())