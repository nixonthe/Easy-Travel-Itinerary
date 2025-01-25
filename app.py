from main import App
import streamlit as st

model = App()

st.title("Seoul Travel Itinerary")
st.write("Find the best travel itinerary tailored for you!")

user_query = st.text_input("Enter your travel question (e.g., 'What are some recommended places to visit in Seoul?')")

if st.button("Get Recommendation"):
    response = model.run_query(user_query)
    st.write("### Recommended Itinerary:")
    st.write(response)
