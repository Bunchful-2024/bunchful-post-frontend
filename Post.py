import os
import streamlit as st
from services.prompts import general_prompt  
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro')

# Title
st.title("🩵 Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Section 1: Content Curation
st.subheader("Step 1: Content Curation")
st.write("Customize your content with the help of AI.")

# SDGs Topic Select
platforms = st.multiselect(
    "Select your topic:",
    ['LinkedIn', 'Instagram', 'Facebook', 'X', 'Instagram Thread']
)

# Text area for entering the topic/keyword
topic = st.text_area("Enter your Topic/Keyword")

#Generate button
generate_button = st.button("Generate")

# Generate button
if generate_button:
    try:
        # Join the selected platforms into a single string
        platforms_str = ", ".join(platforms)

        # Retrieve the predefined prompt and replace placeholders
        prompt_template = general_prompt()
        prompt = prompt_template.format(
            platform=platforms_str,
            Topic=topic,
            LinkedIn_Character_Limit=2000,
            Facebook_Character_Limit=1500,
            Instagram_Character_Limit=1300,
            Twitter_Character_Limit=280,
            Threads_Character_Limit=280
        )

        # Calculate estimated token count (assuming split on whitespace)
        prompt_tokens = len(prompt.split())

        # Calculate character count for prompt
        prompt_char_count = len(prompt)

        # Generate content using the model instance
        response = model.generate_content(prompt)

        # Print the response to understand its structure
        st.write("Response object:", response)

        # Accessing the content from the response object
        generated_text = response.text
        st.write("Generated Content:")
        st.write(generated_text)

        # Calculate character count for generated content
        generated_char_count = len(generated_text)

        # Display estimated token count, estimated cost, and character counts
        st.markdown("### Writer AI Cost projection per article")
        st.write(f"Prompt Character Count: {prompt_char_count}")
        st.write(f"Generated Content Character Count: {generated_char_count}")
        input_tokens = response.usage_metadata.prompt_token_count
        output_tokens = response.usage_metadata.candidates_token_count
        st.write(f"Input tokens: {input_tokens}") #input token count
        st.write(f"Output tokens: {output_tokens}") #output token count
        # Input per token price: 7.50/1,000,000 = 0.0000075 per token
        # Output per token price: 22.50/1,000,000=0.0000225 per token
        token_cost = input_tokens*0.0000075+output_tokens*0.0000225
        st.write(f"Estimated cost: {token_cost}") 
        
    except AttributeError as e:
        st.error(f"An attribute error occurred: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Sidebar for guidance
st.sidebar.title("Need Help?")
st.sidebar.caption("Tips for using the tool.")
st.sidebar.markdown("""
## Step 1. Content Curation
This section allows you to customize your content with the help of AI.
  - Select the Platform you want to write for. You can select multiple topics.
  - Enter your Topic in the text area.
  - Click the 'Generate' button to generate the content.
""")
