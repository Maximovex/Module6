class Figure:
    sides_count = 0
    filled=True

    def __init__(self, __color, *__sides):
        self.__color = __color
        
        if len(list(__sides))==self.sides_count:
            self.__sides=list(__sides)
        else:
            self.__sides=[1]*self.sides_count
    
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
        if len(sides) == len(self.__sides) and sides_check:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self.sides_count==1:
            return sum(self.__sides)
        elif self.sides_count==12:
            return sum(self.get_sides())
        else:
            return sum(self.__sides)

    def set_sides(self, *new_sides):
        
        if len(new_sides) == self.sides_count:
            self.__sides=list(new_sides)
        elif len(new_sides) ==1 and self.sides_count==12:
            self.__sides=list(new_sides*12)
        else:
            pass


class Circle(Figure):
    sides_count = 1
    
    def __init__(self,__color,__sides):
        super().__init__(__color,__sides)
        self.__sides=super().get_sides()
        self.__radius=self.__sides[0]/6.28
        
    def get_square(self):
        return 3.14 * self.__radius ** 2
        

class Triangle(Figure):
    sides_count = 3
    
    def __init__(self,__color,__sides):
        super().__init__(__color,__sides)
        self.__sides=super().get_sides()
        
    def get_square(self):
        p = (sum(self.get_sides()))/2
        return (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** (1 / 2)


class Cube(Figure):
    sides_count = 12
    
    def __init__(self,__color,__sides):
        super().__init__(__color,__sides)
        self.__sides=self.get_sides()
        
    
    def get_sides(self):
        
        return super().get_sides()

    def get_volume(self):
        return self.get_sides()[0]**3
        
circle1 = Circle((200, 200, 100), 20) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1=Triangle((10,340,20),(15,30,10))
triangle1.set_sides(35,30,20,5)
print(triangle1.get_sides())

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
cube1.set_sides(15) # Изменится

print(cube1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(len(triangle1))
print(len(cube1))
# Проверка объёма (куба):
print(cube1.get_volume())
print(triangle1.get_square())
