class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if (self.width or self.height) > 50:
            return "Too big for picture."
        
        else:
            picture = []
            row = ""
            for i in range( 0,self.height):
                for i in range(self.width):
                    row = ("*" * self.width)
                picture.append(row)
            shape = "\n".join(picture)
        return shape + "\n"
        
    def get_amount_inside(self, shape):
        if (self.get_area()) >= shape.get_area():
            return self.get_area() // shape.get_area()
        return 0

class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"







