import streamlit as st
import requests
from datetime import datetime

# Title of the survey
st.title("User Survey")

# Survey questions
favorite_color = st.selectbox("What is your favorite color?", ["Red", "Blue", "Green", "Yellow", "Other"])
favorite_animal = st.selectbox("What is your favorite animal?", ["Dog", "Cat", "Bird", "Fish", "Other"])
favorite_food = st.selectbox("What is your favorite food?", ["Pizza", "Burger", "Sushi", "Pasta", "Other"])
favorite_celebrity = st.text_input("Who is your favorite celebrity?")

# Complete button
# if st.button("Complete Survey"):
#     # JSON data to send
#     survey_data = {
#         "favorite_color": favorite_color,
#         "favorite_animal": favorite_animal,
#         "favorite_food": favorite_food,
#         "favorite_celebrity": favorite_celebrity,
#     }

if st.button("Complete Survey"):
    # Generate a timestamp for uniqueness
    timestamp = datetime.now().isoformat()

    # JSON data to send
    survey_data = {
        "timestamp": timestamp,  # Unique identifier for each submission
        "favorite_color": favorite_color,
        "favorite_animal": favorite_animal,
        "favorite_food": favorite_food,
        "favorite_celebrity": favorite_celebrity,
    }

    # Webhook URL (replace this with your Make Webhook URL)
    webhook_url = "https://hook.us2.make.com/tl5sqx3rx1mvq3p3kqscsmssmhovh95a"

    # Send data to Make using POST request
    response = requests.post(webhook_url, json=survey_data)

    # Display response status
    if response.status_code == 200:
        st.success("Survey completed successfully! Data has been sent.")
    else:
        st.error("Failed to send survey data.")
