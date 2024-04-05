import streamlit as st

def show_about_page():
    st.title("About Us")

    st.write(
        "1. Welcome to Our Real Estate Price Prediction Application!\n"
        "2. We are dedicated to providing you with accurate and insightful price predictions.\n"
        "3. ⚠️THIS WEBSITE IS USED FOR TRAINING AND DEVELOPMENT PURPOSES⚠️"
        )
    
    team_image = "images/project members.png"
    st.image(team_image, use_column_width=True)

    st.success("Thank you for choosing our App!")