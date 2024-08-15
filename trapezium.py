import matplotlib.pyplot as plt
import numpy as np

def plot_trapezium(longer_base, shorter_base, height,fill, color='blue'):
    # Ensure inputs are float
    longer_base = float(longer_base)
    shorter_base = float(shorter_base)
    height = float(height)

    # Calculate the coordinates of the trapezium
    x0, y0 = 0, 0  # Bottom-left of the longer base
    x1, y1 = longer_base, 0  # Bottom-right of the longer base
    x2, y2 = (longer_base - shorter_base) / 2, height  # Top-left of the shorter base
    x3, y3 = (longer_base + shorter_base) / 2, height  # Top-right of the shorter base

    # Vertices in order
    vertices = np.array([(x0, y0), (x1, y1), (x3, y3), (x2, y2), (x0, y0)])

    fig, ax = plt.subplots()
    polygon = plt.Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(polygon)

    # Set plot limits and aspect ratio
    ax.set_xlim(-1, longer_base + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')

    # Set title and grid
    ax.set_title(f'Trapezius with Longer Base {longer_base} and Shorter Base {shorter_base}')
    return fig


def plot_trapezium_with_area(longer_base, shorter_base, height, fill,color='blue'):
    # Ensure inputs are float
    longer_base = float(longer_base)
    shorter_base = float(shorter_base)
    height = float(height)

    # Calculate the area of the trapezium
    area = 0.5 * (longer_base + shorter_base) * height

    # Calculate the coordinates of the trapezium
    x0, y0 = 0, 0  # Bottom-left of the longer base
    x1, y1 = longer_base, 0  # Bottom-right of the longer base
    x2, y2 = (longer_base - shorter_base) / 2, height  # Top-left of the shorter base
    x3, y3 = (longer_base + shorter_base) / 2, height  # Top-right of the shorter base

    # Vertices in order
    vertices = np.array([(x0, y0), (x1, y1), (x3, y3), (x2, y2), (x0, y0)])

    fig, ax = plt.subplots()
    polygon = plt.Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(polygon)

    # Annotate the area
    mid_x = (x0 + x1 + x2 + x3) / 4
    mid_y = (y0 + y1 + y2 + y3) / 4
    ax.text(mid_x, mid_y, f'Area = {area:.2f}', fontsize=12, ha='center', va='center', color='black')

    # Set plot limits and aspect ratio
    ax.set_xlim(-1, longer_base + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')

    # Set title and grid
    ax.set_title(f'Right Trapezium with Longer Base {longer_base}, Shorter Base {shorter_base}, and Height {height}')
    return fig

def plot_right_trapezium(longer_base, shorter_base, height, fill, color='blue'):
    # Ensure inputs are float
    longer_base = float(longer_base)
    shorter_base = float(shorter_base)
    height = float(height)
    
    # Calculate the length of the legs
    leg = np.sqrt(((longer_base - shorter_base) / 2)**2 + height**2)
    
    # Coordinates of the trapezium vertices
    top_base_x = (longer_base - shorter_base) / 2
    vertices = np.array([
        [-longer_base / 2, 0],                # Bottom-left
        [longer_base / 2, 0],                 # Bottom-right
        [shorter_base / 2 + top_base_x, height],  # Top-right
        [-shorter_base / 2 + top_base_x, height],  # Top-left
        [-longer_base / 2, 0]                 # Closing the loop
    ])
    
    fig, ax = plt.subplots()
    trapezium = plt.Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(trapezium)
    
    # Annotate the length of the legs
    ax.plot([vertices[2][0], vertices[3][0]], [vertices[2][1], vertices[3][1]], color='red', label=f'Leg: {leg:.2f}')
    
    # Calculate and annotate the area of the trapezium
    area = 0.5 * (longer_base + shorter_base) * height
    mid_x = (vertices[0][0] + vertices[1][0] + vertices[2][0] + vertices[3][0]) / 4
    mid_y = (vertices[0][1] + vertices[1][1] + vertices[2][1] + vertices[3][1]) / 4
    ax.text(mid_x, mid_y, f'Area = {area:.2f}', fontsize=12, ha='center', va='center', color='black')

    # Set plot limits and aspect ratio
    ax.set_xlim(-longer_base / 2 - 1, longer_base / 2 + 1)
    ax.set_ylim(0, height + 1)
    ax.set_aspect('equal', 'box')
    
    # Set title, legend, and grid
    ax.set_title("right Trapezium")
    ax.legend()
    
    
    return fig

def plot_isosceles_trapezium(long_base, short_base, height, fill=False, color='blue'):
    # Ensure inputs are float
    long_base = float(long_base)
    short_base = float(short_base)
    height = float(height)
    
    # Coordinates of the right trapezium vertices
    vertices = np.array([
        [-long_base / 2, 0],               # Bottom-left
        [long_base / 2, 0],                # Bottom-right
        [long_base / 2 - short_base, height],  # Top-right
        [-long_base / 2 + short_base, height],  # Top-left
        [-long_base / 2, 0]                # Closing the loop
    ])
    
    fig, ax = plt.subplots()
    trapezium = plt.Polygon(vertices, closed=True, color=color, fill=fill, edgecolor='black')
    ax.add_patch(trapezium)
    
    # Annotate the height
    ax.plot([vertices[0][0], vertices[3][0]], [vertices[0][1], vertices[3][1]], color='green', linestyle='--', label=f'Height: {height:.2f}')
    
    # Set plot limits and aspect ratio
    ax.set_xlim(-long_base / 2 - 1, long_base / 2 + 1)
    ax.set_ylim(0, height + 1)
    ax.set_aspect('equal', 'box')
    
    # Set title and legend
    ax.set_title("isosceles Trapezium")
    ax.legend()
    plt.grid(True)
    
    return fig