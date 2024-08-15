from circle import plot_circle, plot_circle_with_radius_and_diameter, plot_circle_with_area, plot_circle_with_perimeter_or_circumference,plot_inscribed_or_circumscribed_circle, plot_sector
from rectangle import plot_rectangle, plot_rectangle_with_area,plot_rectangle_with_perimeter_or_circumference,plot_rectangle_with_perimeter_or_circumference, plot_rectangle_with_diagonals
from square import plot_square, plot_square_with_area,plot_square_with_perimeter_or_circumference, plot_square_with_diagonal
from triangle import plot_triangle, plot_triangle_with_area,plot_triangle_with_perimeter_or_circumference
from equilateral_triangle import plot_equilateral_triangle,plot_equilateral_triangle_with_area,plot_equilateral_triangle_with_perimeter_or_circumference
from isosceles_triangle import plot_isosceles_triangle,plot_isosceles_triangle_with_area,plot_isosceles_triangle_with_perimeter_or_circumference
from scalene_triangle import plot_scalene_triangle,plot_scalene_triangle_with_area,plot_scalene_triangle_with_perimeter_or_circumference
from right_triangle import plot_right_triangle_with_area,plot_right_triangle_with_perimeter,plot_right_triangle
#from isosceles_triangle import plot_scalene_triangle,plot_scalene_triangle_with_area,plot_scalene_triangle_with_perimeter_or_circumference
from polygon import plot_regular_polygon,plot_regular_polygon_with_area,plot_regular_polygon_with_perimeter_or_circumference,plot_regular_polygon_with_angles
from parallelogram import plot_parallelogram, plot_parallelogram_with_area,plot_parallelogram_with_perimeter_or_circumference, plot_parallelogram_with_angles, plot_parallelogram_with_diagonals
from rhombus import plot_rhombus, plot_rhombus_with_area,plot_rhombus_with_perimeter_or_circumfernce, plot_rhombus_with_angles
from trapezium import plot_trapezium, plot_trapezium_with_area, plot_isosceles_trapezium, plot_right_trapezium
from ellipse import plot_ellipse, plot_ellipse_with_area, plot_ellipse_with_foci, plot_ellipse_within_rectangle
from equation import plot_equation
from extract_shapes import extract_shapes_and_dimensions
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import regex as re

def plot_shape(question, shape_list, dimensions_list, properties):
    dimensions = {}
    shape_properties = []
    props = []
    for dimension in dimensions_list:
        dimensions.update(dimension)
    print("Dimensions:", dimensions)
    for prop in properties:
        props.append(prop)
    print("Properties:", props)

    fig = None  # Initialize fig to None

    for shape in shape_list:
        print('Processing shape:', shape)
        
        if shape == "ellipse":
            shape_properties = props
            if 'inscribed' in shape_properties or 'circumscribed' in shape_properties:
                rect_length = dimensions.get('rectangle_length')
                rect_width = dimensions.get('rectangle_width')
                if rect_length is not None and rect_width is not None:
                    print(f"Plotting inscribed ellipse: length={rect_length}, width={rect_width}")
                    fig = plot_ellipse_within_rectangle(rect_length, rect_width, fill=False, color='blue')
                else:
                    print("Error: Rectangle dimensions not provided for inscribed ellipse")
            else:
                major_axis = dimensions.get('ellipse_major_axis')
                minor_axis = dimensions.get('ellipse_minor_axis')
                if major_axis is not None and minor_axis is not None:
                    print(f"Plotting regular ellipse: major axis={major_axis}, minor axis={minor_axis}")
                    if 'area' in shape_properties:
                        fig = plot_ellipse_with_area(major_axis, minor_axis, fill=True, color='blue')
                    elif 'foci' in shape_properties:
                        fig = plot_ellipse_with_foci(major_axis, minor_axis, fill=False, color='blue')
                    else:
                        fig = plot_ellipse(major_axis, minor_axis, fill=False, color='blue')
                
        elif shape== "circle":
          radius = dimensions['circle_radius']
          shape_properties=props
          if 'diameter' in shape_properties:
            filll=False
            fig=plot_circle_with_radius_and_diameter(radius,filll,color='blue')
          elif 'area' in shape_properties :
            area=np.pi*radius*radius
            filll=True
            fig=plot_circle_with_area(radius,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            perimeter=2*np.pi*radius
            filll=False
            fig=plot_circle_with_perimeter_or_circumference(radius,perimeter,filll,color='blue')
          elif 'sector' in shape_properties:
            filll=False
            angle_pattern = re.search(r'angle (\d+\.?\d*)\s*degrees',question)
            if angle_pattern:
              angle = float(angle_pattern.group(1))
            else:
              angle=45 #default angle
            fig=plot_sector(radius,angle,filll,color='blue')
          elif 'inscribed' in shape_properties or 'circumscribed' in shape_properties:
            filll = False
            #  shape1_dimension=[]
            if 'square' in shape_list:
                shape1 = 'square'
                #  shape1_dimension = dimensions.get('square_side', None)
            elif 'rectangle' in shape_list:
                shape1 = 'rectangle'
                #  shape1_dimension = [dimensions.get('rectangle_length',0), dimensions.get('rectangle_breadth',0)]
                #  print(shape1_dimension)
            elif 'triangle' in shape_list:
                shape1 = 'triangle'
                #  shape1_dimension = [dimensions.get('triangle_sides', [0, 0, 0])]
            elif 'parallelogram' in shape_list:
                shape1 = 'parallelogram'
                #  shape1_dimension = [dimensions.get('parallelogram_base', 0), dimensions.get('parallelogram_height', 0)]
            elif 'pentagon' in shape_list:
                shape1 = 'pentagon'
                #  shape1_dimension = dimensions.get('pentagon_side', 0)
            elif 'hexagon' in shape_list:
                shape1 = 'hexagon'
                #  shape1_dimension = dimensions.get('hexagon_side', 0)
            elif 'heptagon' in shape_list:
                shape1 = 'heptagon'
                #  shape1_dimension = dimensions.get('heptagon_side', 0)
            elif 'octagon' in shape_list:
                shape1 = 'octagon'
                #  shape1_dimension = dimensions.get('octagon_side', 0)
            elif 'nonagon' in shape_list:
                shape1 = 'nonagon'
                #  shape1_dimension = dimensions.get('nonagon_side', 0)
            elif 'decagon' in shape_list:
                shape1 = 'decagon'
                #  shape1_dimension = dimensions.get('decagon_side', 0)
            else:
              shape1 = 'square'  # Default to square if no other shape matches
              d={'square_side':2}
              fig = plot_inscribed_or_circumscribed_circle(shape1, radius, d,shape_properties,filll, color='blue')
              break
            fig = plot_inscribed_or_circumscribed_circle(shape1, radius, dimensions,shape_properties,filll, color='blue')
          else:
            filll=False
            fig=plot_circle(radius,filll,color='blue')

        elif shape == "rectangle":
          length = dimensions['rectangle_length']
          breadth = dimensions['rectangle_breadth']
          shape_properties=props
          if 'area' in shape_properties:
            area=length*breadth
            filll=True
            print("plotting right angled triangle with area")
            fig=plot_rectangle_with_area(length,breadth,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            perimeter=2*(length+breadth)
            filll=False
            fig=plot_rectangle_with_perimeter_or_circumference(length,breadth,filll,color='blue')
          elif 'diagonal' in shape_properties or 'diagonals' in shape_properties:
            diagonal=np.sqrt(length**2+breadth**2)
            filll=False
            fig=plot_rectangle_with_diagonals(length,breadth,filll,color='blue')
          else:
            filll=False
            fig=plot_rectangle(length,breadth,filll,color='blue')
        
        elif shape == "square":
          side = dimensions['square_side']
          shape_properties=props
          if 'area' in shape_properties:
            area=side**2
            filll=True
            fig=plot_square_with_area(side,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            perimeter=4*side
            filll=False
            fig=plot_square_with_perimeter_or_circumference(side,filll,color='blue')
          elif 'diagonal' in shape_properties or 'diagonals' in shape_properties:
            filll=False
            fig=plot_square_with_diagonal(side,filll,color='blue')
          else:
            filll=False
            fig=plot_square(side,filll,color='blue')

        elif shape == "triangle":
          shape_properties=props
          if 'triangle_sides' in dimensions:
            sides = dimensions['triangle_sides']
            print("printing sides",sides)
            if 'area' in shape_properties:
              s=(sides[0]+sides[1]+sides[2])/2
              area=(s*(s-sides[0])*(s-sides[1])*(s-sides[2]))**0.5
              filll=True
              fig=plot_triangle_with_area(sides,area,filll,color='blue')
            elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
              perimeter=sum(sides)
              filll=False
              fig=plot_triangle_with_perimeter_or_circumference(sides,filll,color='blue')
            else:
              filll=False
              fig=plot_triangle(sides,filll,color='blue')
            
          else:
            height=dimensions['triangle_height']
            print("printing height",height)
            base=dimensions['triangle_base']
            print("printing base",base)
            if 'area' in shape_properties:
              filll=True
              print("plotting right angled triangle with area")
              fig=plot_right_triangle_with_area(base,height,filll,color='blue')
            elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
              filll=False
              fig=plot_right_triangle_with_perimeter(base,height,filll,color='blue')
            else:
              filll=False
              fig=plot_right_triangle(base,height,filll,color='blue')
        
        elif shape=='equilateral triangle':
          side = dimensions['equilateral_side']
          shape_properties=props
          if 'area' in shape_properties:
            area=(np.sqrt(3)/4)*side**2
            filll=True
            fig=plot_equilateral_triangle_with_area(side,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            perimeter=3*side
            filll=False
            fig=plot_equilateral_triangle_with_perimeter_or_circumference(side,filll,color='blue')
          else:
            filll=False
            fig=plot_equilateral_triangle(side,filll,color='blue')
        
        elif shape=='isosceles triangle':
          base = dimensions['isosceles_base']
          height = dimensions['isosceles_height']
          shape_properties=props
          if 'area' in shape_properties:
            area=0.5*base*height
            filll=True
            fig=plot_isosceles_triangle_with_area(base,height,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            perimeter=base+height+height
            filll=False
            fig=plot_isosceles_triangle_with_perimeter_or_circumference(base,height,filll,color='blue')
          else:
            filll=False
            fig=plot_isosceles_triangle(base,height,filll,color='blue')
        
        elif shape=='scalene triangle':
          shape_properties=props
          a=dimensions['scalene_sides'][0]
          b=dimensions['scalene_sides'][1]
          c=dimensions['scalene_sides'][2]
          if 'area' in shape_properties:
            filll=True
            fig=plot_scalene_triangle_with_area(a,b,c,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            filll=False
            fig=plot_scalene_triangle_with_perimeter_or_circumference(a,b,c,filll,color='blue')
          else:
            filll=False
            fig=plot_scalene_triangle(a,b,c,filll,color='blue')

        elif shape== "parallelogram":
          base = dimensions['parallelogram_base']
          height = dimensions['parallelogram_height']
          shape_properties=props
          if 'area' in shape_properties:
            area = base * height
            filll=True
            fig=plot_parallelogram_with_area(base,height,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            perimeter = 2 * (base + height)
            filll=False
            fig=plot_parallelogram_with_perimeter_or_circumference(base,height,filll,color='blue')
          elif 'diagonal' in shape_properties or 'diagonals' in shape_properties:
            diagonal = np.sqrt(base**2 + height**2)
            filll=False
            fig=plot_parallelogram_with_diagonals(base,height,filll,color='blue')
          else:
            filll=False
            fig=plot_parallelogram(base,height,filll,color='blue')
          
        elif shape == "pentagon" or shape=='hexagon' or shape=='heptagon' or shape=='octagon' or shape=='nonagon' or shape=='decagon':
          side = dimensions[f'{shape}_side']
          shape_properties=props
          if 'area' in shape_properties:
            filll=True
            fig=plot_regular_polygon_with_area(shape,side,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            filll=False
            fig=plot_regular_polygon_with_perimeter_or_circumference(shape,side,filll,color='blue')
          elif 'angles' in shape_properties or 'angle' in shape_properties:
            filll=False
            fig=plot_regular_polygon_with_angles(shape,side, filll, radius=1, color='blue')
          else:
            filll=False
            fig=plot_regular_polygon(shape,side,filll,color='blue')
        
        elif shape=="trapezium":
          long_base=dimensions['trapezium_longer_base']
          short_base=dimensions['trapezium_shorter_base']
          heightt=dimensions['trapezium_height']
          shape_properties=props
          if 'area' in shape_properties:
            filll=True
            fig=plot_trapezium_with_area(long_base,short_base,heightt,filll,color='blue')
          else:
            filll=False
            fig=plot_trapezium(long_base,short_base,heightt,filll,color='blue')
          
        elif shape=='right trapezium':
          long_base=dimensions['trapezium_longer_base']
          short_base=dimensions['trapezium_shorter_base']
          heightt=dimensions['trapezium_height']
          shape_properties=props
          filll=True
          fig=plot_right_trapezium(long_base,short_base,heightt,filll,color='blue')

        elif shape=='isosceles trapezium':
          long_base=dimensions['trapezium_longer_base']
          short_base=dimensions['trapezium_shorter_base']
          heightt=dimensions['trapezium_height']
          shape_properties=props
          filll=True
          fig=plot_isosceles_trapezium(long_base,short_base,heightt,filll,color='blue')

        elif shape=="rhombus" or shape=="diamond":
          diagonal1=dimensions['rhombus_diagonal1']
          diagonal2=dimensions['rhombus_diagonal2']
          shape_properties=props
          if 'area' in shape_properties:
            area=0.5*diagonal1*diagonal2
            filll=True
            fig=plot_rhombus_with_area(diagonal1,diagonal2,filll,color='blue')
          elif 'perimeter' in shape_properties or 'circumference' in shape_properties:
            perimeter=2*(diagonal1+diagonal2)
            filll=False
            fig=plot_rhombus_with_perimeter_or_circumfernce(diagonal1,diagonal2,filll,color='blue')
          elif 'angles' in shape_properties:
            angle_pattern = re.search(r'angle (\d+\.?\d*)\s*degrees',question)
            if angle_pattern:
              angle = float(angle_pattern.group(1))
            filll=False
            fig=plot_rhombus_with_angles(diagonal1,diagonal2,angle,filll,color='blue')
          else:
            filll=False
            fig=plot_rhombus(diagonal1,diagonal2,filll,color='blue')
        else:
            print("shape not found")
            fig = plt.figure()  # Create an empty figure if shape is not found
            plt.text(0.5, 0.5, f"Shape '{shape}' not found", ha='center', va='center')

    if fig is not None:
      st.pyplot(fig)
    else:
      st.write("No figure was generated.")

