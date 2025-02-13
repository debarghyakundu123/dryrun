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

# Feedback Section
st.markdown("---")
st.subheader("📝 We Value Your Feedback")
feedback = st.text_area("Please share your thoughts or suggestions to improve our platform:")
if st.button("Submit Feedback"):
    st.success("Thank you for your valuable feedback!")

# Newsletter Subscription
st.markdown("---")
st.subheader("📬 Subscribe to Our Newsletter")
email = st.text_input("Enter your email to stay updated:")
if st.button("Subscribe"):
    st.success(f"Subscribed successfully with email: {email}")

st.markdown("---")
st.write("Empowering Learners, Transforming Futures")
