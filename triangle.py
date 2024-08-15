import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

def plot_triangle(sides,fill=False, color='blue'):
    # Calculate vertices based on given sides
    vertices = [(0, 0), (sides[0], 0), (sides[2] * np.cos(np.arccos((sides[1]**2 + sides[2]**2 - sides[0]**2)/(2 * sides[1] * sides[2]))), sides[2])]

    fig, ax = plt.subplots()
    triangle = Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(triangle)
    ax.set_xlim(-1, max(sides) + 1)
    ax.set_ylim(-1, max(sides) + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f'Triangle')
    plt.grid(True)

    return fig


def plot_triangle_with_area(sides, area, fill=False, color='blue'):
    # Calculate vertices based on given sides
    vertices = [(0, 0), (sides[0], 0), (sides[2] * np.cos(np.arccos((sides[1]**2 + sides[2]**2 - sides[0]**2)/(2 * sides[1] * sides[2]))), sides[2])]

    fig, ax = plt.subplots()
    triangle = Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(triangle)
    ax.text(sides[0] / 2, -0.5, f'Area: {area:.2f}', ha='center', va='center')
    ax.set_xlim(-1, max(sides) + 1)
    ax.set_ylim(-1, max(sides) + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f'Triangle with Area: {area:.2f}')
    plt.grid(True)

    return fig


def plot_triangle_with_perimeter_or_circumference(sides,fill,color='blue'):
  # Calculate vertices based on given sides
    vertices = [(0, 0), (sides[0], 0), (sides[2] * np.cos(np.arccos((sides[1]**2 + sides[2]**2 - sides[0]**2)/(2 * sides[1] * sides[2]))), sides[2])]

    fig, ax = plt.subplots()
    triangle = Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(triangle)
    perimeter=sum(sides)
    ax.text(sides[0] / 2, -0.5, f'Perimeter: {perimeter:.2f}', ha='center', va='center')
    ax.set_xlim(-1, max(sides) + 1)
    ax.set_ylim(-1, max(sides) + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f'Triangle with Perimeter: {perimeter:.2f}')
    plt.grid(True)

    return fig