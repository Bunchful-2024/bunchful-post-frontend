#Image service for searching images on Pexels
#Implementation ref https://www.youtube.com/watch?v=WiFX89ozRiE&t=1s

import requests

class PixelsAPI:
    def __init__(self,api_key):
        self.api_key = api_key
        self.base_url = "https://api.pexels.com/v1/"

        