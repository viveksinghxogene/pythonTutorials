import streamlit as st

st.header("This is the simpel calculator")

num1 = st.number_input("Enter first num")
num2 = st.number_input("Enter second num")
operation = st.selectbox("Choose Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    else:
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    st.success(f"Result: {result}")