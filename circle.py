import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

def plot_circle(radius, fill, color='blue'):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius, fill=fill, edgecolor=color)
    ax.add_artist(circle)
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Circle with Radius: {radius}")
    return fig

def plot_circle_with_radius_and_diameter(radius, fill, color='blue'):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius, fill=fill, edgecolor=color)
    diameter=2*radius
    ax.add_artist(circle)
    ax.plot([0, radius], [0, 0], color='red', label=f'Radius: {radius}')
    ax.plot([0, -radius], [0, 0], color='green', label=f'Diameter: {2*radius}')
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.set_title(f"Circle with Radius{radius} and Diameter{diameter}")
    return fig

def plot_circle_with_area(radius, fill, color='blue'):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius, fill=fill, edgecolor=color)
    ax.add_artist(circle)
    area = np.pi * radius**2
    #circumference = 2 * np.pi * radius
    ax.text(0, 0, f'Area: {area:.2f}\n', ha='center', va='center')
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title("Circle with Area")
    return fig

def plot_circle_with_perimeter_or_circumference(radius,todo, fill, color='blue'):
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius, fill=fill, edgecolor=color)
    ax.add_artist(circle)
    perimeter = 2 * np.pi * radius
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Circle with Circumference{perimeter}")
    return fig


def plot_sector(radius, angle, fill, color='blue'):
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    theta = np.linspace(0, np.radians(angle), 100)
    r = np.ones_like(theta) * radius
    ax.fill_between(theta, 0, r, color=color, alpha=0.5)
    ax.set_ylim(0, radius)
    ax.set_title(f"Sector of Circle with Radius: {radius} and Angle: {angle} degrees")
    return fig

def plot_inscribed_or_circumscribed_circle( shape,radius, dimensions,props,fill=True, color='blue'):
    print(dimensions)
    fig, ax = plt.subplots()
    # Default dimensions for each shape
    default_dimensions = {
        'square': {'side': 10},
        'rectangle': {'width': 12, 'height': 6},
        'triangle': {'base': 10, 'height': 8.66},
        'parallelogram': {'base': 12, 'height': 6, 'offset': 4},
        'pentagon': {'side_length': 10},
        'hexagon': {'side_length': 10},
        'heptagon': {'side_length': 10},
        'octagon': {'side_length': 10},
        'nonagon': {'side_length': 10},
        'decagon': {'side_length': 10},
        'trapezium': {'base1': 12, 'base2': 6, 'height': 6},
        'rhombus': {'diagonal1': 10, 'diagonal2': 6}
    }

    # Set dimensions to default if not provided
    if dimensions==False:
        dimensions = default_dimensions.get(shape, {})

    # Calculate the radius of the inscribed circle
    if shape == 'square':
        side=dimensions['square_side']
        inscribed_dimensions = {'square_side': side}
        if 'inscribed' in props:
          radiuss = side / 2
        if 'circumscribed' in props:
          radiuss = max(side, side) / 2
        center = (side / 2, side / 2)
        square = patches.Rectangle((0, 0), side, side, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(square)
    elif shape == 'rectangle':
        length = dimensions['rectangle_length']
        breadth = dimensions['rectangle_breadth']
        inscribed_dimensions = {'rectangle_length':length, 'rectangle_breadth':breadth}
        print(length,breadth)
        if 'inscribed' in props:
          radiuss = min(length, breadth) / 2
        if 'circumscribed' in props:
          radiuss = max(length, breadth) / 2
        center = (length / 2, breadth/ 2)
        rectangle = patches.Rectangle((0, 0), length, breadth, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rectangle)
    
    elif shape == 'triangle':
        sides = dimensions['triangle_sides']
        inscribed_dimensions = {'triangle_sides':sides}
        # Calculate vertices based on given sides
        vertices = [(0, 0), (sides[0], 0),(sides[2] * np.cos(np.arccos((sides[1]**2 + sides[2]**2 - sides[0]**2) / (2 * sides[1] * sides[2]))), 
                    sides[2] * np.sin(np.arccos((sides[1]**2 + sides[2]**2 - sides[0]**2) / (2 * sides[1] * sides[2]))))]

        triangle = Polygon(vertices, closed=True, color=color, fill=fill)
        ax.add_patch(triangle)

        # Extract side lengths for readability
        a, b, c = sides[0], sides[1], sides[2]
        # Calculate the incenter
        Px = (a * vertices[2][0] + b * vertices[1][0] + c * vertices[0][0]) / (a + b + c)
        Py = (a * vertices[2][1] + b * vertices[1][1] + c * vertices[0][1]) / (a + b + c)

        # Calculate the inradius
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        radiuss = area / s

        # Calculate the center
        center = (Px, Py)

        # Plot the incenter
        ax.plot(Px, Py, 'ro')  # Plot the incenter


    elif shape == 'parallelogram':
        base = dimensions['parallelogram_base']
        height = dimensions['parallelogram_height']
        inscribed_dimensions = {'parallelogram_base':base, 'parallelogram_height':height}
        if 'inscribed' in props:
          radiuss = min(base, height) / 2
        if 'circumscribed' in props:
          radius = max(base, height) / 2
        center = (base / 2, height / 2)
        parallelogram = patches.Polygon([(0, 0), (base, 0), (base + offset, height), (offset, height)], edgecolor='black', facecolor='none')
        ax.add_patch(parallelogram)
    elif shape in ['pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon']:
        sides = {
            'pentagon': 5,
            'hexagon': 6,
            'heptagon': 7,
            'octagon': 8,
            'nonagon': 9,
            'decagon': 10
        }
        side_length = dimensions[f'{shape}_side']
        inscribed_dimensions = {f'{shape}_side':side_length}
        if 'inscribed' in props:
          radiuss = side_length / (sides[shape]* np.sin(np.pi / sides[shape]))
        if 'circumscribed' in props:
          radiuss = side_length / (sides[shape]* np.sin(np.pi / sides[shape]))  # Adjusted to make circle smaller
        #radiuss = (side_length * np.sqrt(3)) / 2
        center = (radius, radius)
        polygon = patches.RegularPolygon(center, numVertices=sides[shape], radius=side_length / 2, edgecolor='black', facecolor='none')
        ax.add_patch(polygon)
    elif shape == 'trapezium':
        base1 = dimensions['trapezium_base1']
        base2 = dimensions['trapezium_base2']
        height = dimensions['trapezium_height']
        inscribed_dimensions = {'trapezium_base1':base1, 'trapezium_base2':base2, 'trapezium_height':height}
        if 'inscribed' in props:
          radiuss = min(base1, base2, height) / 2
        if 'circumscribed' in props:
          radiuss = max(base1, base2, height) / 2
        center = ((base1 + base2) / 4, height / 2)
        trapezium = patches.Polygon([(0, 0), (base1, 0), (base1 - (base1 - base2) / 2, height), ((base1 - base2) / 2, height)], edgecolor='black', facecolor='none')
        ax.add_patch(trapezium)
    elif shape == 'rhombus':
        diagonal1 = dimensions['radius_diagonal1']
        diagonal2 = dimensions['radius_diagonal2']
        inscribed_dimensions = {'diagonal1':diagonal1, 'diagonal2':diagonal2}
        if 'inscribed' in props:
          radiuss= min(diagonal1, diagonal2) / 2
        if 'circumscribed' in props:
          radiuss = max(diagonal1, diagonal2) / 2
        center = (diagonal1 / 2, diagonal2 / 2)
        rhombus = patches.Polygon([(0, diagonal2 / 2), (diagonal1 / 2, 0), (diagonal1, diagonal2 / 2), (diagonal1 / 2, diagonal2)], edgecolor='black', facecolor='none')
        ax.add_patch(rhombus)
    else:
        raise ValueError(f"Unsupported shape: {shape}")
  

    # Draw the inscribed circle
    circle = patches.Circle(center, radiuss, edgecolor='black', facecolor=color if fill else 'none')
    ax.add_patch(circle)

    # Set the aspect ratio of the plot to be equal
    ax.set_aspect('equal')

    print('inscribed_dimensions',inscribed_dimensions)
    # Set the limits of the plot to fit the shape
    if 'triangle_sides' in inscribed_dimensions:
      limit = max(inscribed_dimensions['triangle_sides']) + radius +1  
    
    elif inscribed_dimensions:
      print('checking dimensions',inscribed_dimensions)
      limit = max(inscribed_dimensions.values()) + radius +1  
    else:
      limit = 2 * radius + 1

    plt.xlim(-1, limit)
    plt.ylim(-1, limit)

    # Add labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{props} Circle in a {shape.capitalize()}')

    return fig
