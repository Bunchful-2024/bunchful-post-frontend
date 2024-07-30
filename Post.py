import os
import streamlit as st
import requests
import json
import google.generativeai as genai
from services.prompts import general_prompt 
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro')

# Access environment variables
fb_page_id = os.environ.get('FB_PAGE_ID')
fb_access_token = os.environ.get('FB_PAGE_ACCESS_TOKEN')
fb_access_token = str(fb_access_token)

# Initialize session state for generated text
if 'generated_text' not in st.session_state:
    st.session_state.generated_text = ''

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

# Platfrom select
platforms = st.multiselect(
    "Select your platform:",
    ['LinkedIn', 'Instagram', 'Facebook', 'X (Twitter)', 'Instagram Thread']
)


# Range for character limits
min_char_limit = st.slider("Minimum Character Limit", min_value=100, max_value=2000, value=280)
max_char_limit = st.slider("Maximum Character Limit", min_value=100, max_value=2000, value=1000)

# Generate button
button_generate = st.button("Generate")

# Platform character limits (for default values if range is not specified)
platform_character_limits = {
    'LinkedIn': 2000,
    'Facebook': 1500,
    'Instagram': 1300,
    'X (Twitter)': 280,
    'Instagram Threads': 500
}

# Mimic Generate Button Logic/Put Gemini logic here
if button_generate:
    try:
        # Process each selected platform
        for platform in platforms:
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
            generated_text = response.text
            generated_char_count = len(generated_text)
            input_tokens = response.usage_metadata.prompt_token_count
            output_tokens = response.usage_metadata.candidates_token_count
            
            # Display results and store generated text in session state
            st.markdown(f"### Generated Content for {platform}:")
            st.write(generated_text)
            st.session_state.generated_text = generated_text

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

if st.session_state.generated_text:
    if platforms == ['Facebook']:
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