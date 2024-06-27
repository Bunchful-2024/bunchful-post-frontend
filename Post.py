import streamlit as st

# Title
st.title("Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Section 1: Content Curation
st.subheader("Step1: Content Curation")
st.write("Modify your content with the help of AI.")
# Defining Multi_Select with Pre-Selection
topics = st.multiselect(
       "Select your topic",
       ['1: No Poverty', '2: Zero Hunger', '3: Good Health and Well-Being', '4: Quality Education',
        '5: Gender Equality', '6: Clean Water and Sanitation', '7: Affordable and Clean Energy',
        '8: Decent Work and Economic Growth', '9: Industry, Innovation, and Infrastructure',
        '10: Reduced Inequalities', '11: Sustainable Cities and Communities', '12: Responsible Consumption and Production',
        '13: Climate Action', '14: Life Below Water', '15: Life on Land', '16: Peace, Justice, and Strong Institutions','17: Partnerships for the Goals'],
       ['1: No Poverty','17: Partnerships for the Goals'])



# Sidebar
st.sidebar.title("Help")