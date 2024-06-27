import streamlit as st

# Title
st.title("🩵 Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Section 1: Content Curation
st.subheader("Step1: Content Curation")
st.write("Customize your content with the help of AI.")
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
    st.write(
        '''
        Eradicating extreme poverty for all people everywhere by 2030 is a pivotal goal of the 2030 Agenda for Sustainable Development. 
        Extreme poverty, defined as surviving on less than $2.15 per person per day at 2017 purchasing power parity, has witnessed remarkable declines over recent decades. 
        
        However, the emergence of COVID-19 marked a turning point, reversing these gains as the number of individuals living in extreme poverty increased for the first time in a generation by almost 90 million over previous predictions.
        '''
    )


# Sidebar
st.sidebar.title("Help")