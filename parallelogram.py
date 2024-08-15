import matplotlib.pyplot as plt

def plot_parallelogram(base, height, fill=False, color='blue'):
    fig, ax = plt.subplots()
    parallelogram = plt.Polygon([[0, 0], [base, 0], [base + height, height], [height, height]], fill=fill, edgecolor=color)
    ax.add_artist(parallelogram)
    ax.set_xlim(-1, base + height + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Parallelogram with Base: {base} and Height: {height}")
    return fig

def plot_parallelogram_with_area(base, height, fill=False, color='blue'):
    fig, ax = plt.subplots()
    parallelogram = plt.Polygon([[0, 0], [base, 0], [base + height, height], [height, height]], fill=fill, edgecolor=color)
    ax.add_artist(parallelogram)
    area = base * height
    ax.text(base / 2, height / 2, f'Area: {area:.2f}', ha='center', va='center')
    ax.set_xlim(-1, base + height + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Parallelogram with Area {area}")
    return fig

def plot_parallelogram_with_perimeter_or_circumference(base, height, fill=False, color='blue'):
    fig, ax = plt.subplots()
    parallelogram = plt.Polygon([[0, 0], [base, 0], [base + height, height], [height, height]], fill=fill, edgecolor=color)
    ax.add_artist(parallelogram)
    perimeter = 2 * (base + height)
    ax.text(base / 2, height / 2, f'Perimeter: {perimeter:.2f}', ha='center', va='center')
    ax.set_xlim(-1, base + height + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title("Parallelogram with Perimeter")
    return fig

def plot_parallelogram_with_angles(base, height, angle, fill=False, color='blue'):
    fig, ax = plt.subplots()
    parallelogram = plt.Polygon([[0, 0], [base, 0], [base + height, height], [height, height]], fill=fill, edgecolor=color)
    ax.add_artist(parallelogram)
    ax.text(base / 2, 0, f'Angle: {angle}°', ha='center', va='center')
    ax.set_xlim(-1, base + height + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    ax.set_title("Parallelogram with Angles")
    return fig

def plot_parallelogram_with_diagonals(base, height, fill=False, color='blue'):
    fig, ax = plt.subplots()
    parallelogram = plt.Polygon([[0, 0], [base, 0], [base + height, height], [height, height]], fill=fill, edgecolor=color)
    ax.add_artist(parallelogram)
    ax.plot([0, base + height], [0, height], color='red', label='Diagonal')
    ax.plot([base, height], [0, height], color='red')
    ax.set_xlim(-1, base + height + 1)
    ax.set_ylim(-1, height + 1)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.set_title("Parallelogram with Diagonals")
    return fig
