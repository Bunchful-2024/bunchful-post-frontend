import streamlit as st, requests, json

class MediumAPI:
    def __init__(self, medium_token):
        self.medium_token = medium_token 

    def get_author_id(self):
        payload = {}
        headers = {
            'Host': 'api.medium.com',
            'Authorization': f"Bearer {self.medium_token}",
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

        response = requests.request("GET", "https://api.medium.com/v1/me", headers=headers, data=payload)
        response.raise_for_status()
        author_id = response.json()['data']['id']
        # store author id
        self.author_id = author_id

        return self.author_id

    def publish_post(self, message:str, title:str):
        # Medium API endpoint for posting
        medium_url = f"https://api.medium.com/v1/users/{self.author_id}/posts"

        payload = json.dumps({
            "title": title,
            "contentFormat": "markdown",
            "content": message,
            "publishStatus": "public"
        })

        headers = {
            'Host': 'api.medium.com',
            'Authorization': f"Bearer {self.medium_token}",
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Accept-Charset': 'utf-8',
        }

        response = requests.post(medium_url, headers=headers, data=payload)

        if response.status_code == 201:
            st.success("Post published successfully on Medium!")
        else:
            st.error(f"Failed to publish post: {response.text}")