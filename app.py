import json
import requests
import streamlit as st
import services.image_service
from services.functions import transform_to_markdown, extract_title
import google.generativeai as genai

# Initialize session state variables
session_keys = [
    'content_type', 'platforms', 'generate_all', 'keyword', 'topic', 'company_name', 'hashtags',
    'char_limit', 'generated_text', 'formatted_text', 'edited_text',
    'image_captions', 'image_mapping', 'parts', 'placeholders',
    'generated_response', 'medium_token', 'gemini_api_key'
]

for key in session_keys:
    if key not in st.session_state:
        if key in ['platforms', 'image_captions', 'parts', 'placeholders']:
            st.session_state[key] = []
        elif key == 'image_mapping':
            st.session_state[key] = {}
        elif key == 'generated_response':
            st.session_state[key] = {}
        elif key in ['char_limit']:
            st.session_state[key] = 1500
        else:
            st.session_state[key] = ""

# Configure generative AI model
genai.configure(api_key=st.session_state.gemini_api_key)
model = genai.GenerativeModel('gemini-1.5-pro')

# Initialize Pexels API
pexels_api = services.image_service.PexelsAPI(st.secrets["PEXELS_API_KEY"])

# Title
st.title("🙌 Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Step 1: Enter Topic
st.markdown("#### Step 1: Enter Topic")
st.session_state.topic = st.text_area("What are you writing today?", height=150, key='text_area_topic')

# Step 2: Enter Keywords
st.markdown("#### Step 2: Enter Keywords")
st.session_state.keyword = st.text_input("Enter your keywords here:", key="keywords_text_input")

# Step 2: Enter Company Name
st.markdown("#### Step 2: Enter Company Name")
st.session_state.company_name = st.text_input("Enter your Company Name:", key="company_name_text_input")

# Step 2: Enter Hashtags
st.markdown("#### Step 2: Enter Hashtags")
st.session_state.hashtags = st.text_input("Enter your hashtags:", key="hashtags_text_input")

# Step 3: Select Content Type
st.markdown("#### Step 3: Select Content Type")
content_choices = ["Social Media Post", "Video Scripts", "Articles", "Blogs", "Ads", "Case Study", "Press Release", 
                "Emails - Promotional", "Emails - Cold", "Emails - Outbounds", "Emails - Warm", "Newsletters", "Welcome", "SMS Messages", "Job Posts"]
st.session_state.content_type = st.selectbox("Select your content type:", content_choices, key="content_type_selectbox")

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
st.session_state.generate_all = st.checkbox("Generate for all platforms", value=False, key="generate_all_checkbox")
st.session_state.platforms = st.multiselect("Select your platform:", content_to_platform[st.session_state.content_type], disabled=st.session_state.generate_all, key="platforms_multiselect")

# Platform character limits (for default values if range is not specified)
platform_character_limits = {
    'LinkedIn': 2000,
    'Facebook': 1500,
    'Instagram': 1300,
    'X (Twitter)': 280,
    'Instagram Threads': 500,
    'Medium': 1500,
    'Hub Pages': 1500,
    'Vocal Media': 1500,
    'NewsBreak': 700,
    'Steemit': 800,
    'Substack': 1200,
    'Ghost': 1500,
    'Write.as': 800,
    'Pinterest': 500,
    'YouTube': 5000,
    'TikTok': 1500,
    'Threads': 500,
    'Idealist': 1600
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
char_limit = st.slider("Select Character Limit", min_value=100, max_value=3000, value=st.session_state.char_limit, key="char_limit_slider")

# Generate button
generate_button = st.button("Generate", key="generate_button")

if generate_button:
    if not st.session_state.gemini_api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    else:
        try:
            # Process based on content type
            if st.session_state.content_type == "Articles":
                from articles import generate_article
                generate_article()
            elif st.session_state.content_type == "Social Media Post":
                from social_media import generate_social_media_post
                generate_social_media_post()

        except Exception as e:
            st.error(f"An error occurred: {e}")

def get_author_id(medium_token):
    headers = {
        'Authorization': f"Bearer {medium_token}",
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.get("https://api.medium.com/v1/me", headers=headers)
    if response.status_code != 200:
        st.error(f"Failed to retrieve Medium user data: {response.text}")
        return None
    return response.json()['data']['id']

def publish_to_medium(medium_token, content):
    author_id = get_author_id(medium_token)
    if not author_id:
        return

    medium_url = f"https://api.medium.com/v1/users/{author_id}/posts"
    payload = json.dumps({
        "title": extract_title(content),
        "contentFormat": "markdown",
        "content": content,
        "publishStatus": "public"
    })
    headers = {
        'Authorization': f"Bearer {medium_token}",
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.post(medium_url, headers=headers, data=payload)
    if response.status_code == 201:
        st.success("Post published successfully on Medium!")
    else:
        st.error(f"Failed to publish post: {response.text}")

# Display the generated text and allow editing
if st.session_state.generated_text:
    st.markdown("### Edit Section")
    st.write("Make sure to edit your content to prevent complete duplication by AI. If you are modifying the image placement, please ensure you copy the whole image info in the format [Image X: Caption].")
    st.session_state.formatted_text = transform_to_markdown(st.session_state.generated_text)
    st.session_state.edited_text = st.text_area("Edit your content:", value=st.session_state.generated_text, height=500, key='edit_text_area_generated')

    if 'Medium' in st.session_state.platforms:
        publish_button = st.button("Publish to Medium", key="publish_to_medium_button")
        if publish_button:
            if not st.session_state.medium_token:
                st.error("Please enter your Medium Access Token in the sidebar.")
            else:
                publish_to_medium(st.session_state.medium_token, st.session_state.edited_text)

# Sidebar for guidance
st.sidebar.title("Set up")
st.session_state.gemini_api_key = st.sidebar.text_input("Enter your Gemini API Key", key='gemini_api_key_input')
st.session_state.medium_token = st.sidebar.text_input("Enter your Medium Token", key='medium_token_input')
