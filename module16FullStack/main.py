import streamlit as st

#def main():
  #  st.title("Hello World")

   # st.button("click me")

#if __name__ == "__main__":
  #  main()


if st.button("click me"):
    st.write("Button clicked")

st.checkbox("check me")

if st.checkbox("check me to show text"):
    st.write("some text")

user_input = st.text_input("enter texxt", "sample")
st.write("you entered", user_input)
age = st.number_input("enter age:", min_value=0, max_value=100)
st.write(f"your age is:{age}")

message = st.text_area("enter a message")
st.write(f"your message:{message}")

choice = st.radio("pick one", [1, 2, 3])
if st.button("Success"):
    st.success("Operation was successful")

try:
    1 / 0
except Exception as e:
    st.exception(e)
