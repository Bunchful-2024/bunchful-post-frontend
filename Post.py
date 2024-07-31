import json
import os
import requests
import streamlit as st
from services.prompts import general_prompt  
from services.functions import extract_generated_content, transform_to_markdown
import google.generativeai as genai
from dotenv import load_dotenv

# Load and set up environment variables
load_dotenv()
genai.configure(api_key="AIzaSyA_c1yyDqScWbXBl2TYc6dj-IC54HqrWOo") #os not working so change to this temporarily
model = genai.GenerativeModel('gemini-1.5-pro')

# Access environment variables
fb_page_id = os.environ.get('FB_PAGE_ID')
fb_access_token = os.environ.get('FB_PAGE_ACCESS_TOKEN')
fb_access_token = str(fb_access_token)

# Set up initial session state
if 'content_type' not in st.session_state:
    st.session_state.content_type = ""
if 'platforms' not in st.session_state:
    st.session_state.platforms = []
if 'generate_all' not in st.session_state:
    st.session_state.generate_all = False
if 'keyword' not in st.session_state:
    st.session_state.keyword = ""
if 'topic' not in st.session_state:
    st.session_state.topic = ""
if 'char_limit' not in st.session_state:
    st.session_state.char_limit = 1500
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ""
if 'formatted_text' not in st.session_state:
    st.session_state.formatted_text = ""

# Title
st.title("🙌 Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Step 1: Enter Topic
st.markdown("#### Step 1: Enter Topic")
st.session_state.topic = st.text_input("Enter your topic here:")

# Step 2: Enter Keywords
st.markdown("#### Step 2: Enter Keywords")
st.session_state.keyword = st.text_input("Enter your keywords here:")

# Step 3: Select Content Type
st.markdown("#### Step 3: Select Content Type")
content_choices = ["Social Media Post", "Video Scripts", "Articles", "Blogs", "Ads", "Case Study", "Press Release", 
                "Emails - Promotional", "Emails - Cold", "Emails - Outbounds", "Emails - Warm", "Newsletters", "Welcome", "SMS Messages", "Job Posts"]
st.session_state.content_type = st.selectbox("Select your content type:", content_choices, index=0)

# Step 4: Select Platform
# dictionary to map content types to platforms
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

# Platform character limits (for default values if range is not specified)
platform_character_limits = {
    'LinkedIn': 2000,
    'Facebook': 1500,
    'Instagram': 1300,
    'X (Twitter)': 280,
    'Instagram Threads': 500,
    'Medium': 1500,
    'Hub Pages':1500,
    'Vocal Media':1500,
    'NewsBreak':700,
    'Steemit':800,
    'Substack':1200,
    'Ghost':1500,
    'Write.as':800
}

# Function to get the default character limit for the selected platforms
def get_default_char_limit(platforms):
    if not platforms:
        return 1500
    return min([platform_character_limits.get(platform, 1500) for platform in platforms])

# Update the character limit based on selected platforms
if st.session_state.platforms:
    st.session_state.char_limit = get_default_char_limit(st.session_state.platforms)

# Single slider for character limit
char_limit = st.slider("Select Character Limit", min_value=100, max_value=3000, value=st.session_state.char_limit)

# Generate button
generate_button = st.button("Generate")

# Mimic Generate Button Logic/Put Gemini logic here
if generate_button:
    try:
        # Process each selected platform
        for platform in st.session_state.platforms:
            # Use the specified character limit if it falls within the platform's default range
            default_limit = platform_character_limits.get(platform, 1500)
            character_limit = min(default_limit, char_limit)

            # Generate prompt based on the platform and character limit
            prompt = general_prompt(platform, character_limit, st.session_state.topic, st.session_state.keyword)

            # Calculate estimated token count
            prompt_tokens = len(prompt.split())
            prompt_char_count = len(prompt)

            # Generate content using the model instance
            response = model.generate_content(prompt)

            # Accessing the content from the response object
            generated_result = response.text
            st.session_state.generated_text = extract_generated_content(response.text)
            #print(generated_result) #for testing
            generated_char_count = len(st.session_state.generated_text)
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

            st.markdown("### Edit Section")
            st.text_area("Prompt", value=st.session_state.generated_text, height=200)

            st.session_state.formatted_text = transform_to_markdown(st.session_state.generated_text)

    except AttributeError as e:
        st.error(f"An attribute error occurred: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if st.session_state.generated_text:
    if st.session_state.platforms == ['Facebook']:
        st.subheader("Step 2: Publish to Facebook")
        publish_button = st.button("Publish")
        #publish content to FB page
        if publish_button:
            # Facebook API endpoint for posting to a page
            fb_api_url = f'https://graph.facebook.com/v20.0/{fb_page_id}/feed'

            payload = {
                'message': st.session_state.generated_text,
                'access_token': "EAAHJqTXE0P4BO5tfCZCEMNJoV9zUHdZCZBN2OE2qtW73dTwL5hNlIrH4w0rLUl7jq4DK7dbAlx7kOfeJRGetUgZAJz6Gzja66g3YsNQe2b1gG9YQ1cZBtqFvvGZBsfUZCd1RnbwwuRSZC1ZC5ZCjLu7uAIhgAdlCl5ZA85R2PmXqHp1WViescdTEGaH5IoeZAhSBaMcJ0G5HlXy1S6xClwtryhx3IALTtfJQLpwDy8xZCa1cZD",
                # 'access_token': fb_access_token cannot work why
            }
            headers = {
                'Content-Type': 'application/json'
            }

            # Debugging: Use st.write to display the payload and URL
            st.write("Facebook API URL:", fb_api_url)
            st.write("Payload:", payload)
            st.write("Headers:", headers)

            response = requests.post(fb_api_url, headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                st.success("Post published successfully on Facebook!")
            else:
                st.error(f"Failed to publish post: {response.text}")

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