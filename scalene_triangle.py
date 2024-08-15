import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt

def plot_scalene_triangle(a, b, c, fill=True, color='blue'):
    # Calculate the angles using the law of cosines
    def law_of_cosines(a, b, c):
        return np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
    
    # Calculate angles in radians
    A = law_of_cosines(b, c, a)
    B = law_of_cosines(a, c, b)
    C = np.pi - A - B
    
    # Coordinates of the vertices
    x0, y0 = 0, 0
    x1, y1 = c * np.cos(C), c * np.sin(C)
    x2, y2 = a, 0
    
    # Create the figure and axis
    fig, ax = plt.subplots()
    triangle = plt.Polygon([[x0, y0], [x1, y1], [x2, y2]], fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)
    
    # Calculate plot limits with padding
    padding = 2  # Amount of padding to add around the triangle
    x_coords = [x0, x1, x2]
    y_coords = [y0, y1, y2]
    ax.set_xlim(min(x_coords) - padding, max(x_coords) + padding)
    ax.set_ylim(min(y_coords) - padding, max(y_coords) + padding)
    
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Scalene Triangle with sides {a},{b} and {c}")

    return fig

def plot_scalene_triangle_with_area(a, b, c, fill, color='blue'):
    # Calculate the angles using the law of cosines
    def law_of_cosines(a, b, c):
        return np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
    
    # Calculate angles in radians
    A = law_of_cosines(b, c, a)
    B = law_of_cosines(a, c, b)
    C = np.pi - A - B
    
    # Coordinates of the vertices
    x0, y0 = 0, 0
    x1, y1 = c * np.cos(C), c * np.sin(C)
    x2, y2 = a, 0
    
    # Calculate the area using Heron's formula
    def herons_formula(a, b, c):
        s = (a + b + c) / 2
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    area = herons_formula(a, b, c)
    
    # Create the figure and axis
    fig, ax = plt.subplots()
    triangle = plt.Polygon([[x0, y0], [x1, y1], [x2, y2]], fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)
    
    # Add text annotation for the area
    centroid_x = (x0 + x1 + x2) / 3
    centroid_y = (y0 + y1 + y2) / 3
    ax.text(centroid_x, centroid_y, f'Area: {area:.2f} cm²', fontsize=12, ha='center', va='center', color='black')
    
    # Set plot limits and aspect ratio
    padding = 2  # Amount of padding to add around the triangle
    x_coords = [x0, x1, x2]
    y_coords = [y0, y1, y2]
    ax.set_xlim(min(x_coords) - padding, max(x_coords) + padding)
    ax.set_ylim(min(y_coords) - padding, max(y_coords) + padding)
    
    # Title for the plot
    ax.set_title(f"Scalene Triangle with area {area}")
    
    return fig


def plot_scalene_triangle_with_perimeter_or_circumference(a, b, c, fill, color='blue'):
    # Calculate the angles using the law of cosines
    def law_of_cosines(a, b, c):
        return np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
    
    # Calculate angles in radians
    A = law_of_cosines(b, c, a)
    B = law_of_cosines(a, c, b)
    C = np.pi - A - B
    
    # Coordinates of the vertices
    x0, y0 = 0, 0
    x1, y1 = c * np.cos(C), c * np.sin(C)
    x2, y2 = a, 0
    
    # Calculate the perimeter
    perimeter = a + b + c
    
    # Create the figure and axis
    fig, ax = plt.subplots()
    triangle = plt.Polygon([[x0, y0], [x1, y1], [x2, y2]], fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)
    
    # Add text annotation for the perimeter
    centroid_x = (x0 + x1 + x2) / 3
    centroid_y = (y0 + y1 + y2) / 3
    ax.text(centroid_x, centroid_y, f'Perimeter: {perimeter:.2f} cm', fontsize=12, ha='center', va='center', color='black')
    
    # Set plot limits and aspect ratio
    padding=4
    ax.set_xlim(min(x0, x1, x2) - padding, max(x0, x1, x2) + padding)
    ax.set_ylim(min(y0, y1, y2) - padding, max(y0, y1, y2) + padding)
    ax.set_aspect('equal', 'box')
    
    # Title for the plot
    ax.set_title(f"Scalene Triangle with perimeter {perimeter}")
    
    return fig





