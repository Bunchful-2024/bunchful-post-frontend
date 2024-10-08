import json
import requests
import streamlit as st

from services.content_generation import generate_article,generate_social_media_post, generate_newsletter_content, generate_listicle, display_social_media_post_results, display_results_with_image_option
from services.functions import transform_to_markdown, extract_title
from platforms.facebook import FacebookAPI

import google.generativeai as genai

# Initialize session state variables
session_keys = [
    'content_type', 'platforms', 'generate_all', 'keyword', 'topic', 'company_name', 'hashtags',
    'char_limit', 'generated_text', 'formatted_text', 'edited_text',
    'image_captions', 'image_mapping', 'image_selected', 'parts', 'placeholders',
    'generated_response', 'medium_token', 'gemini_api_key'
]

for key in session_keys:
    if key not in st.session_state:
        if key in ['platforms', 'image_captions', 'parts', 'placeholders']:
            st.session_state[key] = []
        elif key == 'image_mapping':
            st.session_state[key] = {}
        elif key == 'image_selected':
            st.session_state[key] = {}
        elif key == 'generated_response':
            st.session_state[key] = {}
        elif key in ['char_limit']:
            st.session_state[key] = 1500
        else:
            st.session_state[key] = ""

if st.session_state.gemini_api_key:
    genai.configure(api_key=st.session_state.gemini_api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
else:
    st.warning("Please enter your Gemini API Key in the sidebar.")

# Title
st.title("🙌 Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Step 1: Enter Topic
st.markdown("#### Step 1: Enter Topic")
st.session_state.topic = st.text_area("What are you writing today?")

# Step 2: Enter Keywords
st.markdown("#### Step 2: Enter Keywords")
st.session_state.keyword = st.text_input("Enter your keywords here:")

# Step 3: Enter Company Name
st.markdown("#### Step 3: Enter Company Name")
st.session_state.company_name = st.text_input("Enter your Company Name:")

# Step 4: Enter Hashtags
st.markdown("#### Step 4: Enter Hashtags")
st.session_state.hashtags = st.text_input("Enter your hashtags:")

# Step 5: Select Content Type
st.markdown("#### Step 5: Select Content Type")
content_choices = ["Social Media Post", "Video Scripts", "Articles", "Blogs", "Listicles", "Ads", "Case Study", "Press Release", 
                "Emails - Promotional", "Emails - Cold", "Emails - Outbounds", "Emails - Warm", "Newsletters", "Welcome", "SMS Messages", "Job Posts"]
st.session_state.content_type = st.selectbox("Select your content type:", content_choices, index=0)

# Step 6: Select Platform
# dictionary to map content types to platforms
content_to_platform = {
    "Social Media Post": ["LinkedIn", "Facebook", "Instagram", "X (Twitter)", "Pinterest", "Youtube", "TikTok", "Threads"],
    "Video Scripts": ["Website", "Facebook", "Instagram", "YouTube", "TikTok", "Threads"],
    "Articles": ["Website", "Reddit", "Medium", "Hub Pages", "Vocal Media", "NewsBreak", "Steemit", "Ghost", "Write.as"],
    "Blogs": ["Website", "Tumblr"],
    "Listicles": ["Website", "Reddit", "Medium", "Hub Pages", "Vocal Media", "NewsBreak", "Steemit", "Ghost", "Write.as"],
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

st.markdown("#### Step 6: Select Platform")
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

# Generate content logic
if generate_button:
    if not st.session_state.gemini_api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    else:
        genai.configure(api_key=st.session_state.gemini_api_key)
        try:
            if st.session_state.content_type == "Articles":
                generate_article()                
            elif st.session_state.content_type == "Social Media Post":
                generate_social_media_post()
            elif st.session_state.content_type == "Newsletters":
                generate_newsletter_content()
            elif st.session_state.content_type == "Listicles":
                generate_listicle()
            else:
                st.error("Unsupported content type selected.")
        except AttributeError as e:
            st.error(f"An attribute error occurred: {e}")
        except TypeError as e:
            st.error(f"A type error occurred: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display the generated text
if st.session_state.generated_response:
    if st.session_state.content_type == "Social Media Post":
        for platform in st.session_state.platforms:
            display_social_media_post_results(platform)
    else:
        for platform in st.session_state.platforms:
            display_results_with_image_option(platform)


#Editing Section
if st.session_state.generated_response:

    st.markdown("### Edit Section")
    st.write("If you are modifying the image placment, please ensure you copy the whole image info in the format [Image X: Caption].")
    if st.session_state.content_type == "Social Media Post":
        st.session_state.edited_text = st.text_area("Edit your content:", value=st.session_state.generated_text, height=500)
    else:
        st.session_state.formatted_text = transform_to_markdown(st.session_state.generated_text)
        st.session_state.edited_text = st.text_area("Edit your content:", value=st.session_state.generated_text, height=500)

    print(st.session_state.formatted_text) #for testing

    if st.session_state.platforms == ['Medium']:
        publish_button = st.button("Publish")
        #publish content to Medium
        if publish_button:
            if not st.session_state.medium_token:
                st.error("Please enter your Medium Access Token in the sidebar.")
            else:
                # transform the final text into markdown format
                st.session_state.formatted_text = transform_to_markdown(st.session_state.edited_text)
                # get Medium author ID
                payload = {}
                headers = {
                    'Host': 'api.medium.com',
                    'Authorization': f"Bearer {st.session_state.medium_token}",
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                }

                response = requests.request("GET", "https://api.medium.com/v1/me", headers=headers, data=payload)
                response.raise_for_status()
                author_id = response.json()['data']['id']

                # Medium API endpoint for posting
                medium_url = f"https://api.medium.com/v1/users/{author_id}/posts"

                payload = json.dumps({
                    "title": extract_title(st.session_state.formatted_text),
                    "contentFormat": "markdown",
                    "content": st.session_state.formatted_text,
                    "publishStatus": "public"
                })

                headers = {
                    'Host': 'api.medium.com',
                    'Authorization': f"Bearer {st.session_state.medium_token}",
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Accept-Charset': 'utf-8',
                }

                response = requests.post(medium_url, headers=headers, data=payload)

                if response.status_code == 201:
                    st.success("Post published successfully on Medium!")
                else:
                    st.error(f"Failed to publish post: {response.text}")

    elif st.session_state.platforms == ['Facebook']:
        publish_button = st.button("Publish")
        FacebookAPI = FacebookAPI(st.secrets["FACEBOOK_PAGE_ID"], st.secrets["FACEBOOK_PAGE_ACCESS_TOKEN"])
        #publish content to FB page
        if publish_button:
            # Facebook API endpoint for posting to a page
            #FacebookAPI.publish_post(st.session_state.edited_text)
            FacebookAPI.publish_post(st.session_state.edited_text,st.session_state.image_mapping.get(st.session_state.image_captions))



# Sidebar for guidance
st.sidebar.title("Login Section")
user = st.sidebar.radio(
    "Select your user type:",
    ["Bunchful", "Visitor"],
)
if user == "Visitor":
    st.session_state.gemini_api_key = st.sidebar.text_input("Enter your Gemini API Key")
    st.session_state.medium_token = st.sidebar.text_input("Enter your Medium Token")
elif user == "Bunchful":
    # Password input field
    password = st.sidebar.text_input("Enter your password", type="password")
    if password == st.secrets["BUNCHFUL_PASSWORD"]:
        st.session_state.gemini_api_key = st.secrets["BUNCHFUL_GEMINI_API_KEY"]
        st.session_state.medium_token = st.secrets["BUNCHFUL_MEDIUM_TOKEN"]
        st.sidebar.success("User authenticated")
    else:
        st.sidebar.error("Incorrect password")

# Debug: Check if image captions are available
# if st.session_state.image_captions:
#     st.markdown("#### Image Section")
#     for image_caption in st.session_state.image_captions:
#         try:
#             # Debug: Log the image caption being processed
#             image_result = pexels_api.search_image(image_caption, 1)[0]
#             st.image(image_result, caption=image_caption, use_column_width=True)
#         except Exception as e:
#             st.error(f"An error occurred while fetching images: {e}")
