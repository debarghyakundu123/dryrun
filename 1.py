import streamlit as st

st.set_page_config(page_title="Education Platform", page_icon="📚", layout="centered")

# Header Section
st.title("📚 Welcome to the Education Platform")
st.image("home.jpg", caption="Empowering Education Through Technology", use_column_width=True)
st.write("Explore our curated selection of courses and connect with us on social media.")

# Courses Section
st.subheader("📖 Available Courses")
courses = {
    "Railway Science Foundation": "https://t.me/+Ja5IJyCmnMVkM2Vl",
    "CGL + CHSL + MTS MAINS": "https://t.me/+DumAzg8tD3I5NDc1",
    "Machine Learning Basics": "https://example.com/ml",
    "Web Development": "https://example.com/webdev"
}

for course, link in courses.items():
    st.markdown(f"- [{course}]({link})")

# Divider
st.markdown("---")

# Social Media Section
st.subheader("📢 Stay Connected")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[Join our Telegram](https://t.me/+XuIEiecTujMxODNl)")

with col2:
    st.markdown("[Follow us on WhatsApp](https://whatsapp.com/channel/0029Vb25egi7oQhbkaBNse2o)")

with col3:
    st.markdown("[Follow us on Instagram](https://instagram.com/example)")

st.markdown("---")
st.write("Empowering Learners, Transforming Futures")
