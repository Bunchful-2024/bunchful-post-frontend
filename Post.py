import streamlit as st

# Title
st.title("Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Section 1: Content Curation
st.subheader("Step1: Content Curation")
st.write("Modify your content with the help of AI.")
# SDGs Topic Select 
topics = st.multiselect(
       "Select your topic:",
       ['1: No Poverty', '2: Zero Hunger', '3: Good Health and Well-Being', '4: Quality Education',
        '5: Gender Equality', '6: Clean Water and Sanitation', '7: Affordable and Clean Energy',
        '8: Decent Work and Economic Growth', '9: Industry, Innovation, and Infrastructure',
        '10: Reduced Inequalities', '11: Sustainable Cities and Communities', '12: Responsible Consumption and Production',
        '13: Climate Action', '14: Life Below Water', '15: Life on Land', '16: Peace, Justice, and Strong Institutions','17: Partnerships for the Goals'],
       ['1: No Poverty','17: Partnerships for the Goals'])
# Content Type
content_type = st.selectbox(
        'Select your content type: ',
        ('Blog', 'Newsletter', 'Social Meida Post'),
        index=0)
# Initial Draft
input_draft = st.text_area("Enter your Draft")
# Printing entered text
st.write("""You entered:  \n""",input_draft)
# Generate Button
button_generate = st.button("Generate")
# Mimic Generate Button Logic
if button_generate:
    st.write('You have clicked the Button')


# Sidebar
st.sidebar.title("Help")