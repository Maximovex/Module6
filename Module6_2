class Vehicle:
    
    
    __color_variants =['red','blue','yellow','white']
    
    def __init__(self,owner,__model,__color,__engine_power):
        self.owner=owner
        self.__model=__model
        self.__engine_power=__engine_power
        self.__color=__color
    def get_model(self):
        return f'Модель: {self.__model}'
    def get_horsepower(self):
        return f'Мощность: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'
        
    def set_color(self,new_color):
        if new_color.lower() in self.__color_variants:
            self.__color=new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')
    
    def print_info(self):
        print(self.get_model(),self.get_horsepower(),self.get_color(),self.owner,sep='\n')

class Sedan(Vehicle):
    __passengers_limit=5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()


