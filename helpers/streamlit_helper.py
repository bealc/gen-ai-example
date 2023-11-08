import streamlit as stl

def pet_color_text(animal_type): 
    pet_color = stl.sidebar.text_area(label=f"What color is your {animal_type}?",max_chars=15)
    return pet_color