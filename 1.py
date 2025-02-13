import streamlit as st

st.set_page_config(page_title="Education Platform", page_icon="📚")

st.title("📚 Welcome to the Education Platform")
st.image("home.jpg", caption="Empowering Education Through Technology", use_column_width=True)
st.write("Explore our available courses and connect with us on social media.")

st.subheader("📖 Available Courses")
courses = {
    "Railway Science Foundation": "https://t.me/+Ja5IJyCmnMVkM2Vl",
    "CGL + CHSL + MTS MAINS": "https://t.me/+DumAzg8tD3I5NDc1",
    "Machine Learning Basics": "https://example.com/ml",
    "Web Development": "https://example.com/webdev"
}

for course, link in courses.items():
    st.markdown(f"- [{course}]({link})")

st.subheader("📢 Stay Connected")
st.markdown("[Join our Telegram](https://t.me/+XuIEiecTujMxODNl)")
st.markdown("[Follow us on WhatsApp](https://whatsapp.com/channel/0029Vb25egi7oQhbkaBNse2o)")
st.markdown("[Follow us on Instagram](https://instagram.com/example)")
