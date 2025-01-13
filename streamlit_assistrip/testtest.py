import streamlit as st

# Get query parameters
params = st.experimental_get_query_params()

# Extract data
name = params.get("name", [""])[0]
sightseeing = params.get("sightseeing", [""])[0]
activities = params.get("activities", [""])[0]
restaurants = params.get("restaurants", [""])[0]

# Display the data
st.title("New Data from Google Sheets")
if name:
    st.write(f"**Name:** {name}")
    st.write(f"**Sightseeing:** {sightseeing}")
    st.write(f"**Activities:** {activities}")
    st.write(f"**Restaurants:** {restaurants}")
else:
    st.write("Waiting for data...")
