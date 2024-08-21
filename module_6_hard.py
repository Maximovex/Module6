class Figure:
    sides_count = 0

    def __init__(self, __sides, __color, filled=True):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
        return self.__color

    def is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def is_valid_sides(self, *sides):
        sides_check=False

        for i in range(len(sides)):
            if isinstance(sides[i], int) and sides[i]>0:
                sides_check=True
            else:
                sides_check=False

        if (len(sides) + 1) == self.__sides and sides_check:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self,*new_sides):
        if range(new_sides)+1 == self.sides_count:
            self.__sides=new_sides
        else:
            pass

class Circle(Figure):
    sides_count = 1
    __radius=super().__sides[0]/6,28
    def get_square(self):
        return 3,14*self.__radius**2


class Triangle(Figure):
    sides_count = 3
    def get_square(self):


class Cube(Figure):
    sides_count = 12
