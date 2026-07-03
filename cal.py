import streamlit as st

st.title("WELCOME TO VIVEK'S CALCULATOR")
usr = st.text_input("What's your name??")

if usr:
    st.write("Hello", usr, "my name is vivek, let's start calculating")
    num1 = st.number_input("Enter the first number", value=None)
    
    if num1 is not None:
        num2 = st.number_input("Enter the second number", value=None)
        
        if num2 is not None:
            opp = st.text_input("Enter the operation '+', '-', '*', '/'").strip()
            
            if st.button("Calculate"):
                st.balloons()
                if opp == '+':
                    st.code("Addition is :" + str(num1 + num2))
                elif opp == '-':
                    st.code("Subtraction is: " + str(num1 - num2))
                elif opp == '*':
                    st.code("Multiplication is :" + str(num1 * num2))
                elif opp == '/':
                    if num2 != 0:
                        st.code("Division is :" + str(num1 / num2))
                    else:
                        st.error("cant divided by 0")
                else:
                    st.warning("Invalid operation")
