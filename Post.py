import os
import streamlit as st
import requests
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

# Text area for entering the topic/keyword
topic = st.text_area("Enter your Topic/Keyword")

st.divider()

# Content Type
st.write("Select your Content Type:")

# simplize for this branch
# col1, col2, col3 = st.columns(3)

# with col1:
#    facebook = st.checkbox('Facebook Post')
#    medium = st.checkbox('LinkedIn Post')

# with col2:
#    instagram = st.checkbox('Instagram Post')
#    tweet = st.checkbox('X (Tweet)')

# with col3:
#    linkedin = st.checkbox('Instagram Threads')
#    all = st.checkbox('All')

# Platfrom select
platforms = st.selectbox(
    "Select your platform:",
    ['LinkedIn', 'Instagram', 'Facebook', 'X', 'Instagram Thread']
)


# Generate Button
button_generate = st.button("Generate")

# Mimic Generate Button Logic/Put Gemini logic here
generated_text = '''
    Eradicating extreme poverty for all people everywhere by 2030 is a pivotal goal of the 2030 Agenda for Sustainable Development. 
    Extreme poverty, defined as surviving on less than $2.15 per person per day at 2017 purchasing power parity, has witnessed remarkable declines over recent decades. 
        
    However, the emergence of COVID-19 marked a turning point, reversing these gains as the number of individuals living in extreme poverty increased for the first time in a generation by almost 90 million over previous predictions.
'''
if button_generate:
    if platforms == 'Facebook':
        st.markdown("#### Facebook Post:")
        st.write(generated_text)

        publish_button = st.button("Publish")

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
- Select the Platform you want to write for. You can select multiple platforms.
- Enter your Topic in the text area.
- Click the 'Generate' button to generate the content.
""")