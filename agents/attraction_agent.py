import requests
from tavily import TavilyClient
import os

class AttractionAgent:
    def __init__(self):
        self.tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    def run(self, destination, interests):
        query = f"Best attractions in {destination} for people interested in {interests}"
        response = self.tavily_client.search(query)
        return response['results']
