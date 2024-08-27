import streamlit as st, requests, json

class FacebookAPI:
    def __init__(self, page_id, page_access_token):
        self.page_id = page_id
        self.page_access_token = page_access_token 
        self.base_url = "https://graph.facebook.com/v20.0/"

    def publish_post(self, message:str, image_url:str):
        fb_api_url = f'https://graph.facebook.com/v20.0/{self.page_id}/photos'

        payload = {
            'message': message,
            'access_token': self.page_access_token,
            'url': image_url
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(fb_api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            st.success("Post published successfully on Facebook!")
        else:
            st.error(f"Failed to publish post")
