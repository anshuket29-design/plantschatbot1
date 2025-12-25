import streamlit as st
from backend import analyze_plant_text

st.set_page_config(
    page_title="🌾 Krishi AI Mitra",
    page_icon="🌱",
    layout="wide"
)

st.title("🌾 Krishi AI Mitra")
st.write("Describe crop symptoms to get disease & treatment")

user_input = st.text_area(
    "📝 Enter crop name & symptoms",
    placeholder="Example: Tomato plant leaves turning yellow with brown spots..."
)

if st.button("🔍 Analyze"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = analyze_plant_text(user_input)
            st.success("✅ Analysis Complete")
            st.markdown(result)
    else:
        st.warning("Please enter crop details.")
