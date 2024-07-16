import requests
from tavily import TavilyClient
import os

class DiningAgent:
    def __init__(self):
        self.tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    def run(self, destination, dietary_preferences):
        query = f"Best dining options in {destination} for {dietary_preferences}"
        response = self.tavily_client.search(query)
        return response['results']
