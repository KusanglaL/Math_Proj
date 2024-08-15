import matplotlib.pyplot as plt
import numpy as np

def plot_regular_polygon(shape,side, fill, radius=1, color='blue'):
    if shape=='pentagon':
      num_sides = 5
    elif shape=='hexagon':
      num_sides = 6
    elif shape=='heptagon':
      num_sides = 8
    elif shape=='octagon':
      num_sides = 8
    elif shape=='nonagon':
      num_sides = 10
    elif shape=='decagon':
      num_sides = 10

     #calculate the radius
    radius = side / (2 * np.sin(np.pi / num_sides))

    # Calculate the vertices of the polygon
    angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    vertices = np.array([(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles])

    # Close the polygon by adding the first vertex at the end
    vertices = np.vstack([vertices, vertices[0]])

    fig, ax = plt.subplots()

    # Create the polygon
    polygon = plt.Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(polygon)

    # Set plot limits and aspect ratio
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')

    # Set title and grid
    ax.set_title(f'{shape} of side {side}')
    plt.grid(True)

    return fig

def plot_regular_polygon_with_area(shape,side, fill, radius=1, color='blue'):
    if shape=='pentagon':
      num_sides = 5
    elif shape=='hexagon':
      num_sides = 6
    elif shape=='heptagon':
      num_sides = 8
    elif shape=='octagon':
      num_sides = 8
    elif shape=='nonagon':
      num_sides = 10
    elif shape=='decagon':
      num_sides = 10

    #calculate the radius
    radius = side / (2 * np.sin(np.pi / num_sides))
    # Calculate the vertices of the polygon
    angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    vertices = np.array([(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles])

    # Close the polygon by adding the first vertex at the end
    vertices = np.vstack([vertices, vertices[0]])

    # Calculate the area of the polygon
    area = 0.5 * num_sides * radius**2 * np.sin(2 * np.pi / num_sides)

    fig, ax = plt.subplots()

    # Create the polygon
    polygon = plt.Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(polygon)

    # Annotate the area in the center of the polygon
    centroid = np.mean(vertices[:-1], axis=0)  # Calculate centroid of the polygon
    ax.text(centroid[0], centroid[1], f'Area: {area:.2f}', ha='center', va='center', fontsize=12, color='black')

    # Set plot limits and aspect ratio
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')

    # Set title and grid
    ax.set_title(f'{shape} with Area {area}')
    plt.grid(True)

    return fig

def plot_regular_polygon_with_perimeter_or_circumference(shape,side, fill,  radius=1,color='blue'):
    if shape=='pentagon':
      num_sides = 5
    elif shape=='hexagon':
      num_sides = 6
    elif shape=='heptagon':
      num_sides = 8
    elif shape=='octagon':
      num_sides = 8
    elif shape=='nonagon':
      num_sides = 10
    elif shape=='decagon':
      num_sides = 10

     #calculate the radius
    radius = side / (2 * np.sin(np.pi / num_sides))

    # Calculate the vertices of the polygon
    angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
    vertices = np.array([(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles])

    # Close the polygon by adding the first vertex at the end
    vertices = np.vstack([vertices, vertices[0]])

    # Calculate the perimeter of the polygon
    perimeter = 2 * num_sides * radius * np.sin(np.pi / num_sides)

    fig, ax = plt.subplots()

    # Create the polygon
    polygon = plt.Polygon(vertices, closed=True, color=color, fill=fill)
    ax.add_patch(polygon)

    # Annotate the perimeter in the center of the polygon
    centroid = np.mean(vertices[:-1], axis=0)  # Calculate centroid of the polygon
    ax.text(centroid[0], centroid[1], f'Perimeter: {perimeter:.2f}', ha='center', va='center', fontsize=12, color='black')

    # Set plot limits and aspect ratio
    ax.set_xlim(-radius - 1, radius + 1)
    ax.set_ylim(-radius - 1, radius + 1)
    ax.set_aspect('equal', 'box')

    # Set title and grid
    ax.set_title(f'{shape} with Perimeter')
    plt.grid(True)

    return fig

def plot_regular_polygon_with_angles(shape,side, fill, radius=1, color='blue'):
  if shape=='pentagon':
      num_sides = 5
  elif shape=='hexagon':
    num_sides = 6
  elif shape=='heptagon':
    num_sides = 8
  elif shape=='octagon':
    num_sides = 8
  elif shape=='nonagon':
    num_sides = 10
  elif shape=='decagon':
    num_sides = 10

  #calculate the radius
  radius = side / (2 * np.sin(np.pi / num_sides))

  # Calculate the vertices of the polygon
  angles = np.linspace(0, 2 * np.pi, num_sides, endpoint=False)
  vertices = np.array([(radius * np.cos(angle), radius * np.sin(angle)) for angle in angles])

  # Close the polygon by adding the first vertex at the end
  vertices = np.vstack([vertices, vertices[0]])

  fig, ax = plt.subplots()

  # Create the polygon
  polygon = plt.Polygon(vertices, closed=True, color=color, fill=fill)
  ax.add_patch(polygon)

  # Set plot limits and aspect ratio
  ax.set_xlim(-radius - 1, radius + 1)
  ax.set_ylim(-radius - 1, radius + 1)
  ax.set_aspect('equal', 'box')

  # Set title and grid
  ax.set_title(f'{shape} of side {side}')
  plt.grid(True)
  
  # Calculate internal angle of the polygon
  internal_angle = (num_sides - 2) * 180 / num_sides

  # Annotate the vertices with labels and internal angles
  for i, (x, y) in enumerate(vertices[:-1]):
      label = f'{i+1}\n{internal_angle:.1f}°'
      ax.annotate(label, (x, y), fontsize=12, ha='center', va='center', color='red')
  return fig

