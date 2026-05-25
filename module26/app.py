import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Recipe CRUD App")

st.header("Add Recipe")

recipe_name = st.text_input("Recipe Name")
recipe_desc = st.text_area("Recipe Instructions")
recipe_author = st.text_input("Author")

if st.button("Create Recipe"):

    data = {
        "name": recipe_name,
        "instructions": recipe_desc,
        "author": recipe_author
    }

    response = requests.post(
        f"{API_URL}/recipes/",
        json=data
    )

    if response.status_code == 200:
        recipes = response.json()

st.header("All Recipes")

response = requests.get(f"{API_URL}/recipes/")

if response.status_code == 200:

    recipes = response.json()

    if recipes:
        df = pd.DataFrame(recipes)
        st.dataframe(df)
    else:
        st.info("No recipes found")

st.header("Update Recipe")

update_id = st.number_input(
    "Recipe ID to Update",
    min_value=1,
    step=1
)

update_name = st.text_input("Updated Recipe Name")
update_instructions = st.text_area("Updated Instructions")
update_author = st.text_input("Updated Author")

if st.button("Update Recipe"):

    updated_data = {
        "name": update_name,
        "instructions": update_instructions,
        "author": update_author
    }

    response = requests.put(
        f"{API_URL}/recipes/{update_id}",
        json=updated_data
    )

    if response.status_code == 200:
        st.success("Recipe updated successfully!")
    else:
        st.error("Recipe not found")

st.header("Delete Recipe")

delete_id = st.number_input(
    "Recipe ID to Delete",
    min_value=1,
    step=1
)

if st.button("Delete Recipe"):

    response = requests.delete(
        f"{API_URL}/recipes/{delete_id}"
    )

    if response.status_code == 200:
        st.success("Recipe deleted successfully!")
    else:
        st.error("Recipe not found")



