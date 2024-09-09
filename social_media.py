import streamlit as st
import re
from services.prompts import create_social_media_post
from app import pexels_api 
from services.functions import extract_generated_content, extract_image_captions
import google.generativeai as genai

def generate_social_media_post():
    model = genai.GenerativeModel('gemini-1.5-pro')

    # Process each selected platform
    for platform in st.session_state.platforms:
        # Check if the platform is already in the generated response dictionary
        if platform not in st.session_state.generated_response:
            st.session_state.generated_response[platform] = {}

        # Use the specified character limit
        character_limit = st.session_state.char_limit

        # Generate prompt and store prompt length
        prompt = create_social_media_post(platform, character_limit, st.session_state.topic, st.session_state.keyword, st.session_state.company_name, st.session_state.hashtags)
        st.session_state.generated_response[platform]['prompt_char_count'] = len(prompt)

        # Generate content using the model instance and store the response object
        response = model.generate_content(prompt)
        st.session_state.generated_response[platform]['response'] = response

        # Store the input and output token counts
        st.session_state.generated_response[platform]['input_tokens'] = response.usage_metadata.prompt_token_count
        st.session_state.generated_response[platform]['output_tokens'] = response.usage_metadata.candidates_token_count

        display_results(platform)

def display_results(platform):
    platform_dic = st.session_state.generated_response[platform]
    response_obj = platform_dic['response']
    generated_result = response_obj.text
    st.session_state.generated_text = extract_generated_content(response_obj.text)
    st.session_state.image_captions = extract_image_captions(response_obj.text)

    # Insert image links into the generated content
    pattern = r'\[Image \d+: .*?\]'
    parts = re.split(pattern, generated_result)
    placeholders = re.findall(pattern, generated_result)

    for image_caption in st.session_state.image_captions:
        try:
            image_result = pexels_api.search_image(image_caption, 1)[0]
            st.session_state.image_mapping[image_caption] = image_result
        except Exception as e:
            st.error(f"An error occurred while fetching images: {e}")

    st.markdown(f"### Generated Result for {platform}:")
    for i, part in enumerate(parts):
        st.write(part)
        if i < len(placeholders):
            placeholder = placeholders[i]
            description = placeholder[1:-1]  # Remove the square brackets
            image_url = st.session_state.image_mapping.get(description)
            if image_url:
                st.image(image_url, caption=description, use_column_width=True)

    # Display character counts and cost projection
    st.markdown("###Gemini Cost projection per Post")
    st.write(f"Prompt Character Count: {platform_dic['prompt_char_count']}")
    st.write(f"Generated Content Character Count: {len(st.session_state.generated_text)}")
    # Define pricing for tokens
    input_token_rate = 0.000035  # Cost per input token
    output_token_rate = 0.000105  # Cost per output token

    # Calculate the estimated cost based on input and output tokens
    token_cost = (
        platform_dic['input_tokens'] * input_token_rate +
        platform_dic['output_tokens'] * output_token_rate
    )
    st.write(f"Estimated cost: ${token_cost:.6f}")