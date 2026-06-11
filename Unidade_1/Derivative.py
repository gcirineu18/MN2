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
        error_order = int(input("Choose the 'error_order' value (1 - O(h) | 2 - O(h^2) | 3 - O(h^3) | 4 - O(h^4)): "))
        match error_order:
            case 1:
                match derivative_order:
                    case 1:
                        return (Function.f(self.x + self.delta_x) - Function.f(self.x)) / self.delta_x
                    case 2:
                        return (Function.f(self.x + 2 * self.delta_x) - 2 * Function.f(self.x + self.delta_x) + Function.f(self.x)) / (self.delta_x ** 2)
                    case 3:
                        return (Function.f(self.x + 3 * self.delta_x) - 3 * Function.f(self.x + 2 * self.delta_x) + 3 * Function.f(self.x + self.delta_x) - Function.f(self.x)) / (self.delta_x ** 3)
                    case 4:
                        return (Function.f(self.x + 4 * self.delta_x) - 4 * Function.f(self.x + 3 * self.delta_x) + 6 * Function.f(self.x + 2 * self.delta_x) - 4 * Function.f(self.x + self.delta_x) + Function.f(self.x)) / (self.delta_x ** 4)
                    case _:
                        return "Invalid derivative order!"
            case 2:
                match derivative_order:
                    case 1:
                        return (-Function.f(self.x + 2 * self.delta_x) + 4 * Function.f(self.x + self.delta_x) - 3 * Function.f(self.x)) / (2 * self.delta_x)
                    case 2:
                        return (2 * Function.f(self.x) - 5 * Function.f(self.x + self.delta_x) + 4 * Function.f(self.x + 2 * self.delta_x) - Function.f(self.x + 3 * self.delta_x))/ (self.delta_x ** 2)
                    case 3:
                        return (-2.5 * Function.f(self.x) + 9 * Function.f(self.x+self.delta_x) - 12 * Function.f(self.x + 2 * self.self.delta_x) + 7 * Function.f(self.x + 3 * self.delta_x) - 1.5 * Function.f(self.x + 4 * self.delta_x))/(self.delta_x ** 3)
                    case _:                            
                        return "Invalid derivative order!"
            case 3:
                match derivative_order:
                    case 1:
                        return (-11 * Function.f(self.x) + 18 * Function.f(self.x + self.delta_x) - 9 * Function.f(self.x + 2 * self.delta_x) + 2 * Function.f(self.x + 3 * self.delta_x))/(6 * self.delta_x)
                    case 2:
                        return (35 * Function.f(self.x) - 104 * Function.f(self.x + self.delta_x) + 114 * Function.f(self.x + 2 * self.delta_x) - 56 * Function.f(self.x + 3 * self.delta_x) + 11 * Function.f(self.x + 4 * self.delta_x))/(12 * (self.delta_x ** 2))
                    case 3:
                        return (-23 * Function.f(self.x) + 95 * Function.f(self.x + self.delta_x) - 154 * Function.f(self.x + 2 * self.delta_x) + 122 * Function.f(self.x + 3 * self.delta_x) - 47 * Function.f(self.x + 4 * self.delta_x) + 7 * Function.f(self.x + 5 * self.delta_x))/(4 * (self.delta_x ** 3))
                    case _:                            
                        return "Invalid derivative order!"
            case 4:
                match derivative_order:
                    case 1:
                        return (-3 * Function.f(self.x + 4 * self.delta_x) + 16 * Function.f(self.x + 3 * self.delta_x) - 36 * Function.f(self.x + 2 * self.delta_x) + 48 * Function.f(self.x + self.delta_x) - 25 * Function.f(self.x)) / (12 * self.delta_x)
                    case 2:
                        return (45 * Function.f(self.x) - 154 * Function.f(self.x + self.delta_x) + 214 * Function.f(self.x + 2 * self.delta_x) - 156 * Function.f(self.x + 3 * self.delta_x) + 61 * Function.f(self.x + 4 * self.delta_x) - 10 * Function.f(self.x + 5 * self.delta_x)) / (12 * (self.delta_x ** 2))
                    case 3:
                        return (-61 * Function.f(self.x) + 280 * Function.f(self.x + self.delta_x) - 533 * Function.f(self.x + 2 * self.delta_x) + 544 * Function.f(self.x + 3 * self.delta_x) - 319 * Function.f(self.x + 4 * self.delta_x) + 104 * Function.f(self.x + 5 * self.delta_x) - 15 * Function.f(self.x + 6 * self.delta_x)) / (8 * (self.delta_x ** 3))
                    case _:                            
                        return "Invalid derivative order!"
            case _:                
                return "Invalid error order!"

    def backward_derivative(self):
        """Calcula a derivada usando a filosofia Backward"""
        derivative_order = int(input("Choose the 'derivative_order' value (1 - First | 2 - Second | 3 - Third | 4 - Fourth): "))
        error_order = int(input("Choose the 'error_order' value (1 - O(h) | 2 - O(h^2) | 3 - O(h^3) | 4 - O(h^4)): "))
        match error_order:
            case 1:
                match derivative_order:
                    case 1:
                        return (Function.f(self.x) - Function.f(self.x - self.delta_x)) / self.delta_x
                    case 2:
                        return (Function.f(self.x) - 2 * Function.f(self.x - self.delta_x) + Function.f(self.x - 2 * self.delta_x)) / (self.delta_x ** 2)
                    case 3:
                        return (Function.f(self.x) - 3 * Function.f(self.x - self.delta_x) + 3 * Function.f(self.x - 2 * self.delta_x) - Function.f(self.x - 3 * self.delta_x)) / (self.delta_x ** 3)
                    case 4:
                        return (Function.f(self.x) - 4 * Function.f(self.x - self.delta_x) + 6 * Function.f(self.x - 2 * self.delta_x) - 4 * Function.f(self.x - 3 * self.delta_x) + Function.f(self.x - 4 * self.delta_x)) / (self.delta_x ** 4)
                    case _:
                        return "Invalid derivative order!"
            case 2:
                match derivative_order:
                    case 1:
                        return (3 * Function.f(self.x) - 4 * Function.f(self.x - self.delta_x) + Function.f(self.x - 2 * self.delta_x)) / (2 * self.delta_x)
                    case 2:
                        return (2 * Function.f(self.x) - 5 * Function.f(self.x - self.delta_x) + 4 * Function.f(self.x - 2 * self.delta_x) - Function.f(self.x - 3 * self.delta_x)) / (self.delta_x ** 2)
                    case 3:
                        return (2.5 * Function.f(self.x) - 9 * Function.f(self.x - self.delta_x) + 12 * Function.f(self.x - 2 * self.delta_x) - 7 * Function.f(self.x - 3 * self.delta_x) + 1.5 * Function.f(self.x - 4 * self.delta_x)) / (self.delta_x ** 3)
                    case 4:
                        return (35 * Function.f(self.x) - 104 * Function.f(self.x - self.delta_x) + 114 * Function.f(self.x - 2 * self.delta_x) - 56 * Function.f(self.x - 3 * self.delta_x) + 11 * Function.f(self.x - 4 * self.delta_x)) / (12 * (self.delta_x ** 4))
                    case _:
                        return "Invalid derivative order!"
            case 3:
                match derivative_order:
                    case 1:
                        return (11 * Function.f(self.x) - 18 * Function.f(self.x - self.delta_x) + 9 * Function.f(self.x - 2 * self.delta_x) - 2 * Function.f(self.x - 3 * self.delta_x)) / (6 * self.delta_x)
                    case 2:
                        return (35 * Function.f(self.x) - 104 * Function.f(self.x - self.delta_x) + 114 * Function.f(self.x - 2 * self.delta_x) - 56 * Function.f(self.x - 3 * self.delta_x) + 11 * Function.f(self.x - 4 * self.delta_x)) / (12 * (self.delta_x ** 2))
                    case 3:
                        return (23 * Function.f(self.x) - 95 * Function.f(self.x - self.delta_x) + 154 * Function.f(self.x - 2 * self.delta_x) - 122 * Function.f(self.x - 3 * self.delta_x) + 47 * Function.f(self.x - 4 * self.delta_x) - 7 * Function.f(self.x - 5 * self.delta_x)) / (4 * (self.delta_x ** 3))
                    case 4:
                        return ((35/6)  * Function.f(self.x) - 31 * Function.f(self.x - self.delta_x) + (137/2) * Function.f(self.x - 2 * self.delta_x) - (242/3) * Function.f(self.x - 3 * self.delta_x) + (107/2) * Function.f(self.x - 4 * self.delta_x) - 19 * Function.f(self.x - 5 * self.delta_x) + (17/6) * Function.f(self.x - 6 * self.delta_x)) / (self.delta_x ** 4)
                    case _:
                        return "Invalid derivative order!"
            case 4:
                match derivative_order:
                    case 1:
                        return (25 * Function.f(self.x) - 48 * Function.f(self.x - self.delta_x) + 36 * Function.f(self.x - 2 * self.delta_x) - 16 * Function.f(self.x - 3 * self.delta_x) + 3 * Function.f(self.x - 4 * self.delta_x)) / (12 * self.delta_x)
                    case 2:
                        return (45 * Function.f(self.x) - 154 * Function.f(self.x - self.delta_x) + 214 * Function.f(self.x - 2 * self.delta_x) - 156 * Function.f(self.x - 3 * self.delta_x) + 61 * Function.f(self.x - 4 * self.delta_x) - 10 * Function.f(self.x - 5 * self.delta_x)) / (12 * (self.delta_x ** 2))
                    case 3:
                        return (61 * Function.f(self.x) - 280 * Function.f(self.x - self.delta_x) + 533 * Function.f(self.x - 2 * self.delta_x) - 544 * Function.f(self.x - 3 * self.delta_x) + 319 * Function.f(self.x - 4 * self.delta_x) - 104 * Function.f(self.x - 5 * self.delta_x) + 15 * Function.f(self.x - 6 * self.delta_x)) / (8 * (self.delta_x ** 3))
                    case 4:
                        return ((28/3) * Function.f(self.x) - (111/2) * Function.f(self.x - self.delta_x) + 142 * Function.f(self.x - 2 * self.delta_x) - (1219/6) * Function.f(self.x - 3 * self.delta_x) + 176 * Function.f(self.x - 4 * self.delta_x) - (185/2) * Function.f(self.x - 5 * self.delta_x) + (82/3) * Function.f(self.x - 6 * self.delta_x) - (7/2) * Function.f(self.x - 7 * self.delta_x)) / (self.delta_x ** 4)
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
