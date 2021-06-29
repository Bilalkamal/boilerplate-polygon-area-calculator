class Rectangle:
    def __init__(self, width,height):
        self.width = width
        self.height = height
        
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    def get_area(self):
        return self.height * self.width
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def get_picture(self):
        if self.width > 50 or self.height >50: return "Too big for picture."
        pic = ""
        for i in range(self.height):
            pic += "*"*self.width + "\n"
        return pic
    def get_amount_inside(self,polygon):
        return int(self.width/polygon.width)*int(self.height/polygon.height)
    def __repr__(self):
       return self.__str__()   
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
    def __init__(self, side,):
        super().__init__(side, side)
    def set_width(self,new_width):
        self.width = new_width
        self.height = new_width
    def set_height(self,new_height):
        self.width = new_height
        self.height = new_height
    def set_side(self,new_side):
        self.set_height(new_side)
    def __repr__(self):
       return self.__str__()   
    def __str__(self):
        return f"Square(side={self.width})"

