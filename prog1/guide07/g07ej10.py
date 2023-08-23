# Usando las clases Operacion y Suma, definir otra que se llame Promedio y utilizarla

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def operate(self):
        pass

class Sum(Operation):
    def operate(self, firstNumber: int, secondNumber: int) -> int:
        return firstNumber + secondNumber

class Average(Sum):
    def __init__(self, numbers) -> None:
        self.numbers = numbers

    def calculate(self):
        total = 0
        for i in range(len(self.numbers)):
            number = self.numbers[i]
            total = self.operate(total, number)
        
        return total / len(self.numbers)

numbers = [1, 2, 3]

average = Average(numbers)
result = average.calculate()

print(result)
# Esto resultará en un TypeError, ya que la clase MiClaseAbstracta es abstracta y no puede ser instanciada directamente.
# objeto_abstracto = MiClaseAbstracta()

# class Operation:
#     def __init__(self, firstNumber, secondNumber):
#         self.firstNumber = firstNumber
#         self.secondNumber = secondNumber

#     def solveTwo(self, firstNumber, secondNumber):
#         return firstNumber / secondNumber