# TODO: Create the code to calculate numerical integration using the following methods:
# Fórmulas Newton-Cotes com polinômios de substituição de graus 1 a 4, fórmulas abertas e fechadas.
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

    # =-=-=-=-=-=-=-= Fórmulas Newton-Cotes com polinômios de substituição de graus 1 a 4, fórmulas abertas e fechadas. =-=-=-=-=-=-=-=
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

    # =-=-=-=-=-=-=-= Gauss-Legendre com n=2, 3 e 4 pontos =-=-=-=-=-=-=-=
    def gauss_legendre(self, n):
        if n == 2:
            points = [-np.sqrt(1/3), np.sqrt(1/3)]
            weights = [1, 1]
        elif n == 3:
            points = [-np.sqrt(3/5), 0, np.sqrt(3/5)]
            weights = [5/9, 8/9, 5/9]
        elif n == 4:
            points = [-np.sqrt((3 + 2 * np.sqrt(6/5)) / 7), -np.sqrt((3 - 2 * np.sqrt(6/5)) / 7), np.sqrt((3 - 2 * np.sqrt(6/5)) / 7), np.sqrt((3 + 2 * np.sqrt(6/5)) / 7)]
            weights = [(18 - np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 - np.sqrt(30)) / 36]
        else:
            raise ValueError("n deve ser 2, 3 ou 4")
        
        # Transformação para o intervalo [xi, xf]
        transformed_points = [((self.xf + self.xi) / 2) + ((self.xf - self.xi) / 2) * p for p in points]
        
        return ((self.xf - self.xi) / 2) * sum(w * Function.f(tp) for w, tp in zip(weights, transformed_points))

    # =-=-=-=-=-=-=-= Gauss-Hermite com n=2, 3 e 4 pontos =-=-=-=-=-=-=-=
    def gauss_hermite(self, n):
        if n == 2:
            points = [-1/np.sqrt(2), 1/np.sqrt(2)]
            weights = [np.sqrt(np.pi)/2, np.sqrt(np.pi)/2]
        elif n == 3:
            points = [-np.sqrt(3/2), 0, np.sqrt(3/2)]
            weights = [np.sqrt(np.pi)/6, 2*np.sqrt(np.pi)/3, np.sqrt(np.pi)/6]
        elif n == 4:
            points = [-np.sqrt((3 + np.sqrt(6)) / 2), -np.sqrt((3 - np.sqrt(6)) / 2), np.sqrt((3 - np.sqrt(6)) / 2), np.sqrt((3 + np.sqrt(6)) / 2)]
            weights = [np.sqrt(np.pi) / (4 * (3 + np.sqrt(6))), np.sqrt(np.pi) / (4 * (3 - np.sqrt(6))), np.sqrt(np.pi) / (4 * (3 - np.sqrt(6))), np.sqrt(np.pi) / (4 * (3 + np.sqrt(6)))]
        else:
            raise ValueError("n deve ser 2, 3 ou 4")
        
        return sum(w * Function.f(p) for w, p in zip(weights, points))

    # =-=-=-=-=-=-=-= Gauss-Laguerre com n=2, 3  e 4 pontos =-=-=-=-=-=-=-=
    def gauss_laguerre(self, n):
        if n == 2:
            points = [2 - np.sqrt(2), 2 + np.sqrt(2)]
            weights = [1/4 * (2 + np.sqrt(2)), 1/4 * (2 - np.sqrt(2))]
        elif n == 3:
            points = [0.4157745568, 2.2942803603, 6.2899450829]
            weights = [0.7110930099, 0.2785177336, 0.0103892565]
        elif n == 4:
            points = [0.322548, 1.74576, 4.53662, 9.39507]
            weights = [0.603154, 0.357419, 0.0388889, 0.000539295]
        else:
            raise ValueError("n deve ser 2, 3 ou 4")
        
        return sum(w * Function.f(p) for w, p in zip(weights, points))
    
    # =-=-=-=-=-=-=-= Gauss-chebyshev com n=2, 3 e 4 pontos =-=-=-=-=-=-=-=
    def gauss_chebyshev(self, n):
        if n == 2:
            points = [-1/np.sqrt(2), 1/np.sqrt(2)]
            weights = [np.pi/2, np.pi/2]
        elif n == 3:
            points = [-np.sqrt(3)/2, 0, np.sqrt(3)/2]
            weights = [np.pi/3, np.pi/3, np.pi/3]
        elif n == 4:
            points = [-np.sqrt((1 + np.sqrt(1/2)) / 2), -np.sqrt((1 - np.sqrt(1/2)) / 2), np.sqrt((1 - np.sqrt(1/2)) / 2), np.sqrt((1 + np.sqrt(1/2)) / 2)]
            weights = [np.pi/4, np.pi/4, np.pi/4, np.pi/4]
        else:
            raise ValueError("n deve ser 2, 3 ou 4")
        
        return sum(w * Function.f(p) for w, p in zip(weights, points))

    # =-=-=-=-=-=-=-= "Dino"  Exponencial simples e Dupla =-=-=-=-=-=-=-=
    def exponential_simple(self, c=5.0, n=1000):
        a = self.xi
        b = self.xf
        
        s = np.linspace(-c, c, n + 1)
        h = (2 * c) / n

        x_s = ((a + b) / 2) + ((b - a) / 2) * np.tanh(s)
        
        dx_ds = ((b - a) / 2) * (1 / np.cosh(s)**2)

        f_bar = Function.f(x_s) * dx_ds
        
        integral = (h / 2) * (f_bar[0] + 2 * np.sum(f_bar[1:-1]) + f_bar[-1])
        
        return integral

    def exponential_double(self, c=3.5, n=1000):
        a = self.xi
        b = self.xf
        
        s = np.linspace(-c, c, n + 1)
        h = (2 * c) / n
        
        inner_term = (np.pi / 2) * np.sinh(s)

        x_s = ((a + b) / 2) + ((b - a) / 2) * np.tanh(inner_term)
        
        dx_ds = ((b - a) / 2) * (np.pi / 2) * (np.cosh(s) / (np.cosh(inner_term)**2))

        f_bar = Function.f(x_s) * dx_ds
        
        integral = (h / 2) * (f_bar[0] + 2 * np.sum(f_bar[1:-1]) + f_bar[-1])
        
        return integral


if __name__ == "__main__":
    xi = 0
    xf = 1
    integration = NumericalIntegration(xi, xf)

    print("Fórmulas Newton-Cotes:")
    print("Trapézio (fechada):", integration.trapezoidal_rule())
    print("Simpson 1/3:", integration.simpsons_1_3())
    print("Simpson 3/8:", integration.simpsons_3_8())
    print("Fórmula fechada grau 4:", integration.closed_formula_degree_4())
    print("Trapézio (aberta):", integration.open_trapezoidal_rule())
    print("Milne:", integration.milne_rule())
    print("Fórmula aberta grau 3:", integration.open_formula_degree_3())
    print("Fórmula aberta grau 4:", integration.open_formula_degree_4())

    print("\nGauss-Legendre:")
    for n in [2, 3, 4]:
        print(f"n={n}:", integration.gauss_legendre(n))

    print("\nGauss-Hermite:")
    for n in [2, 3, 4]:
        print(f"n={n}:", integration.gauss_hermite(n))

    print("\nGauss-Laguerre:")
    for n in [2, 3, 4]:
        print(f"n={n}:", integration.gauss_laguerre(n))

    print("\nGauss-Chebyshev:")
    for n in [2, 3, 4]:
        print(f"n={n}:", integration.gauss_chebyshev(n))

    print("\nExponencial Simples e Dupla:")
    print("Exponencial Simples:", integration.exponential_simple())
    print("Exponencial Dupla:", integration.exponential_double())