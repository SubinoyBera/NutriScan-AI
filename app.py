import streamlit as st
from PIL import Image
from helper_functions import HelperFunctions

# Streamlit UI

st.set_page_config(page_title="NutriScan AI", layout="centered", page_icon=":apple:")

st.title("NutriScan AI - Personal Nutrition Analyzer 👨‍⚕️🎓")

st.write("Upload a food image and get its nutritional insights 📊")

# File uploader for food image
uploaded_image = st.file_uploader("📤 Upload image of your food", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_image is not None:
    image_display = Image.open(uploaded_image)
    st.image(image_display, caption="Uploaded Food Image", use_container_width=True)

# Prompt for LLM to provide analysis
health_analysis_prompt = """
You are a senior nutritionist expert. Analyze the food items in this image and provide:
1. Name of each food items present
2. Estimated calorie count
3. Macronutrient breakdown (carbs, proteins, fats)
4. Health rating (Healthy / Unhealthy / Moderate)
5. If unhealthy, explain why and suggest a healthier alternative.
6. Summary: Should this meal be part of a healthy diet? What to add or remove?
If the image has no food items reply as "Sorry, No food item found in the uploaded image!"
"""

if st.button("🔍 Start Analysis"):
    try:
        with st.spinner("Preparing report ..."):
            obj = HelperFunctions()
            image_data = obj.prepare_image_data(uploaded_image)
            analysis_result = obj.analyze_food_image(health_analysis_prompt, image_data)
            st.success("✅ Analysis Complete!")
            st.markdown(analysis_result)
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")