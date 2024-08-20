import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify, solve, diff, integrate, latex


class EquationSolver:
    def __init__(self, equation_str):
        self.x = symbols('x')
        try:
            self.expr = sympify(equation_str)
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
            solutions = solve(self.expr, self.x)
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

