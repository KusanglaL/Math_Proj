import matplotlib.pyplot as plt

def plot_rectangle(length, width, fill=False, color='blue'):
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((1,1), length, width, fill=fill, edgecolor=color)
    ax.add_artist(rectangle)
    ax.set_xlim(0,length+5)
    ax.set_ylim(0,width+5)
    ax.set_aspect('equal', 'box')
    ax.set_title(f"Rectangle with Length: {length} and Width: {width}")
    return fig

def plot_rectangle_with_area(length, breadth, fill, color='blue'):
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((1,1),length, breadth,fill=fill, edgecolor=color)
    ax.add_artist(rectangle)
    area = length * breadth
    ax.text(length/2, breadth/2, f'Area: {area:.2f}\n', ha='center', va='center')
    ax.set_xlim(0,length+10)
    ax.set_ylim(0,breadth+10)
    ax.set_aspect('equal', 'box')
    ax.set_title("Rectangle with Area")
    return fig

def plot_rectangle_with_perimeter_or_circumference(length, breadth,fill, color='blue'):
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((1,1),length,breadth,fill=fill, edgecolor=color)
    ax.add_artist(rectangle)
    perimeter = 2 * (length + breadth)
    ax.text(0, 0, f'Perimeter: {perimeter:.2f}',ha='center',va='center')
    ax.set_title("Rectangle with Area and Perimeter")
    ax.set_xlim(0,length+5)
    ax.set_ylim(0,breadth+5)
    ax.set_aspect('equal', 'box')
    return fig

def plot_rectangle_with_diagonals(length, width, fill, color='blue'):
    fig, ax = plt.subplots()
    rectangle = plt.Rectangle((1,1),length,width, fill=fill, edgecolor=color)
    ax.add_artist(rectangle)
    ax.plot([1,1+length], [1,1+width], color='red', label='Diagonal 1')
    ax.plot([1,1+length], [1+width,1], color='red',label='Diagonal 2')
    ax.set_xlim(0,length+5)
    ax.set_ylim(0,width+5)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.set_title("Rectangle with Diagonals")
    return fig
