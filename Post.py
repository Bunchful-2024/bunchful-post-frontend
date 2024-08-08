import json
import requests
import streamlit as st
import re
import services.image_service
from services.prompts import general_prompt  
from services.functions import extract_generated_content, transform_to_markdown, extract_title, extract_image_captions
import google.generativeai as genai

# Load and set up environment variables
genai.configure(api_key=st.secrets["GEMINI_API_KEY"]) 
model = genai.GenerativeModel('gemini-1.5-pro')
pexels_api = services.image_service.PexelsAPI(st.secrets["PEXELS_API_KEY"])

# # Access environment variables
# fb_page_id = os.environ.get('FB_PAGE_ID')
# fb_access_token = os.environ.get('FB_PAGE_ACCESS_TOKEN')
# fb_access_token = str(fb_access_token)

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
if 'edited_text' not in st.session_state:
    st.session_state.edited_text = ""
if 'image_captions' not in st.session_state:
    st.session_state.image_captions = []
if 'image_mapping' not in st.session_state:
    st.session_state.image_mapping = {}
if 'parts' not in st.session_state:
    st.session_state.parts = []
if 'placeholders' not in st.session_state:
    st.session_state.placeholders = []
# the dictionary to store the generated response
# format {Medium: {prompt_char_count: 100, generated_char_count: 200, input_tokens: 100, output_tokens: 200}} 
if 'generated_response' not in st.session_state:
    st.session_state.generated_response = {}

# Title
st.title("🙌 Bunchful Post")
st.caption("Welcome to Bunchful Post! Manage your content here.")

# Step 1: Enter Topic
st.markdown("#### Step 1: Enter Topic")
st.session_state.topic = st.text_area("What are you writing today?")

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
# Have to fix the disappearing generated text issue
if generate_button:
    try:
        # Process each selected platform
        for platform in st.session_state.platforms:
            # check if the platform is already in the generated response dictionary
            if platform not in st.session_state.generated_response:
                st.session_state.generated_response[platform] = {}
            # Use the specified character limit if it falls within the platform's default range
            default_limit = platform_character_limits.get(platform, 1500)
            character_limit = min(default_limit, char_limit)

            # Generate prompt based on the platform and character limit and store prompt length (characters count)
            prompt = general_prompt(platform, character_limit, st.session_state.topic, st.session_state.keyword)
            st.session_state.generated_response[platform]['prompt_char_count'] = len(prompt)

            # Generate content using the model instance and store the response object
            response = model.generate_content(prompt)
            st.session_state.generated_response[platform]['response'] = response

            # Store the input and output token counts with Gemini methods
            st.session_state.generated_response[platform]['input_tokens'] = response.usage_metadata.prompt_token_count
            st.session_state.generated_response[platform]['output_tokens'] = response.usage_metadata.candidates_token_count
            
    except AttributeError as e:
        st.error(f"An attribute error occurred: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display results
if st.session_state.generated_response:
    for platform in st.session_state.platforms:
        platform_dic = st.session_state.generated_response[platform]
        response_obj = platform_dic['response']
        # Accessing the content from the response object
        generated_result = response_obj.text
        st.session_state.generated_text = extract_generated_content(response_obj.text)
        st.session_state.image_captions = extract_image_captions(response_obj.text)
        print(generated_result) #for testing

        # Insert image links to the generated content
        # Adjust the regular expression to match the placeholders
        pattern = r'\[Image \d+: .*?\]'

        # Split the content by the placeholders
        parts = re.split(pattern, generated_result)

        # Find all placeholders
        placeholders = re.findall(pattern, generated_result)
        count = 0
        for image_caption in st.session_state.image_captions:
            try:
                # Debug: Log the image caption being processed
                image_result = pexels_api.search_image(image_caption, 1)[0]
                print(image_result) #for testing
                st.session_state.image_mapping[image_caption] = image_result
                count+=1
            except Exception as e:
                st.error(f"An error occurred while fetching images: {e}")

        st.markdown(f"### Generated Result for {platform}:")
        # st.write(generated_result)
        # Iterate over the parts and display text and images
        for i, part in enumerate(parts):
            st.write(part)
            if i < len(placeholders):
                placeholder = placeholders[i]
                description = placeholder[1:-1]  # Remove the square brackets
                image_url = st.session_state.image_mapping.get(description)
                if image_url:
                    st.image(image_url, caption=description, use_column_width=True)

        # Display character counts and cost projection
        st.markdown("### Writer AI Cost projection per article")
        st.write(f"Prompt Character Count: {platform_dic['prompt_char_count']}")
        st.write(f"Generated Content Character Count: {len(st.session_state.generated_text)}")
        st.write(f"Input tokens: {platform_dic['input_tokens']}")  # Input token count
        st.write(f"Output tokens: {platform_dic['output_tokens']}")  # Output token count
        token_cost = platform_dic['input_tokens'] * 0.0000075 + platform_dic['output_tokens'] * 0.0000225
        st.write(f"Estimated cost: ${token_cost:.6f}")

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

if st.session_state.generated_text:

    st.markdown("### Edit Section")
    st.write("If you are modifying the image placment, please ensure you copy the whole image info in the format [Image X: Caption].")
    st.session_state.formatted_text = transform_to_markdown(st.session_state.generated_text)
    st.session_state.edited_text = st.text_area("Edit your content:", value=st.session_state.generated_text, height=500)
    print(st.session_state.formatted_text) #for testing

    # if st.session_state.platforms == ['Facebook']:
    #     st.subheader("Step 2: Publish to Facebook")
    #     publish_button = st.button("Publish")
    #     #publish content to FB page
    #     if publish_button:
    #         # Facebook API endpoint for posting to a page
    #         fb_api_url = f'https://graph.facebook.com/v20.0/{fb_page_id}/feed'

    #         payload = {
    #             'message': st.session_state.generated_text,
    #             'access_token': "EAAHJqTXE0P4BO5tfCZCEMNJoV9zUHdZCZBN2OE2qtW73dTwL5hNlIrH4w0rLUl7jq4DK7dbAlx7kOfeJRGetUgZAJz6Gzja66g3YsNQe2b1gG9YQ1cZBtqFvvGZBsfUZCd1RnbwwuRSZC1ZC5ZCjLu7uAIhgAdlCl5ZA85R2PmXqHp1WViescdTEGaH5IoeZAhSBaMcJ0G5HlXy1S6xClwtryhx3IALTtfJQLpwDy8xZCa1cZD",
    #             # 'access_token': fb_access_token cannot work why
    #         }
    #         headers = {
    #             'Content-Type': 'application/json'
    #         }

    #         # Debugging: Use st.write to display the payload and URL
    #         st.write("Facebook API URL:", fb_api_url)
    #         st.write("Payload:", payload)
    #         st.write("Headers:", headers)

    #         response = requests.post(fb_api_url, headers=headers, data=json.dumps(payload))

    #         if response.status_code == 200:
    #             st.success("Post published successfully on Facebook!")
    #         else:
    #             st.error(f"Failed to publish post: {response.text}")
    if st.session_state.platforms == ['Medium']:
        publish_button = st.button("Publish")
        #publish content to Medium
        if publish_button:
            #transform the final text into markdown format
            st.session_state.formatted_text = transform_to_markdown(st.session_state.edited_text)
            # Medium API endpoint for posting
            medium_url = f"https://api.medium.com/v1/users/1980e4756f9f99298a88b228cc6990e0bcc38f9e4fc0a970494f646ee62db46fd/posts"

            payload = json.dumps({
                "title": extract_title(st.session_state.formatted_text),
                "contentFormat": "markdown",
                "content": st.session_state.formatted_text,
                "publishStatus": "public"
            })

            headers = {
                'Host': 'api.medium.com',
                'Authorization': 'Bearer 2958656ad24671bca553257e68aac2a094b7bf62ebd268ac0c7c495eba1ea4291',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Accept-Charset': 'utf-8',
            }

            response = requests.post(medium_url, headers=headers, data=payload)

            if response.status_code == 201:
                st.success("Post published successfully on Medium!")
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

