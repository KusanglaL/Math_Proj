import matplotlib.pyplot as plt
import numpy as np

def plot_square(side, fill=False, color='blue'):
    fig, ax = plt.subplots()
    square = plt.Rectangle((1,1), side, side, fill=fill, edgecolor=color)
    ax.add_artist(square)
    ax.set_xlim(0,side+5)
    ax.set_ylim(0,side+5)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Square with Side: {side}")
    return fig

def plot_square_with_area(side, fill, color='blue'):
    fig, ax = plt.subplots()
    square = plt.Rectangle((1,1), side, side, fill=fill, edgecolor=color)
    ax.add_artist(square)
    area = side**2
    ax.text(0, 0, f'Area: {area:.2f}', ha='center', va='center')
    ax.set_xlim(0,side+5)
    ax.set_ylim(0,side+5)
    ax.set_aspect('equal', 'box')
    ax.set_title("Square with Area")
    return fig

def plot_square_with_perimeter_or_circumference(side, fill, color='blue'):
    fig, ax = plt.subplots()
    square = plt.Rectangle((1,1), side, side, fill=fill, edgecolor=color)
    ax.add_artist(square)
    perimeter = 4 * side
    ax.text(0, 0, f'Perimeter: {perimeter:.2f}', ha='center', va='center')
    ax.set_xlim(0,side+5)
    ax.set_ylim(0,side+5)
    ax.set_aspect('equal', 'box')
    ax.set_title("Square with Perimeter")
    return fig

def plot_square_with_diagonal(side):
    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Define the coordinates of the square
    square_coords = np.array([
        [0, 0], 
        [side, 0], 
        [side, side], 
        [0, side], 
        [0, 0]  # Closing the square
    ])

    # Plot the square
    ax.plot(square_coords[:, 0], square_coords[:, 1], 'b-', label='Square')
    
    # Plot the diagonal
    ax.plot([0, side], [0, side], 'r--', label='Diagonal')
    
    # Set the limits and labels
    ax.set_xlim(-1, side + 1)
    ax.set_ylim(-1, side + 1)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Square with Diagonal')
    ax.set_aspect('equal', adjustable='box')
    ax.legend()
    
    # Return the figure object
    return fig
