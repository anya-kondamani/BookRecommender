import streamlit as st
from recommender import get_recommendations,personalized_recommendations

user_title = st.text_input("Enter a book title you like:")
author_preference = st.text_input("Do you have a preferred author? If so, enter their name or press Enter to skip: ").lower()
year_preference = st.text_input("Do you prefer books from a specific publication year? If so, enter the year or press Enter to skip: ")

personalized_recs = personalized_recommendations(user_title, author_preference, year_preference)
print("\nBased on your preferences, you might enjoy:\n")

st.title("Welcome to the Book Recommendation System")

if st.button("Get Recommendations"):
    for i, title in enumerate(personalized_recs, 1):
        st.write(f"{i}. {title}")
    