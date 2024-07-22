import os
import streamlit as st
import services.prompts as prompts
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

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
       ['1: No Poverty','17: Partnerships for the Goals'], max_selections=2)

# Initial Keywords
input_draft = st.text_area("Enter your keywords (seperate with commas):")

st.divider()
# Content Type
st.write("Select your Content Type:")

col1, col2, col3 = st.columns(3)

with col1:
   facebook = st.checkbox('Facebook Post')
   medium = st.checkbox('Medium Article')

with col2:
   instagram = st.checkbox('Instagram Post')
   tweet = st.checkbox('Tweet')

with col3:
   linkedin = st.checkbox('LinkedIn Post')
   all = st.checkbox('All')

# content_type = st.selectbox(
#         'Select your content type: ',
#         ('LinkedIn Post','Facebook Post','Instagram Post','Medium Article','Tweet','Blog', 'Newsletter','Short Videos (TikTok, Reels)'),
#         index=0)


# Generate Button
button_generate = st.button("Generate")

# Mimic Generate Button Logic/Put Gemini logic here
if button_generate:
    st.write(
        '''
        Eradicating extreme poverty for all people everywhere by 2030 is a pivotal goal of the 2030 Agenda for Sustainable Development. 
        Extreme poverty, defined as surviving on less than $2.15 per person per day at 2017 purchasing power parity, has witnessed remarkable declines over recent decades. 
        
        However, the emergence of COVID-19 marked a turning point, reversing these gains as the number of individuals living in extreme poverty increased for the first time in a generation by almost 90 million over previous predictions.
        '''
    )

# original OpenAI API logic
# if button_generate:
#     if content_type == 'Blog':
#         blog_prompt = prompts.generate_blog_prompt(topics, input_draft)
#         generated_response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": prompts.general_prompt()},
#                 {"role": "user", "content": prompts.generate_blog_prompt(topics, input_draft)},
#             ]
#         )
#         st.write(generated_response.choices[0].message.content)
#     else:
#         st.write("Content type not supported yet.")


# Sidebar for guidance
st.sidebar.title("Need Help?")
st.sidebar.caption("Tips for using the tool.")
st.sidebar.markdown("""
## Step 1. Content Curation
This section allows you to customize your content with the help of AI.
   - Select the SDG topics you want to write for. You can select multiple topics.
   - Select your content type based on the target plaftorm needs.
   - Enter your initial draft in the text area.
   - Click the 'Generate' button to generate the content.
   - After you're satisfied with the content, click the 'Save' button to save your work.
   - You can also export your content by clicking the 'Export' button.
""")