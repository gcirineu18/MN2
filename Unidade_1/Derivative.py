import numpy as np
#TODO: Colocar as ordens de erro para cada método
# Forward: falta 0(h^2), 0(h^3), 0(h^4)
# Backward: falta 0(h^2), 0(h^3), 0(h^4)
# Central: falta 0(h^1), 0(h^3), 0(h^4)

class Function:
    """Classe que representa a função a ser derivada"""

    @staticmethod
    def f(x):
        return x ** 5 * np.cos(x)


class Derivative:
    """Classe para calcular derivadas usando diferentes filosofias"""

    def __init__(self, x: float, delta_x: float):
        self.x = x
        self.delta_x = delta_x

    def calculate(self):
        """Calcula a derivada baseado na filosofia escolhida"""
        philosophy = int(input("Choose the 'philosophy' value (1 - Forward | 2 - Backward | 3 - Central): "))
        match philosophy:
            case 1:
                return self.forward_derivative()
            case 2:
                return self.backward_derivative()
            case 3:
                return self.central_derivative()
            case _:
                return "Unknown philosophy!"

    def forward_derivative(self):
        """Calcula a derivada usando a filosofia Forward"""
        derivative_order = int(input("Choose the 'derivative_order' value (1 - First | 2 - Second | 3 - Third | 4 - Fourth): "))
        match derivative_order:
            case 1:
                return (Function.f(self.x + self.delta_x) - Function.f(self.x)) / self.delta_x
            case 2:
                return (Function.f(self.x + (2 * self.delta_x)) - (2 * Function.f(self.x + self.delta_x)) + Function.f(self.x)) / (self.delta_x ** 2)
            case 3:
                return (Function.f(self.x + (3 * self.delta_x)) - (3 * Function.f(self.x + (2 * self.delta_x))) + (3 * Function.f(self.x + self.delta_x)) - Function.f(self.x)) / (self.delta_x ** 3)
            case 4:
                return (Function.f(self.x + (4 * self.delta_x)) - (4 * Function.f(self.x + (3 * self.delta_x))) + (6 * Function.f(self.x + (2 * self.delta_x))) - (4 * Function.f(self.x + self.delta_x)) + Function.f(self.x)) / (self.delta_x ** 4)
            case _:
                return "Invalid derivative order!"

    def backward_derivative(self):
        """Calcula a derivada usando a filosofia Backward"""
        derivative_order = int(input("Choose the 'derivative_order' value (1 - First | 2 - Second | 3 - Third | 4 - Fourth): "))
        match derivative_order:
            case 1:
                return (Function.f(self.x) - Function.f(self.x - self.delta_x)) / self.delta_x
            case 2:
                return (Function.f(self.x) - (2 * Function.f(self.x - self.delta_x)) + Function.f(self.x - (2 * self.delta_x))) / (self.delta_x ** 2)
            case 3:
                return (Function.f(self.x) - (3 * Function.f(self.x - self.delta_x)) + (3 * Function.f(self.x - (2 * self.delta_x))) - Function.f(self.x - (3 * self.delta_x))) / (self.delta_x ** 3)
            case 4:
                return (Function.f(self.x) - (4 * Function.f(self.x - self.delta_x)) + (6 * Function.f(self.x - (2 * self.delta_x))) - (4 * Function.f(self.x - (3 * self.delta_x))) + Function.f(self.x - (4 * self.delta_x))) / (self.delta_x ** 4)
            case _:
                return "Invalid derivative order!"

    def central_derivative(self):
        """Calcula a derivada usando a filosofia Central"""
        derivative_order = int(input("Choose the 'derivative_order' value (1 - First | 2 - Second | 3 - Third | 4 - Fourth): "))
        match derivative_order:
            case 1:
                return (Function.f(self.x + self.delta_x) - Function.f(self.x - self.delta_x)) / (2 * self.delta_x)
            case 2:
                return (Function.f(self.x + self.delta_x) - (2 * Function.f(self.x)) + Function.f(self.x - self.delta_x)) / (self.delta_x ** 2)
            case 3:
                return (Function.f(self.x + (2 * self.delta_x)) - (2 * Function.f(self.x + self.delta_x)) + (2 * Function.f(self.x - self.delta_x)) - Function.f(self.x - (2 * self.delta_x))) / (2 * (self.delta_x ** 3))
            case 4:
                return (Function.f(self.x + (2 * self.delta_x)) - (4 * Function.f(self.x + self.delta_x)) + (6 * Function.f(self.x)) - (4 * Function.f(self.x - self.delta_x)) + Function.f(self.x - (2 * self.delta_x))) / (self.delta_x ** 4)
            case _:
                return "Invalid derivative order!"


if __name__ == "__main__":
    x = np.pi / 2
    delta_x = 0.0001

    derivative_calculator = Derivative(x, delta_x)
    result = derivative_calculator.calculate()

    print(f"The result of the derivative is: {result}")
