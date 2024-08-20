import numpy as np
import matplotlib.pyplot as plt
from sympy import (symbols, sympify, lambdify, solve, diff, integrate, latex,
                   limit, series, Matrix, solveset, Eq, factorial, summation,
                   product, expand, factor, simplify, trigsimp, cse, N, S)
from sympy.parsing.sympy_parser import parse_expr
from sympy.calculus.util import continuous_domain
from sympy.plotting import plot3d, PlotGrid
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class AdvancedEquationSolver:
    def __init__(self, equation_str):
        self.x, self.y, self.z = symbols('x y z')
        try:
            self.expr = parse_expr(equation_str)
        except Exception as e:
            raise ValueError(f"Invalid equation format: {str(e)}")

    def plot(self, x_range=(-10, 10), num_points=1000):
        try:
            f = lambdify(self.x, self.expr, modules=['numpy', 'sympy'])
            x_vals = np.linspace(x_range[0], x_range[1], num_points)
            y_vals = f(x_vals)

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(x_vals, y_vals, label=f'y = {self.expr}', color='blue')
            ax.set_title(f"Plot of y = {self.expr}")
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.axhline(y=0, color='k', linestyle='--', linewidth=0.5)
            ax.axvline(x=0, color='k', linestyle='--', linewidth=0.5)
            ax.grid(True, linestyle=':', alpha=0.7)
            ax.legend()

            y_min, y_max = np.min(y_vals), np.max(y_vals)
            margin = 0.1 * (y_max - y_min)
            ax.set_ylim(y_min - margin, y_max + margin)

            return fig
        except Exception as e:
            raise RuntimeError(f"An error occurred while plotting: {str(e)}")

    def solve(self):
        try:
            solutions = solve(self.expr, self.x, dict=True)
            return solutions
        except Exception as e:
            raise RuntimeError(f"An error occurred while solving the equation: {str(e)}")

    def derivative(self):
        try:
            derivative_expr = diff(self.expr, self.x)
            return derivative_expr
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the derivative: {str(e)}")

    def integral(self):
        try:
            integral_expr = integrate(self.expr, self.x)
            return integral_expr
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the integral: {str(e)}")

    def calculate_limit(self, point=0):
        try:
            return limit(self.expr, self.x, point)
        except Exception as e:
            raise RuntimeError(f"Error calculating limit: {str(e)}")

    def calculate_series(self, point=0, n=5):
        try:
            return series(self.expr, self.x, point, n)
        except Exception as e:
            raise RuntimeError(f"Error calculating series: {str(e)}")

    def find_domain(self):
        try:
            return continuous_domain(self.expr, self.x, S.Reals)
        except Exception as e:
            raise RuntimeError(f"Error finding domain: {str(e)}")

    def simplify_expression(self):
        try:
            return simplify(self.expr)
        except Exception as e:
            raise RuntimeError(f"Error simplifying expression: {str(e)}")

    def factor_expression(self):
        try:
            return factor(self.expr)
        except Exception as e:
            raise RuntimeError(f"Error factoring expression: {str(e)}")

    def expand_expression(self):
        try:
            return expand(self.expr)
        except Exception as e:
            raise RuntimeError(f"Error expanding expression: {str(e)}")

    def plot_3d(self, range_x=(-5, 5), range_y=(-5, 5), num_points=100):
        try:
            x, y = symbols('x y')
            f = lambdify((x, y), self.expr, 'numpy')
            
            x = np.linspace(range_x[0], range_x[1], num_points)
            y = np.linspace(range_y[0], range_y[1], num_points)
            X, Y = np.meshgrid(x, y)
            
            Z = f(X, Y)
            
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            surface = ax.plot_surface(X, Y, Z, cmap='viridis')
            
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.set_title(f"3D Plot of z = {self.expr}")
            
            fig.colorbar(surface, shrink=0.5, aspect=5)
            
            return fig
        except Exception as e:
            raise RuntimeError(f"Error plotting 3D graph: {str(e)}")
