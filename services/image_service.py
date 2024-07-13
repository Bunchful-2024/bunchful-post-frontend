#Image service for searching images on Pexels
#Implementation ref https://www.youtube.com/watch?v=WiFX89ozRiE&t=1s

import requests

class PixelsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.pexels.com/v1/"

    def search_image(self, query:str, per_page=5):
        headers = {'Authorization': self.api_key}
        params = {'query':query, 'per_page':per_page}
        response = requests.get(self.base_url+'search', headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return[photo['url'] for photo in data['photos']]
        else:
            print("Failed to fetch the images", response.status_code)
            return []
