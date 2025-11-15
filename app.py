import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to cal its sq, cube and 5th power : ")
n = st.number_input("Enter any integer : ",value=1,step=1)

square = n*n
cube = n*n*n
fifth = n**5

st.write(f"Square is {square}")
st.write(f"Cube is {cube}")
st.write(f"Fifth power is {fifth}")

