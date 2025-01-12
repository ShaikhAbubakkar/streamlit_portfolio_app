import streamlit as st
import streamlit.components.v1 as components

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

components.html(GA_TRACKING_CODE, height=0, width=0)


# --- PAGE SETUP ---
about_page = st.Page(
    page='views/about_me.py',
    title='About me',
    icon=':material/account_circle:',
    default=True
)

project_1_page = st.Page(
    page='views/dashboard.py',
    title='Sales Dashboard',
    icon=':material/bar_chart:',
)

project_2_page = st.Page(
    page='views/chatbot.py',
    title='Chat Bot',
    icon=':material/smart_toy:',
)

# --- NAIVGATION SETUP [WITHOUT SECTION] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

pg = st.navigation(
    {
        'Info': [about_page],
        'Projects': [project_1_page, project_2_page],
    }
)

# --- RUN NAVIGATION ---
pg.run()