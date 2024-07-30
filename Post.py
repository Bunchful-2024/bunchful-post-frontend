import os
import streamlit as st
from services.prompts import general_prompt  
from services.functions import extract_generated_content
import google.generativeai as genai
from dotenv import load_dotenv

# Load and set up environment variables
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

# Set up initial session state
if 'content_type' not in st.session_state:
    st.session_state.content_type = ""
if 'platforms' not in st.session_state:
    st.session_state.platforms = []
if 'generate_all' not in st.session_state:
    st.session_state.generate_all = False

# Title
st.title("🙌 Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Step 1: Enter Topic
st.markdown("#### Step 1: Enter Topic")
topic = st.text_input("Enter your topic here:")

# Step 2: Enter Keywords
st.markdown("#### Step 2: Enter Keywords")
topic = st.text_input("Enter your keywords here:")

# Step 3: Select Content Type
st.markdown("#### Step 3: Select Content Type")
content_choices = ["Social Media Post", "Video Scripts", "Articles", "Blogs", "Ads", "Case Study", "Press Release", 
                "Emails - Promotional", "Emails - Cold", "Emails - Outbounds", "Emails - Warm", "Newsletters", "Welcome", "SMS Messages", "Job Posts"]
st.session_state.content_type = st.selectbox("Select your content type:", content_choices, index=1)

# Step 4: Select Platform
content_to_platform = {
    "Social Media Post": ["LinkedIn", "Facebook", "Instagram", "X (Twitter)", "Pinterest", "Youtube", "TikTok", "Threads"],
    "Video Scripts": ["Website", "Facebook", "Instagram", "YouTube", "TikTok", "Threads"],
    "Articles": ["Website", "Reddit", "Medium", "Hub Pages", "Vocal Media", "NewsBreak", "Steemit", "Ghost", "Write.as"],
    "Blogs": ["Website", "Tumblr"],
    "Ads": ["Website", "Amazon", "Bing", "Google", "LinkedIn", "Facebook", "Instagram", "X (Twitter)", "Pinterest", "YouTube", "TikTok", "Threads"],
    "Case Study": [],
    "Press Release": [],
    "Emails - Promotional": [],
    "Emails - Cold": [],
    "Emails - Outbounds": [],
    "Emails - Warm": [],
    "Newsletters": [],
    "Welcome": [],
    "SMS Messages": ["Idealist"],
    "Job Posts": []
}

st.markdown("#### Step 4: Select Platform")
st.session_state.generate_all = st.checkbox("Generate for all platforms", value=False)
st.session_state.platforms = st.multiselect("Select your platform:", content_to_platform[st.session_state.content_type], disabled=st.session_state.generate_all)


# Range for character limits
min_char_limit = st.slider("Minimum Character Limit", min_value=100, max_value=2000, value=280)
max_char_limit = st.slider("Maximum Character Limit", min_value=100, max_value=2000, value=1000)

# Generate button
generate_button = st.button("Generate")

# Platform character limits (for default values if range is not specified)
platform_character_limits = {
    'LinkedIn': 2000,
    'Facebook': 1500,
    'Instagram': 1300,
    'X (Twitter)': 280,
    'Instagram Threads': 500,
    'Medium': 2000,
}

# Generate content on button click
if generate_button:
    try:
        # Process each selected platform
        for platform in st.session_state.platforms:
            # Use platform default limit if it falls within the user-specified range
            character_limit = min(max_char_limit, platform_character_limits.get(platform, 500))
            character_limit = max(min_char_limit, character_limit)

            # Generate prompt based on the platform and character limit
            prompt = general_prompt(platform, character_limit)
            prompt = prompt.format(Topic=topic)

            # Calculate estimated token count
            prompt_tokens = len(prompt.split())
            prompt_char_count = len(prompt)

            # Generate content using the model instance
            response = model.generate_content(prompt)

            # Accessing the content from the response object
            generated_result = response.text
            generated_text = extract_generated_content(response.text)
            generated_char_count = len(generated_text)
            input_tokens = response.usage_metadata.prompt_token_count
            output_tokens = response.usage_metadata.candidates_token_count
            
            # Display results
            st.markdown(f"### Generated Result for {platform}:")
            st.write(generated_result)

            # Display character counts and cost projection
            st.markdown("### Writer AI Cost projection per article")
            st.write(f"Prompt Character Count: {prompt_char_count}")
            st.write(f"Generated Content Character Count: {generated_char_count}")
            st.write(f"Input tokens: {input_tokens}")  # Input token count
            st.write(f"Output tokens: {output_tokens}")  # Output token count
            token_cost = input_tokens * 0.0000075 + output_tokens * 0.0000225
            st.write(f"Estimated cost: ${token_cost:.6f}")

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
