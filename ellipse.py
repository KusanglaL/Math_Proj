import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np

def plot_ellipse(major_axis, minor_axis, fill=False, color='blue'):
    fig, ax = plt.subplots()
    ellipse = Ellipse((0, 0), major_axis, minor_axis, fill=fill, color=color)
    ax.add_patch(ellipse)
    ax.set_xlim(-major_axis/2, major_axis/2)
    ax.set_ylim(-major_axis/2, major_axis/2)
    ax.set_aspect('equal')
    ax.set_title(f'Ellipse with major axis {major_axis} and minor axis {minor_axis}')
    return fig

def plot_ellipse_with_area(major_axis, minor_axis, fill=False, color='blue'):
    fig, ax = plt.subplots()
    ellipse = Ellipse((0, 0), major_axis, minor_axis, fill=fill, color=color)
    ax.add_patch(ellipse)
    ax.set_xlim(-major_axis/2, major_axis/2)
    ax.set_ylim(-major_axis/2, major_axis/2)
    ax.set_aspect('equal')
    area = np.pi * (major_axis/2) * (minor_axis/2)
    ax.set_title(f'Ellipse with major axis {major_axis}, minor axis {minor_axis}\nArea: {area:.2f}')
    return fig

def plot_ellipse_with_foci(major_axis, minor_axis, fill=False, color='blue'):
    fig, ax = plt.subplots()
    ellipse = Ellipse((0, 0), major_axis, minor_axis, fill=fill, color=color)
    ax.add_patch(ellipse)
    c = np.sqrt((major_axis/2)**2 - (minor_axis/2)**2)
    ax.plot([-c, c], [0, 0], 'ro', markersize=5)
    ax.set_xlim(-major_axis/2, major_axis/2)
    ax.set_ylim(-major_axis/2, major_axis/2)
    ax.set_aspect('equal')
    ax.set_title(f'Ellipse with major axis {major_axis}, minor axis {minor_axis}, and foci')
    return fig

def plot_ellipse_within_rectangle(rect_length, rect_width, fill=False, color='blue'):
    fig, ax = plt.subplots()
    
    # Create the rectangle
    rectangle = Rectangle((-rect_length/2, -rect_width/2), rect_length, rect_width, fill=False, edgecolor='red')
    ax.add_patch(rectangle)
    
    # Create the inscribed ellipse
    ellipse = Ellipse((0, 0), rect_length, rect_width, fill=fill, edgecolor=color, facecolor='none')
    ax.add_patch(ellipse)
    
    ax.set_xlim(-rect_length/2 - 1, rect_length/2 + 1)
    ax.set_ylim(-rect_width/2 - 1, rect_width/2 + 1)
    ax.set_aspect('equal')
    ax.set_title(f'Ellipse inscribed in a rectangle\nRectangle: {rect_length}x{rect_width}')
    return fig

def plot_ellipse_with_properties(major_axis, minor_axis, properties, dimensions, fill=False, color='blue'):
    if 'inscribed' in properties:
        rect_length = dimensions.get('rectangle_length', major_axis)
        rect_width = dimensions.get('rectangle_width', minor_axis)
        return plot_ellipse_within_rectangle(major_axis, minor_axis, rect_length, rect_width, fill, color)
    elif 'area' in properties:
        return plot_ellipse_with_area(major_axis, minor_axis, fill, color)
    elif 'foci' in properties:
        return plot_ellipse_with_foci(major_axis, minor_axis, fill, color)
    else:
        return plot_ellipse(major_axis, minor_axis, fill, color)
