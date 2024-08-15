import matplotlib.pyplot as plt
import numpy as np
def plot_rhombus(d1, d2, fill=False, color='blue'):
    fig, ax = plt.subplots()
    rhombus = plt.Polygon([[0, d1 / 2], [d2 / 2, 0], [0, -d1 / 2], [-d2 / 2, 0]], fill=fill, edgecolor=color)
    side=0.5 * np.sqrt(d1**2 + d2**2)
    ax.add_artist(rhombus)
    ax.set_xlim(-d2 / 2 - 1, d2 / 2 + 1)
    ax.set_ylim(-d1 / 2 - 1, d1 / 2 + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Rhombus with Side: {side}, Diagonal1: {d1}, and Diagonal2: {d2}")
    return fig

def plot_rhombus_with_area(diagonal1, diagonal2, fill=False, color='blue'):
    fig, ax = plt.subplots()
    rhombus = plt.Polygon([[0, diagonal1 / 2], [diagonal2 / 2, 0], [0, -diagonal1 / 2], [-diagonal2 / 2, 0]], fill=fill, edgecolor=color)
    ax.add_artist(rhombus)
    area = 0.5 * diagonal1 * diagonal2
    ax.text(0, 0, f'Area: {area:.2f}', ha='center', va='center')
    ax.set_xlim(-diagonal2 / 2 - 1, diagonal2 / 2 + 1)
    ax.set_ylim(-diagonal1 / 2 - 1, diagonal1 / 2 + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title("Rhombus with Area")
    return fig

def plot_rhombus_with_perimeter_or_circumfernce(diagonal1, diagonal2, fill=False, color='blue'):
    fig, ax = plt.subplots()
    rhombus = plt.Polygon([[0, diagonal1 / 2], [diagonal2 / 2, 0], [0, -diagonal1 / 2], [-diagonal2 / 2, 0]], fill=fill, edgecolor=color)
    ax.add_artist(rhombus)
    perimeter=2*(diagonal1+diagonal2)
    ax.text(0, 0, f'Perimeter: {perimeter:.2f}', ha='center', va='center')
    ax.set_xlim(-diagonal2 / 2 - 1, diagonal2 / 2 + 1)
    ax.set_ylim(-diagonal1 / 2 - 1, diagonal1 / 2 + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title("Rhombus with Perimeter")
    return fig

def plot_rhombus_with_angles(diagonal1, diagonal2, angle, fill=False, color='blue'):
    fig, ax = plt.subplots()
    rhombus = plt.Polygon([[0, diagonal1 / 2], [diagonal2 / 2, 0], [0, -diagonal1 / 2], [-diagonal2 / 2, 0]], fill=fill, edgecolor=color)
    ax.add_artist(rhombus)
    ax.text(0, diagonal1 / 4, f'Angle: {angle}°', ha='center', va='center')
    ax.set_xlim(-diagonal2 / 2 - 1, diagonal2 / 2 + 1)
    ax.set_ylim(-diagonal1 / 2 - 1, diagonal1 / 2 + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title("Rhombus with Angles")
    return fig
