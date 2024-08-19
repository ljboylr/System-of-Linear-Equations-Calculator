import streamlit as st
import numpy as np

# Set the background image and color
st.set_page_config(page_title="System of Linear Equations Calculator", layout="wide", page_icon=":cat:")

st.sidebar.title('SLE Calculator')
choices = st.sidebar.selectbox('Select Option', ('Home', 'SLE Calculator'))
if choices == 'Home':
    st.markdown("""<style>.stApp{background-color :  #00203FFF;} </style>
    """,unsafe_allow_html=True)
    st.markdown("""
                <h1 style="font-size: 45px; font-family: 'Arial, sans-serif'; text-align: center;color:#ADEFD1FF ">
                Coding Exercise in Advance Mathematics
                </h1>
                <p style='text-align: center; font-size: 35px;color:    #ADEFD1FF;
                '>"SYSTEM OF LINEAR EQUATION Calculator"</p>
            """, unsafe_allow_html=True)


elif choices == 'SLE Calculator':
    st.markdown("""<style>.stApp{background-color :  #00203FFF;} </style>
        """, unsafe_allow_html=True)
    st.markdown("""
            <h1 style="font-size: 40px; font-family: 'Arial, sans-serif'; text-align: center; color: #ADEFD1FF">
            "Please Input to calculate"!!
            </h1>
        """, unsafe_allow_html=True)

    # Get the size of the matrices from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                Input number of Linear Equations:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        num_equations = st.number_input("", min_value=2, max_value=5, key='num_equations')

    # Create empty lists to store the coefficients and constants
    coefficients = []
    constants = []

    # Get the coefficients and constants from the user
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("""
                <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                Input for the Coefficients and Constants:
                </h1>
            """, unsafe_allow_html=True)
    with col2:
        for i in range(num_equations):
            st.markdown("""
                        <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                        Equation
                        </h1>
                    """, unsafe_allow_html=True)
            st.subheader(f"{i + 1}")
            col = st.columns(num_equations, gap="medium")
            row_coeffs = []
            for j in range(num_equations):
                with col[j]:
                    st.markdown("""
                                <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                                Coefficients
                                </h1>
                            """, unsafe_allow_html=True)
                    coeff = st.number_input(f"{j + 1}", key=f"coeff_{i}_{j}", format="%f")
                    row_coeffs.append(coeff)
            st.markdown("""
                                        <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                                        Constants
                                        </h1>
                                    """, unsafe_allow_html=True)
            constants.append(st.number_input("", key=f"const_{i}"))
            coefficients.append(row_coeffs)

    # Create the coefficient and constant matrices
    coefficient_matrix = np.array(coefficients)
    constant_matrix = np.array(constants)


    # Define a function to calculate the inverse of a matrix
    def inverse_matrix(matrix):
        return np.linalg.inv(matrix)


    # Define a function to solve the system of equations
    def solve_system(coefficient_matrix, constant_matrix):
        matrix_inv = np.linalg.inv(coefficient_matrix)
        solution = np.dot(matrix_inv, constant_matrix)
        return solution


    # Add a button to solve the system of equations
    if st.button("Calculate"):
        # Check if the coefficient matrix is square
        if coefficient_matrix.shape[0] != coefficient_matrix.shape[1]:
            st.error("The coefficient matrix must be square.")
        else:
            # Check if the determinant of the coefficient matrix is non-zero
            if np.linalg.det(coefficient_matrix) == 0:
                st.error("The coefficient matrix is singular and cannot be solved.")
            else:
                # Calculate the inverse of the coefficient matrix
                A = inverse_matrix(coefficient_matrix)
                # Calculate the solution
                X = solve_system(coefficient_matrix, constant_matrix)
                # Display the inverse of the coefficient matrix and the constant matrix
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("""
                                                <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                                                Step by Step Solution:
                                                </h1>
                                            """, unsafe_allow_html=True)
                with col2:
                    st.subheader("")
                    st.write(np.round(A, 2))
                with col3:
                    st.subheader("")
                    st.write(np.round(constant_matrix, 2))
                # Display the solution
                st.markdown("""
                                                            <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                                                            Solution of the System of Linear Equations:
                                                            </h1>
                                                        """, unsafe_allow_html=True)
                st.subheader("")
                for i, root in enumerate(X):
                    st.write(f"X{i + 1}: {root}")
    # Add divider
    st.divider()

# Add credits
col1, col2, col3, col4, col5 = st.columns(5)


with col3:
    st.markdown("""  <h1 style="font-size: 30px; font-family: 'Arial, sans-serif'; text-align: left; color: #ADEFD1FF">
                                      LLJ TEAM  
                                        </h1>
                                    """, unsafe_allow_html=True)
with col4:


    st.image("image1.jpg",  width=200)
    

with col5:
    pass

    st.image("image2.jpg", width=200)
st.markdown("""
            <h1 style="font-size: 20px; font-family: 'Arial, sans-serif'; text-align: right; color:#ADEFD1FF; margin-right: 150px">
         LAREY JAHN BAUGBOG-LESTER POLENIO
             </h1>
         """, unsafe_allow_html=True)
