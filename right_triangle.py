import matplotlib.pyplot as plt
import numpy as np

def plot_right_triangle_with_area(leg1, leg2, fill, color='blue'):
    hypotenuse = np.sqrt(leg1**2 + leg2**2)
    area = 0.5 * leg1 * leg2
    fig, ax = plt.subplots()
    triangle = plt.Polygon([[0, 0], [leg1, 0], [0, leg2]], fill=fill, edgecolor=color)
    ax.add_artist(triangle)
    
    ax.text(leg1/2, leg2/2, f'Area: {area:.2f}', fontsize=12, ha='center', va='center', backgroundcolor='white')
    ax.set_xlim(-1, leg1 + 1)
    ax.set_ylim(-1, leg2 + 1)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.set_title(f"Triangle with area: {area}")
    
    return fig


def plot_right_triangle_with_perimeter(leg1, leg2, fill=True, color='blue'):
    hypotenuse = np.sqrt(leg1**2 + leg2**2)
    perimeter = leg1 + leg2 + hypotenuse
    fig, ax = plt.subplots()
    triangle = plt.Polygon([[0, 0], [leg1, 0], [0, leg2]], fill=fill, edgecolor=color)
    ax.add_artist(triangle)
    ax.plot([0, leg1], [0, leg2], color='red', label=f'Hypotenuse: {hypotenuse:.2f}')
    ax.text(leg1/2, leg2/2, f'Perimeter: {perimeter:.2f}', fontsize=12, ha='center', va='center', backgroundcolor='white')
    ax.set_xlim(-1, leg1 + 1)
    ax.set_ylim(-1, leg2 + 1)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.set_title("Right Triangle")
    return fig




def plot_right_triangle(base, height, fill=True, color='blue'):
    hypotenuse = np.sqrt(base**2 + height**2)
    fig, ax = plt.subplots()
    
    # Corrected triangle vertices
    triangle = plt.Polygon([[0, 0], [base, 0], [0, height]], fill=fill, edgecolor=color)
    ax.add_artist(triangle)
    
    # Draw hypotenuse
    ax.plot([0, base], [height, 0], color='red', label=f'Hypotenuse: {hypotenuse:.2f}')
    
    # Annotate base and height
    ax.text(base / 2, -1/2, f'Base: {base}', fontsize=12, ha='center', va='center')
    ax.text(-1/2, height / 2, f'Height: {height}', fontsize=12, ha='center', va='center', rotation=90)
    ax.text(base / 2, height / 2, f'Hypotenuse: {hypotenuse:.2f}', fontsize=12, ha='center', va='center', backgroundcolor='white')
    
    # Set plot limits and aspect ratio
    ax.set_xlim(-1, base + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    
    # Add legend and title
    ax.legend()
    ax.set_title("Right Triangle with Base and Height")
    
    return fig

