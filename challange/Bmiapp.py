from abc import ABC , abstractmethod

class Person(ABC):
    def __init__(self ,name,age,weight,height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self._weight = value

    @propery
    def height(self):
        return self._height
    @height.setter
    def heiight(self,value):
        if value < 0:
            raise ValueError("height cannot be negative")
        self._height = value
    @abstractmethod
    def calculate_bmi(self):
        pass
    @abstractmethod
    def get_bmi_category(self):
        pass
    def print_info(self):
        print(f"{self.name}, age:{self.age}, weight:{self.weight} kg, height:{self.height},"
              f"BMI{self.calculate_bmi():.2f}, category:{self.get_bmi_category()}")