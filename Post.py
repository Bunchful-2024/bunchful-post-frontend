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
    if content_type == 'Blog':
        blog_prompt = prompts.generate_blog_prompt(topics, input_draft)
        generated_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompts.general_prompt()},
                {"role": "user", "content": prompts.generate_blog_prompt(topics, input_draft)},
            ]
        )
        st.write(generated_response.choices[0].message.content)
    else:
        st.write("Content type not supported yet.")


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