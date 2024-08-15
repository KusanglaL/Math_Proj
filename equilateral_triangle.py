import matplotlib.pyplot as plt
import numpy as np

def plot_equilateral_triangle(side, fill, color='blue'):
    # Calculate the height of the equilateral triangle
    height = (np.sqrt(3) / 2) * side

    # Define the vertices of the equilateral triangle
    vertices = [
        [1, 1],
        [1+side , 1],
        [1+side/2, 1+height]
    ]
    fig, ax = plt.subplots()
    triangle = plt.Polygon(vertices, fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)
    ax.set_xlim(0, side + 3)
    ax.set_ylim(0, height + 3)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Equilateral Triangle with Side Length: {side}")
    return fig

def plot_equilateral_triangle_with_area(side, fill, color='blue'):
    # Calculate the height of the equilateral triangle
    height = (np.sqrt(3) / 2) * side

    # Define the vertices of the equilateral triangle
    vertices = [
        [-side / 2, 0],
        [side / 2, 0],
        [0, height]
    ]
    fig, ax = plt.subplots()
    triangle = plt.Polygon(vertices, fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)
    area = (3 * np.sqrt(3) * (side**2)) / 2
    ax.text(0, 0, f'Area: {area:.2f}', ha='center', va='center')
    ax.set_xlim(-side / 2 - 1, side / 2 + 1)
    ax.set_ylim(0, height + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Equilateral Triangle with Area: {area}")
    return fig

def plot_equilateral_triangle_with_perimeter_or_circumference(side, fill, color='blue'):
    # Calculate the height of the equilateral triangle
    height = (np.sqrt(3) / 2) * side

    # Define the vertices of the equilateral triangle
    vertices = [
        [-side / 2, 0],
        [side / 2, 0],
        [0, height]
    ]
    fig, ax = plt.subplots()
    triangle = plt.Polygon(vertices, fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)
    perimeter=3*side
    ax.text(0, 0, f'Perimeter: {perimeter:.2f}', ha='center', va='center')
    ax.set_xlim(-side / 2 - 1, side / 2 + 1)
    ax.set_ylim(0, height + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Equilateral Triangle with Perimeter: {perimeter}")
    return fig

