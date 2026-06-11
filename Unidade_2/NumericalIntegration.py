# TODO: Create the code to calculate numerical integration using the following methods:
# Fórmulas Newton-Cotes com polinômios de substituição de graus 1 a 3, fórmulas abertas e fechadas.
# Gauss-Legendre com n=2, 3 e 4 pontos
# Gauss-Hermite com n=2, 3 e 4 pontos
# Gauss-Laguerre com n=2, 3  e 4 pontos
# Gauss-chebyshev com n=2, 3 e 4 pontos
# "Dino"  Exponencial simples e Dupla
# Tarefas de integral dupla.

import numpy as np


class Function:
    """Classe que representa a função a ser derivada"""

    @staticmethod
    def f(x):
        return x ** 5 * np.cos(x)


class NumericalIntegration:
    """Classe que implementa os métodos de integração numérica"""
    def __init__(self, xi, xf):
        self.xi = xi
        self.xf = xf

    # =-=-=-=-=-=-=-= Fórmulas Newton-Cotes com polinômios de substituição de graus 1 a 3, fórmulas abertas e fechadas. =-=-=-=-=-=-=-=
    # --------- Abordagem Fechada ---------
    # Regra do trapézio fechada - Grau 1
    def trapezoidal_rule(self):
        h = (self.xf - self.xi)
        
        return (h / 2) * (Function.f(self.xi) + Function.f(self.xf))

    # Simpson 1/3 - Grau 2
    def simpsons_1_3(self):
        h = (self.xf - self.xi) / 2
        
        return (h / 3) * (Function.f(self.xi) + 4 * Function.f(self.xi + h) + Function.f(self.xf))
    
    # Simpson 3/8 - Grau 3
    def simpsons_3_8(self):
        h = (self.xf - self.xi) / 3
        
        return (3 * h / 8) * (Function.f(self.xi) + 3 * Function.f(self.xi + h) + 3 * Function.f(self.xi + 2 * h) + Function.f(self.xf))
    
    # Fórmula sem nome - Grau 4
    def closed_formula_degree_4(self):
        h = (self.xf - self.xi) / 4
        
        return (2 * h / 45) * (7 * Function.f(self.xi) + 32 * Function.f(self.xi + h) + 12 * Function.f(self.xi + 2 * h) + 32 * Function.f(self.xi + 3 * h) + 7 * Function.f(self.xf))
    
    # --------- Abordagem Aberta ---------
    # Regra do Trapézio Aberta - Grau 1
    def open_trapezoidal_rule(self):
        h = (self.xf - self.xi) / 3
        
        return ((3 * h) / 2) * (Function.f(self.xi + h) + Function.f(self.xi + 2 * h))
    
    # Regra de Milne - Grau 2
    def milne_rule(self):
        h = (self.xf - self.xi) / 4
        
        return ((4 * h) / 3) * (2 * Function.f(self.xi + h) - Function.f(self.xi + 2 * h) + 2 * Function.f(self.xi + 3 * h))
    
    # Fórmula sem nome - Grau 3
    def open_formula_degree_3(self):
        h = (self.xf - self.xi) / 5
        
        return ((5 * h) / 24) * (11 * Function.f(self.xi + h) + Function.f(self.xi + 2 * h) + Function.f(self.xi + 3 * h) + 11 * Function.f(self.xi + 4 * h))
    
    def open_formula_degree_4(self):
        h = (self.xf - self.xi) / 6
        
        return ((6 * h) / 20) * (11 * Function.f(self.xi + h) - 14 * Function.f(self.xi + 2 * h) + 26 * Function.f(self.xi + 3 * h) - 14 * Function.f(self.xi + 4 * h) + 11 * Function.f(self.xi + 5* h))
        

if __name__ == "__main__":
    pass