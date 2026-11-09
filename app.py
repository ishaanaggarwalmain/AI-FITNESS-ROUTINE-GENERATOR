import streamlit as st
from google import genai

st.title("🏋️‍♂️ AI Fitness Routine Generator")
st.write("Enter your details below to get a personalized weekly workout plan.")

# 1. Simple User Inputs
age = st.number_input("Age", min_value=15, max_value=70, value=19)
weight = st.number_input("Weight (in kg)", min_value=35.0, max_value=150.0, value=65.0)
height = st.number_input("Height (in cm)", min_value=120.0, max_value=220.0, value=170.0)
goal = st.selectbox("Fitness Goal", ["Muscle Gain", "Fat Loss", "General Fitness"])
level = st.selectbox("Experience Level", ["Beginner", "Intermediate"])
days = st.slider("Workout Days per Week", 2, 6, 3)
equipment = st.selectbox("Available Equipment", ["Bodyweight Only", "Dumbbells Only", "Full Gym"])

# 2. Simple Python Logic (BMI + Split Rule)
bmi = round(weight / ((height / 100) ** 2), 1)
if days <= 3:
    split = "Full Body Workout Split"
elif days == 4:
    split = "Upper / Lower Body Split"
else:
    split = "Push / Pull / Legs (PPL) Split"

# 3. Generate Plan Button
if st.button("Generate My Workout Plan"):
    st.subheader(f"📊 Your Stats: BMI is {bmi} | Recommended: {split}")
    
    # Replace with your free key from aistudio.google.com when running locally
    client = genai.Client(api_key="YOUR_GEMINI_API_KEY")
    prompt = f"""
    Create a {days}-day {split} workout table for a {age}-year-old {level} 
    with BMI {bmi}. Goal: {goal}. Equipment allowed: {equipment} ONLY.
    Show Day, Exercise Name, Sets, Reps, and Rest time in a clean Markdown table.
    """
    with st.spinner("Generating your personalized plan..."):
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        st.markdown(response.text)
