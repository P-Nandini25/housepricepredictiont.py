import streamlit as st

st.title("🏠 House Price Predictor (No ML)")

# User Inputs
sqft = st.number_input("Enter Square Footage", min_value=100, max_value=10000, step=50)
bedrooms = st.slider("Number of Bedrooms", 1, 10, 3)
bathrooms = st.slider("Number of Bathrooms", 1, 10, 2)
location = st.selectbox("Location Type", ["Urban", "Suburban", "Rural"])

# Custom price calculation logic
def calculate_price(sqft, bedrooms, bathrooms, location):
    base_price = 500000
    location_factor = {"Urban": 1.5, "Suburban": 1.2, "Rural": 1.0}
    price = base_price
    price += sqft * 3000
    price += bedrooms * 100000
    price += bathrooms * 80000
    price *= location_factor[location]
    return price

# Button to trigger prediction
if st.button("Predict Price"):
    final_price = calculate_price(sqft, bedrooms, bathrooms, location)
    st.success(f"🏷️ Estimated House Price: ₹{final_price:,.0f}")
