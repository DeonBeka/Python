import streamlit as st
st.title("Calculator App")
num1_input = st.number_input("enter the first number" )
num2_input = st.number_input("enter the second number" )
result = 0
if st.button("add"):
    result = num1_input + num2_input
    st.write(f"Your sum is {result}")

if st.button("subtract"):
    result = num1_input - num2_input
    st.write(f"Your result is {result}")

if st.button("here"):
    result = num1_input * num2_input
    st.write(f"Your result is {result}")

if st.button("/"):
    result = num1_input / num2_input
    st.write(f"Your result is {result}")





