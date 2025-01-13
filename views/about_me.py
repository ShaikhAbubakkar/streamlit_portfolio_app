import streamlit as st
from forms.contact import contact_form

GA_TRACKING_CODE = """
    <!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-KQ7W446XQW"></script>
<script>

  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-KQ7W446XQW');
</script>
"""
st.markdown(GA_TRACKING_CODE, unsafe_allow_html=True)


@st.dialog('Contact Me')
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image("./assets/Abubakkar.jpg", width=230)

with col2:
    st.title("Shaikh Abubakkar", anchor=False)
    st.subheader("Aspiring Software Developer")
    st.write("Undergrad IT Engineering Student | Aspiring Software Developer | Vice Chairperson @ACM-MHSSCE | System Design and DSA Enthusiast | Specialising in AI & ML")

    if st.button('✉️ Contact Me!'):
        show_contact_form()

# --- EXPERIENCE AND QUALIFICATIONS ---
st.write('\n')
st.subheader('Experience & Qualifications', anchor=False)
st.write(
    """
    - Vice Chaiperson at ACM-MHSSCE
    - AWS Academy Core Committee Member at MHSSCE
    - B.E. in Information Technology, MHSSCE 
    """
)

st.write('\n')
st.subheader("Skills", anchor=False)
st.write(
    """
    - Programming Languages: Python, Java, C++
    - DevOps Tools: Jenkins, JIRA, Docker, AWS Cloud
    - Public Speaking
    """
)