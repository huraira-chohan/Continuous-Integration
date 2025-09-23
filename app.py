import streamlit as st

st.title("Power Calculator")
st.write("Cal power of numbers.")

n = st.number_input("Enter any number :",value=1,step=1)

square = n**2
cube = n**3
fifth = n**5

st.write(f"Square of {n} is {square}.")
st.write(f"Cube of {n} is {cube}.")
st.write(f"Fifth of {n} is {fifth}.")


