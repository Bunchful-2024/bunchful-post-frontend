import re
import streamlit as st
import google.generativeai as genai
from services.prompts import article, social_media_post, newsletter, listicles  # Add listicles import
from services.image_service import PexelsAPI
from services.functions import extract_generated_content, extract_image_captions

pexels_api = PexelsAPI(st.secrets["PEXELS_API_KEY"])

def generate_article():
    model = genai.GenerativeModel('gemini-1.5-pro')
    for platform in st.session_state.platforms:
        if platform not in st.session_state.generated_response:
            st.session_state.generated_response[platform] = {}

        character_limit = st.session_state.char_limit
        prompt = article(platform, character_limit, st.session_state.topic, st.session_state.keyword, st.session_state.company_name, st.session_state.hashtags)
        st.session_state.generated_response[platform]['prompt_char_count'] = len(prompt)
        response = model.generate_content(prompt)
        st.session_state.generated_response[platform]['response'] = response
        st.session_state.generated_response[platform]['input_tokens'] = response.usage_metadata.prompt_token_count
        st.session_state.generated_response[platform]['output_tokens'] = response.usage_metadata.candidates_token_count
        display_results(platform)

def generate_social_media_post():
    model = genai.GenerativeModel('gemini-1.5-pro')
    for platform in st.session_state.platforms:
        if platform not in st.session_state.generated_response:
            st.session_state.generated_response[platform] = {}

        character_limit = st.session_state.char_limit
        prompt = social_media_post(platform, character_limit, st.session_state.topic, st.session_state.keyword, st.session_state.company_name, st.session_state.hashtags)
        st.session_state.generated_response[platform]['prompt_char_count'] = len(prompt)
        response = model.generate_content(prompt)
        st.session_state.generated_response[platform]['response'] = response
        st.session_state.generated_response[platform]['input_tokens'] = response.usage_metadata.prompt_token_count
        st.session_state.generated_response[platform]['output_tokens'] = response.usage_metadata.candidates_token_count
        display_results(platform)

def generate_newsletter_content():
    model = genai.GenerativeModel('gemini-1.5-pro')
    prompt = newsletter(
        st.session_state.topic, 
        st.session_state.keyword, 
        st.session_state.company_name, 
        st.session_state.hashtags, 
        st.session_state.char_limit
    )
    
    st.session_state.generated_response = {
        'prompt_char_count': len(prompt)
    }
    
    response = model.generate_content(prompt)
    st.session_state.generated_response['response'] = response
    st.session_state.generated_response['input_tokens'] = response.usage_metadata.prompt_token_count
    st.session_state.generated_response['output_tokens'] = response.usage_metadata.candidates_token_count
    display_newsletter_results()

def generate_listicle():
    model = genai.GenerativeModel('gemini-1.5-pro')
    for platform in st.session_state.platforms:
        if platform not in st.session_state.generated_response:
            st.session_state.generated_response[platform] = {}
        prompt = listicles(platform, st.session_state.topic, st.session_state.keyword, st.session_state.hashtags, st.session_state.char_limit)
    st.session_state.generated_response = {
        'prompt_char_count': len(prompt)
    }
    response = model.generate_content(prompt)
    st.session_state.generated_response['response'] = response
    st.session_state.generated_response['input_tokens'] = response.usage_metadata.prompt_token_count
    st.session_state.generated_response['output_tokens'] = response.usage_metadata.candidates_token_count
    display_listicle_results()

def display_results(platform):
    platform_dic = st.session_state.generated_response[platform]
    response_obj = platform_dic['response']
    generated_result = response_obj.text
    st.session_state.generated_text = extract_generated_content(response_obj.text)
    st.session_state.image_captions = extract_image_captions(response_obj.text)

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
            description = placeholder[1:-1]
            image_url = st.session_state.image_mapping.get(description)
            if image_url:
                st.image(image_url, caption=description, use_column_width=True)

    st.markdown("### Gemini Cost Projection per Article/Post")
    st.write(f"Prompt Character Count: {platform_dic['prompt_char_count']}")
    st.write(f"Generated Content Character Count: {len(st.session_state.generated_text)}")

    input_token_rate = 0.000035
    output_token_rate = 0.000105

    token_cost = (
        platform_dic['input_tokens'] * input_token_rate +
        platform_dic['output_tokens'] * output_token_rate
    )
    st.write(f"Estimated cost: ${token_cost:.6f}")

def display_newsletter_results():
    response_obj = st.session_state.generated_response['response']
    generated_result = response_obj.text
    st.session_state.generated_text = extract_generated_content(generated_result)
    st.session_state.image_captions = extract_image_captions(generated_result)

    pattern = r'\[Image \d+: .*?\]'
    parts = re.split(pattern, generated_result)
    placeholders = re.findall(pattern, generated_result)

    for image_caption in st.session_state.image_captions:
        try:
            image_result = pexels_api.search_image(image_caption, 1)[0]
            st.session_state.image_mapping[image_caption] = image_result
        except Exception as e:
            st.error(f"An error occurred while fetching images: {e}")

    st.markdown("### Generated Newsletter:")
    for i, part in enumerate(parts):
        st.write(part)
        if i < len(placeholders):
            placeholder = placeholders[i]
            description = placeholder[1:-1]
            image_url = st.session_state.image_mapping.get(description)
            if image_url:
                st.image(image_url, caption=description, use_column_width=True)

    st.markdown("### Gemini Cost Projection for the Newsletter")
    st.write(f"Prompt Character Count: {st.session_state.generated_response['prompt_char_count']}")
    st.write(f"Generated Content Character Count: {len(st.session_state.generated_text)}")

    input_token_rate = 0.000035
    output_token_rate = 0.000105

    token_cost = (
        st.session_state.generated_response['input_tokens'] * input_token_rate +
        st.session_state.generated_response['output_tokens'] * output_token_rate
    )
    st.write(f"Estimated cost: ${token_cost:.6f}")

def display_listicle_results():
    response_obj = st.session_state.generated_response['response']
    generated_result = response_obj.text
    st.session_state.generated_text = extract_generated_content(generated_result)
    st.session_state.image_captions = extract_image_captions(generated_result)

    pattern = r'\[Image \d+: .*?\]'
    parts = re.split(pattern, generated_result)
    placeholders = re.findall(pattern, generated_result)

    for image_caption in st.session_state.image_captions:
        try:
            image_result = pexels_api.search_image(image_caption, 1)[0]
            st.session_state.image_mapping[image_caption] = image_result
        except Exception as e:
            st.error(f"An error occurred while fetching images: {e}")

    st.markdown("### Generated Listicle:")
    for i, part in enumerate(parts):
        st.write(part)
        if i < len(placeholders):
            placeholder = placeholders[i]
            description = placeholder[1:-1]
            image_url = st.session_state.image_mapping.get(description)
            if image_url:
                st.image(image_url, caption=description, use_column_width=True)

    st.markdown("### Gemini Cost Projection for the Listicle")
    st.write(f"Prompt Character Count: {st.session_state.generated_response['prompt_char_count']}")
    st.write(f"Generated Content Character Count: {len(st.session_state.generated_text)}")

    input_token_rate = 0.000035
    output_token_rate = 0.000105

    token_cost = (
        st.session_state.generated_response['input_tokens'] * input_token_rate +
        st.session_state.generated_response['output_tokens'] * output_token_rate
    )
    st.write(f"Estimated cost: ${token_cost:.6f}")