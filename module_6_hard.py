class Figure:
    sides_count = 0
    filled=True

    def __init__(self, __color, __sides):
        
        self.__color = __color
        self.__sides = __sides


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
        sides_check = False

        for i in range(len(sides)):
            if isinstance(sides[i], int) and sides[i] > 0:
                sides_check = True
            else:
                sides_check = False

        if (len(sides) + 1) == len(self.__sides)+1 and sides_check:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) + 1 == self.sides_count:
            self.__sides = new_sides
        else:
            pass


class Circle(Figure):
    sides_count = 1
    
    def __init__(self,__color,__sides):
        super().__init__(__color,__sides)
        self.__radius=__sides/6.28
        
    def get_square(self):
        return 3.14 * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3
    
    def __init__(self,__color,__sides):
        super().__init__(__color,__sides)

    def get_square(self):
        p = 1 / 2 * (sum(self.__sides))
        return (p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) ** (1 / 2)


class Cube(Figure):
    sides_count = 12
    def __init__(self,__color,__sides):
        
        super().__init__(__color,__sides)
        
        self.__sides=__sides*12

    def get_volume(self):
        return self.__sides**3
        
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1=Triangle((10,340,20),[2,7,10])

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
#cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
#print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
print(triangle1.get_sides())

