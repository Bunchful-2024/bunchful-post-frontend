import streamlit as st, requests, json

class FacebookAPI:
    def __init__(self, page_id, page_access_token):
        self.page_id = page_id
        self.page_access_token = page_access_token 
        self.base_url = "https://graph.facebook.com/v20.0/"

    def publish_post(self, message:str):
        fb_api_url = f'https://graph.facebook.com/v20.0/{self.page_id}/feed'

        payload = {
            'message': message,
            'access_token': self.page_access_token,
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(fb_api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            st.success("Post published successfully on Facebook!")
        else:
            st.error(f"Failed to publish post")

    def publish_post_with_photos(self, message):
        # Step 1: Upload photos with published state set to false
        photo_ids = []
        for photo_url in st.session_state.image_mapping.values():
            upload_url = f'https://graph.facebook.com/v20.0/{self.page_id}/photos'
            params = {
                'access_token': self.page_access_token,
                'published': 'false',
                'url': photo_url,
            }

            try:
                response = requests.post(upload_url, params=params)
                result = response.json()

                if 'id' in result:
                    photo_ids.append(result['id'])
                else:
                    st.error(f"Error uploading photo: {result}")

            except requests.exceptions.RequestException as e:
                st.error(f"Request error: {e}")

        # Step 2: Use the IDs of unpublished photos to post
        fb_api_url = f'https://graph.facebook.com/v20.0/{self.page_id}/feed'

        payload = {
            'message': message,
            'access_token': self.page_access_token,
        }
        headers = {
            'Content-Type': 'application/json'
        }

        for index, photo_id in enumerate(photo_ids):
            payload[f'attached_media[{index}]'] = f'{{"media_fbid":"{photo_id}"}}'

        response = requests.post(fb_api_url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            st.success("Post published successfully on Facebook!")
        else:
            st.error(f"Failed to publish post")
