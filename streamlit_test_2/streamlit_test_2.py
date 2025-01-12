import streamlit as st
import requests

# Title of the app
st.title("Search App")

# Search bar
user_input = st.text_input("Enter your search query:")

# When the user presses Enter
if user_input:
    # Webhook URL
    webhook_url = "https://hook.us2.make.com/y0697pbs9m5p6wqw39dte2tngoejxfbj"

    # JSON payload
    data = {"search_query": user_input}

    # Send data to Make Webhook
    response = requests.post(webhook_url, json=data)

    if response.status_code == 200:
        st.success("Search query sent successfully!")
    else:
        st.error("Failed to send search query.")
