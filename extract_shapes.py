import re
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

def shape_operations():
    st.header("Shape Operations")
    st.write("Here you can perform operations related to shapes.")
    # Add your shape-related logic here

    st.write("Shape processing functionality goes here...")


def extract_shapes_and_dimensions(text):
    shapes = {'circle':['diameter','area','perimeter','circumference','sector','inscribed','circumscribed'],
              'rectangle':['area','perimeter','circumference','diagonals'],
              'square':['area','perimeter','circumference','diagonals'],
              'triangle':[['equilateral triangle','isosceles triangle','scalene triangle','right triangle','right-angled triangle','right angled triangle','triangle'],['area','perimeter','circumference']],
              'parallelogram':['area','perimeter','diagonals','circumference'],
              'rhombus':['area','perimeter','circumference'],
              'trapezium':[['isosceles trapezium','right trapezium'],['area','perimeter','circumference']],
              'pentagon':['area','perimeter','circumference','angles','angle'],
              'hexagon':['area','perimeter','circumference','angles','angle'],
              'heptagon':['area','perimeter','circumference','angles','angle'],
              'octagon':['area','perimeter','circumference','angles','angle'],
              'nonagon':['area','perimeter','circumference','angles','angle'],
              'decagon':['area','perimeter','circumference','angles','angle'],
              'ellipse':['area','foci','inscribed']
    }

    plot_shapes=[]
    shape_list = []
    dimensions_list = []
    props=[]
    radius = None
    diameter = None
    length = None
    height = None
    width = None



    for shape in shapes:
        if shape in text:
            dimensions = {}

            if shape == 'circle':
                radius_match = re.search(r'(radius)\s*(of)*\s*(\d+\.?\d*)\s*(cm)*', text)
                diameter_match = re.search(r'(diameter)\s*(of)*\s*(\d+\.?\d*)\s*(cm)*', text)

                if radius_match:
                  dimensions['circle_radius'] = float(radius_match.group(3))
                elif diameter_match:
                  diameter = float(diameter_match.group(3))
                  dimensions['circle_radius'] = diameter / 2  # Calculate radius from diameter
                else:
                  dimensions['circle_radius'] = 2 # default radius

                shape_list.append(shape)

                # for prop in shapes[shape]:
                #   if prop in text:
                #     props.append(prop)

                props = []
                for prop in shapes.get(shape, []):
                  if prop in text:
                    props.append(prop)




            elif shape == 'square':
              shape_list.append(shape)
              match = re.search(r'(\d+\.?\d*)\s*(cm)?\s*side|side\s*\w*\s*(\d+\.?\d*)\s*(cm)?', text)
              if match:
                  dimensions['square_side'] = float(match.group(1) or match.group(3)) 
              else:
                  dimensions['square_side'] = 2 # default side length
              for prop in shapes[shape]:
                  if prop in text:
                    props.append(prop)



            elif 'rectangle' in text:
                shape = 'rectangle'
                shape_list.append(shape)
                dimension=re.search(r'dimensions?\s*(\d+\.?\d*)\s*\w*\s*(\d+\.?\d*)\b',text,re.IGNORECASE)
                if dimension:
                  num1=float(dimension.group(1))
                  num2=float(dimension.group(2))
                  if num1>num2:
                   length_value=num1
                   breadth_value=num2
                  else:
                    length_value=num2
                    breadth_value=num1

                else:
                      
                  match_length = re.search(r'(\d+\.?\d*)\s*(cm)?\s*(length|height)|(length|height)\s*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)
                  match_breadth = re.search(r'(\d+\.?\d*)\s*(cm)?\s*(breadth|width)|(breadth|width)\s*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)
                  if match_length:
                      if match_length.group(1):  # When number is before unit
                        length_value = float(match_length.group(1))
                      elif match_length.group(4):  # When number is after unit
                        length_value = float(match_length.group(5))
                  else:
                    length_value=3

                  # Breadth/Width extraction
                  if match_breadth:
                      if match_breadth.group(1):  # When number is before unit
                        breadth_value = float(match_breadth.group(1))
                      elif match_breadth.group(4):  # When number is after unit
                        breadth_value = float(match_breadth.group(5))

                  else:
                    breadth_value=2
                        
                dimensions['rectangle_length']=length_value
                dimensions['rectangle_breadth']=breadth_value

                for prop in shapes[shape]:
                  if prop in text:
                    props.append(prop)


            elif shape == 'triangle':
              for typee in shapes[shape][0]:
                if typee in text:
                  shape2 = typee
                  break

              if shape2 in ['right triangle', 'right-angled triangle', 'right angled triangle']:
                shape_list.append(shape2)
                legs = re.search(r'(?:legs?\s*)?(\d+\.?\d*)\s*(?:cm)?\s*(?:and\s*)?(\d+\.?\d*)\s*(?:cm)?\s*(?:legs?)?', text, re.IGNORECASE)
                print("legsss",legs.groups())
                if legs:
                  leg1=float(legs.group(1))
                  leg2=float(legs.group(2))
                  dimensions['triangle_height']=float(leg1)
                  dimensions['triangle_base']=float(leg2)
                else:
                  height=re.search(r'(height|length)\s*\w*\s*(\d+\.?\d*)\s*(cm)?|(\d+\.?\d*)\s*(cm)?(height|length)',text)
                  if height:
                    dimensions['triangle_height'] = float(height.group(2) or height.group(4))
                  else:
                     dimensions['triangle_height']=5
                  base=re.search(r'base\s*\w*\s*(\d+\.?\d*)\s*(cm)?|(\d+\.?\d*)\s*(cm)?base',text)
                  if base:
                    dimensions['triangle_base'] = float(base.group(1) or base.group(3))
                  else:
                     dimensions['triangle_base']=3

              if shape2 == 'equilateral triangle':
                shape_list.append(shape2)
                match = re.search(r'(side)*\s*(\d+\.?\d*)\s*(?:cm)?|(\d+\.?\d*)\s*(?:cm)?\s*(side)*', text)
                if match:
                    dimensions['equilateral_side'] = float(match.group(2) or match.group(3))
                else:
                    dimensions['equilateral_side'] = 3 # default side length

              elif shape2=='isosceles triangle':
                shape_list.append(shape2)
                base=re.search(r'((\d+\.?\d*)\s*(?:cm)?\s*base)|(base\s*(\d+\.?\d*)\s*(?:cm)?)',text)
                height=re.search(r'((\d+\.?\d*)\s*(?:cm)?\s*(side|length|height|sides)|(height|length|side|sides)\s*(\d+\.?\d*)\s*(?:cm)?)',text)
                if base:
                  dimensions['isosceles_base']=float(base.group(1) or base.group(4))
                else:
                  dimensions['isosceles_base']=3
                if height:
                  dimensions['isosceles_height']=float(height.group(2) or height.group(5))
                else:
                  dimensions['isosceles_height']=4

              elif shape2=='scalene triangle':
                shape_list.append(shape2)
                matches = re.findall(r'(\d+\.?\d*)\s*(?:cm)?', text)
                if len(matches) >= 3:
                    dimensions['scalene_sides'] = list(map(float, matches[:3]))
                else:
                    dimensions['scalene_sides'] = [3, 4, 5]  # default sides

              else:
                shape_list.append(shape)
                matches = re.findall(r'(\d+\.?\d*)\s*(cm)?', text)
                if len(matches) >= 3:
                  dimensions['triangle_sides'] = list(map(float, matches[:3]))
                else:
                  # dimensions['triangle_sides'] = [3, 4, 5]  # default side
                  height=re.search(r'(height|length)\s*\w*\s*(\d+\.?\d*)\s*(cm)?|(\d+\.?\d*)\s*(cm)?(height|length)',text)
                  if height:
                    dimensions['triangle_height'] = float(height.group(2) or height.group(4))
                  base=re.search(r'(base)\s*(\d+\.?\d*)\s*(cm)?|(\d+\.?\d*)\s*(cm)?\s*(base)',text)
                  if base:
                    print("extracted base= ",base)
                    dimensions['triangle_base'] = float(base.group(2) or base.group(3))
                

              for prop in shapes[shape][1]:
                  if prop in text:
                    props.append(prop)


            elif shape == 'parallelogram':
              shape_list.append(shape)
              height = re.search(r'(\d+\.?\d*)\s*(cm)?\s*(length|height)|(length|height)\s*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)
              if height:
                  dimensions['parallelogram_height'] = float(height.group(1) or height.group(5))
              else:
                  dimensions['parallelogram_height'] = 4  # default height
              base = re.search(r'(\d+\.?\d*)\s*(cm)?\s*(breadth|width|base)|(base|breadth|width)\s*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)
              if base:
                  dimensions['parallelogram_base'] = float(base.group(1) or base.group(5))
              else:
                  dimensions['parallelogram_base'] = 3  # default base
              for prop in shapes[shape]:
                if prop in text:
                  props.append(prop)



            elif shape == 'pentagon' or shape == 'hexagon' or shape == 'heptagon' or shape == 'octagon' or shape=='nonagon' or shape == 'decagon':
              shape_list.append(shape)
              match = re.search(r'(\d+\.?\d*)\s*(?:cm)?', text)
              if match:
                  dimensions[f'{shape}_side'] = float(match.group(1))
              else:
                  dimensions[f'{shape}_side'] = 2  # default side length
              for prop in shapes[shape]:
                if prop in text:
                  props.append(prop)

            elif shape=='trapezium':
              for typee in shapes[shape][0]:
                if typee in text:
                  shape2 = typee
                  break
              if shape2=='right trapezium':
                shape_list.append(shape2)
              else:  
                shape_list.append(shape)
              bases=re.search(r'(bases|sides)\s*(\d+\.?\d*)\s*(?:cm)?\s*and\s*(\d+\.?\d*)\s*(?:cm)?|(\d+\.?\d*)\s*(?:cm)?\s*and\s*(\d+\.?\d*)\s*(?:cm)?\s*(bases|sides)',text)
              if bases:
                num1=float(bases.group(2) or bases.group(4))
                print(num1)
                num2=float(bases.group(3) or bases.group(5))
                print(num2)
                if num1>num2:
                   longer_base=num1
                   shorter_base=num2
                else:
                   longer_base=num2
                   shorter_base=num1
              else:
                longer_base=5
                shorter_base=3
              dimensions['trapezium_longer_base']=longer_base
              dimensions['trapezium_shorter_base']=shorter_base
              height=re.search(r'(height|length)\s*(\d+\.?\d*)\s*(?:cm)?|(\d+\.?\d*)\s*(?:cm)?\s*(height|length)',text)  
              if height:
                heightt=height.group(2) or height.group(3)
              else:
                 heightt=3
              dimensions['trapezium_height']=heightt
              
              for prop in shapes[shape][1]:
                  if prop in text:
                    props.append(prop)

            elif shape=='rhombus':
              shape_list.append(shape)
              diagonals=re.search(r'diagonals?\s*(\d+\.?\d*)\s*\w*\s*(\d+\.?\d*)\b',text,re.IGNORECASE)
              if diagonals:
                diag1=float(diagonals.group(1))
                dimensions['rhombus_diagonal1']=diag1
                diag2=float(diagonals.group(2))
                dimensions['rhombus_diagonal2']=diag2
              else:
                diagonal1 = re.search(r'(\d+\.?\d*)\s*(cm)?\s*(diagonal1|d1)|(diagonal1|d1)\s*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)
                diagonal2 = re.search(r'(\d+\.?\d*)\s*(cm)?\s*(diagonal2|d2)|(diagonal2|d2)\s*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)

                if diagonal1:
                    dimensions['rhombus_diagonal1'] = float(diagonal1.group(1) or diagonal1.group(4))
                else:
                    dimensions['rhombus_diagonal1'] = 4  # default length

                if diagonal2:
                    dimensions['rhombus_diagonal2'] = float(diagonal2.group(1) or diagonal2.group(4))
                else:
                    dimensions['rhombus_diagonal2'] = 3  # default breadth

              for prop in shapes[shape]:
                if prop in text:
                  props.append(prop)

            elif shape == 'ellipse':
              print("hello ellipse")
              shape_list.append(shape)
              axes=re.search(r'axes?\s*(\d+\.?\d*)\s*\w*\s*(\d+\.?\d*)\b',text,re.IGNORECASE)
              if axes:
                num1=float(axes.group(1))
                num2=float(axes.group(2))
                if num1>num2:
                  dimensions['major-axis']=num1
                  dimensions['minor-axis']=num2
                else:
                  dimensions['major-axis']=num1
                  dimensions['minor-axis']=num2
              else:
                major_axis=re.search(r'(\d+\.?\d*)\s*(cm)?\s*(major\s*axis|major-axis)|(major\s*axis|major-axis)\s*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)
                print("major axis extracted")
                if major_axis:
                   dimensions['major-axis']=float(major_axis.group(1) or major_axis.group(5))
                else:
                   dimensions['major-axis']=6 
                minor_axis=re.search(r'(\d+\.?\d*)\s*(cm)?\s*(minor\s*axis|minor-axis)|(minor\s*axis|minor-axis)\s*\w*(\d+\.?\d*)\s*(cm)?', text, re.IGNORECASE)
                if minor_axis:
                   dimensions['minor-axis']=float(minor_axis.group(1) or minor_axis.group(5))
                else:
                   dimensions['minor-axis']=4

              for prop in shapes[shape]:
                if prop in text:
                  props.append(prop)

            dimensions_list.append(dimensions)
    print("props",props)
    print("dimensions",dimensions_list)
    return shape_list, dimensions_list, props
