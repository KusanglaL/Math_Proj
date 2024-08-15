import matplotlib.pyplot as plt

def plot_isosceles_triangle(base, height, fill, color='blue'):
    # Calculate the coordinates of the vertices
    x_coords = [-base / 2, base / 2, 0]
    y_coords = [0, 0, height]

    # Plot the triangle
    fig, ax = plt.subplots()
    triangle = plt.Polygon(list(zip(x_coords, y_coords)), fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)

    # Set plot limits and aspect ratio
    ax.set_xlim(-base / 2 - 1, base / 2 + 1)
    ax.set_ylim(-1, height + 1)  # Adjusted ylim to show entire triangle
    ax.set_aspect('equal', 'box')

    # Set title
    ax.set_title(f"Isosceles Triangle with Base: {base} and Height: {height}")

    return fig

def plot_isosceles_triangle_with_area(base, height, fill, color='blue'):
    # Calculate the coordinates of the vertices
    x_coords = [-base / 2, base / 2, 0]
    y_coords = [0, 0, height]

    # Plot the triangle
    fig, ax = plt.subplots()
    triangle = plt.Polygon(list(zip(x_coords, y_coords)), fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)

    area=0.5*base*height
    ax.text(0, 0, f'Area: {area:.2f}', ha='center', va='center')
    # Set plot limits and aspect ratio
    ax.set_xlim(-base / 2 - 1, base / 2 + 1)
    ax.set_ylim(-1, height + 1)  # Adjusted ylim to show entire triangle
    ax.set_aspect('equal', 'box')

    # Set title
    ax.set_title(f"Isosceles Triangle with Area: {area}")

    return fig

def plot_isosceles_triangle_with_perimeter_or_circumference(base, height, fill, color='blue'):
    # Calculate the coordinates of the vertices
    x_coords = [-base / 2, base / 2, 0]
    y_coords = [0, 0, height]

    # Plot the triangle
    fig, ax = plt.subplots()
    triangle = plt.Polygon(list(zip(x_coords, y_coords)), fill=fill, edgecolor=color, facecolor=color if fill else 'none')
    ax.add_artist(triangle)

    perimeter=base+height+height
    ax.text(0, 0, f'Perimeter: {perimeter:.2f}', ha='center', va='center')
    # Set plot limits and aspect ratio
    ax.set_xlim(-base / 2 - 1, base / 2 + 1)
    ax.set_ylim(-1, height + 1)  # Adjusted ylim to show entire triangle
    ax.set_aspect('equal', 'box')

    # Set title
    ax.set_title(f"Isosceles Triangle with Perimeter: {perimeter}")

    return fig


