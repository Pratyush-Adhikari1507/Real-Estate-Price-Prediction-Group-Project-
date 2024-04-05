import streamlit as st
from predict import show_predict_page
from contact import show_contact_page
from about import show_about_page
import sklearn

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏡",
)

from explore import show_explore_page
from comparison import show_comparison_page

page_options = ["Home", "Explore", "Comparison of models", "About", "Contact"]
selected_page = st.sidebar.radio("Navigation", page_options)

if selected_page == "Home":
    show_predict_page()
elif selected_page == "Explore":
    show_explore_page()
elif selected_page == "Comparison of models":
    show_comparison_page()
elif selected_page == "About":
    show_about_page()
elif selected_page == "Contact":
    show_contact_page()