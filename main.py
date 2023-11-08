import helpers.langchain_helper as lch
import streamlit as stl
import helpers.streamlit_helper as stlhelper

stl.title("Pets name generator")

user_animal_type = stl.sidebar.selectbox("What is your pet?",("Cat","Dog","Cow","Chicken"))

user_pet_color = stlhelper.pet_color_text(user_animal_type)

if user_pet_color:
    response = lch.generate_pet_name(user_animal_type,user_pet_color)
    stl.text(response['pet_name'])