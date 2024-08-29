#Image service for searching images on Pexels
#Implementation ref https://www.youtube.com/watch?v=WiFX89ozRiE&t=1s

import requests
import streamlit as st

class PexelsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.pexels.com/v1/"

    def search_image(self, query:str, per_page=5):
        headers = {'Authorization': self.api_key}
        params = {'query':query, 'per_page':per_page}
        response = requests.get(self.base_url+'search', headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return[photo['src']['original'] for photo in data['photos']]
        else:
            print("Failed to fetch the images", response.status_code)
            return []

    # Callback function to regenerate an image
    def regenerate_image(self, index):
        try:
            description = st.session_state.image_captions[index]
            # Fetch a new image URL using the Pexels API
            new_image_result = self.search_image(description, 1)[0]
            st.session_state.image_mapping[description] = new_image_result
            # Update the specific image in the UI
            st.session_state[f"image_{index}"] = new_image_result
        except Exception as e:
            st.error(f"An error occurred while regenerating the image: {e}")
            