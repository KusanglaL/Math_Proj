"""
This module contains a Streamlit app that demonstrates shape and equation solving functionality.
"""
import streamlit as st
import string 
import regex as re
import spacy   
from spacy.lang.en import English
import pytesseract
from PIL import Image
from circle import plot_circle, plot_circle_with_radius_and_diameter, plot_circle_with_area, plot_circle_with_perimeter_or_circumference,plot_inscribed_or_circumscribed_circle, plot_sector
from rectangle import plot_rectangle, plot_rectangle_with_area,plot_rectangle_with_perimeter_or_circumference,plot_rectangle_with_perimeter_or_circumference, plot_rectangle_with_diagonals
from square import plot_square, plot_square_with_area,plot_square_with_perimeter_or_circumference, plot_square_with_diagonal
from triangle import plot_triangle, plot_triangle_with_area,plot_triangle_with_perimeter_or_circumference
from equilateral_triangle import plot_equilateral_triangle,plot_equilateral_triangle_with_area,plot_equilateral_triangle_with_perimeter_or_circumference
from isosceles_triangle import plot_isosceles_triangle,plot_isosceles_triangle_with_area,plot_isosceles_triangle_with_perimeter_or_circumference
#from scalene_triangle import plot_scalene_triangle,plot_scalene_triangle_with_area,plot_scalene_triangle_with_perimeter_or_circumference
from polygon import plot_regular_polygon,plot_regular_polygon_with_area,plot_regular_polygon_with_perimeter_or_circumference
from parallelogram import plot_parallelogram, plot_parallelogram_with_area,plot_parallelogram_with_perimeter_or_circumference, plot_parallelogram_with_angles, plot_parallelogram_with_diagonals
from rhombus import plot_rhombus, plot_rhombus_with_area,plot_rhombus_with_perimeter_or_circumfernce, plot_rhombus_with_angles
from trapezium import plot_trapezium, plot_trapezium_with_area, plot_isosceles_trapezium, plot_right_trapezium
from ellipse import plot_ellipse, plot_ellipse_with_area, plot_ellipse_with_foci, plot_ellipse_within_rectangle
from extract_shapes import extract_shapes_and_dimensions
from plot_shapes import plot_shape, equation_operations

# Load spaCy English model
nlp = English()
print(nlp)


# Example questions for each shape and equation
example_questions = {
    "circle": [
        "Plot a circle with radius 5",
        "Draw a circle with a radius of 10 units",
        "Show me a circle of radius 3",
        "Plot a circle with diameter 10",
        "Show the area and circumference of a circle with radius 5",
        "Show a sector of a circle with radius 5 and angle 45 degrees"
    ],
    "rectangle": [
        "Plot a rectangle with length 10 and width 5",
        "Draw a rectangle with dimensions 8 by 3",
        "Show me a rectangle of length 4 and width 2",
        "Show the area and perimeter of a rectangle with length 10 and width 5",
        "Display a rectangle with diagonals"
    ],
    "square": [
        "Plot a square with side 6",
        "Draw a square with side length 4",
        "Show me a square with a side of 8",
        "Show the area and perimeter of a square with side 5",
        "Display a square with its diagonal"
    ],
    "triangle": [
        "Plot a triangle with base 8 and height 4",
        "Draw a triangle with a base of 6 and height of 5",
        "Show me a triangle with base 7 and height 3",
        "Show the area of a triangle with base 10 and height 5",
        "Display a right triangle with legs 3 and 4",
        "Show an equilateral triangle with side 5",
        "Display an isosceles triangle with base 8 and sides 5",
        "Show a scalene triangle with sides 5, 7, and 10"
    ],
    "parallelogram": [
        "Plot a parallelogram with base 7 and height 3",
        "Draw a parallelogram with base 5 and height 2",
        "Show me a parallelogram with base 6 and height 4",
        "Show the area of a parallelogram with base 8 and height 4",
        "Show me the perimeter of a parallelogram with base 8 and height 4",
        "Display a parallelogram with angles 60 and 120 degrees",
        "Show a parallelogram with its diagonals"
    ],
    "rhombus": [
        "Plot a rhombus with diagonals 6 and 8",
        "Draw a rhombus with diagonals 5 and 7",
        "Show me a rhombus with diagonals 4 and 9",
        "Show the area of a rhombus with diagonals 6 and 8",
        "Display a rhombus with angles 45 and 135 degrees"
    ],
    "trapezium": [
        "Plot a trapezium with bases 8 and 6, and height 4",
        "Draw a trapezium with bases 5 and 3, and height 2",
        "Show me a trapezium with bases 7 and 4, and height 3",
        "Show the area of a trapezium with bases 8 and 6, and height 4",
        "Display an isosceles trapezium with bases 10 and 6, and sides 5",
        "Show a right trapezium with bases 8 and 6, and height 4"
    ],
    "pentagon": [
        "Plot a regular pentagon with side 5",
        "Draw a pentagon with side length 6",
        "Show me a pentagon with a side of 4",
        "Show the area of a pentagon with side 5",
        "Display a pentagon with internal angles labeled",
        "Show a pentagon inscribed by a circle",
        "Show a pentagon  and circumscribed by a circle"
    ],
    "hexagon": [
        "Plot a regular hexagon with side 4",
        "Draw a hexagon with side length 5",
        "Show me a hexagon with a side of 6",
        "Show the area of a hexagon with side 5",
        "Display a hexagon with internal angles labeled",
    ],
    "heptagon": [
        "Plot a regular heptagon with side 4",
        "Draw a heptagon with side length 5",
        "Show me a heptagon with a side of 6",
        "Show the area of a heptagon with side 5",
        "Display a heptagon with internal angles labeled",
    ],
    "octagon": [
        "Plot a regular octagon with side 4",
        "Draw a octagon with side length 2",
        "Show me a octagon with a side of 5",
        "Show the area of a octagon with side 5",
        "Display a octagon with internal angles labeled",
    ],
    "nonagon": [
        "Plot a regular nonagon with side 4",
        "Draw a nonagon with side length 5",
        "Show me a nonagon with a side of 6",
        "Show the area of a nonagon with side 5",
        "Display a nonagon with internal angles labeled",
    ],
    "decagon": [
        "Plot a regular decagon with side 4",
        "Draw a decagon with side length 5",
        "Show me a decagon with a side of 6",
        "Show the area of a decagon with side 5",
        "Display a decagon with internal angles labeled",
    ],
    "ellipse": [
        "Plot an ellipse with major axis 10 and minor axis 5",
        "Draw an ellipse with axes 8 and 4",
        "Show me an ellipse with major axis 7 and minor axis 3",
        "Show the area of an ellipse with major axis 10 and minor axis 5",
        "Display an ellipse with its foci",
    ],
    "equation": [
        "Linear 2*x + 1",
        "Quadratic x**2 - 4*x + 4",
        "Cubic x**3 - 6*x**2 + 11*x - 6",
        "Polynomial x**4 - 7*x**3 + 3*x**2 - 5*x + 9",
        "Rational (x**2 + 1) / (x - 2)",
        "Exponential exp(x) - 2",
        "Logarithmic log(x) - 1",
        "Trigonometric (Sin) sin(x) - 0.5",
        "Trigonometric (Cos) cos(x) + 0.5",
        "Trigonometric (Tan) tan(x) - 1",
        "Inverse Trigonometric asin(x) + acos(x)",
        "Hyperbolic sinh(x) - cosh(x)",
        "Absolute Value Abs(x) - 2",
        "Square Root sqrt(x) - 2",
        "Complex x**2 + 1",
        "Piecewise Piecewise((x**2, x < 0), (x, x >= 0))"
    ]
}
# Streamlit App
st.set_page_config(page_title="AI Geometry and Equation Solver", page_icon=":bar_chart:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* ... [Keep all the existing CSS styles] ... */
    </style>
""", unsafe_allow_html=True)

# Header
st.title("AI Geometry and Equation Solver :bar_chart:")
st.markdown("### Plot geometric shapes and solve mathematical equations!")

def shape_interface():
    # Sidebar for selecting shapes and showing example questions
    st.sidebar.header("Example Questions")
    selected_shape = st.sidebar.selectbox("Select a shape:", [k for k in example_questions.keys() if k != "equation"], key="shape_selectbox")
    st.sidebar.write("### Example Questions for", selected_shape)
    for example in example_questions[selected_shape]:
        st.sidebar.write(f"- {example}")

    # Options to customize plot
    fill = st.sidebar.checkbox("Fill Shape", value=False, key="fill_checkbox")
    color = st.sidebar.color_picker("Choose Color", value='#0000FF', key="color_picker")  # Default to blue in hex

    # Main area for shapes
    st.markdown("#### Enter your question about a shape:")
    user_question = st.text_area("Shape Query", placeholder="e.g., Plot a circle with radius 5", key="shape_query_textarea")

    if st.button("Generate Shape Plot", key="generate_shape_plot_button"):
        if user_question:
            shape_list, dimensions_list, properties = extract_shapes_and_dimensions(user_question)
            plot_shape(user_question, shape_list, dimensions_list, properties)

def equation_interface():
    # Sidebar for equation examples
    st.sidebar.header("Example Equations")
    for example in example_questions["equation"]:
        st.sidebar.write(f"- {example}")

    # Main area for equations
    equation_operations()

def main():
    st.sidebar.title("Navigation")
    options = st.sidebar.radio("Choose an operation", ["Shapes", "Equation Solver"])

    if options == "Shapes":
        shape_interface()
    elif options == "Equation Solver":
        equation_interface()

if __name__ == "__main__":
    main()
