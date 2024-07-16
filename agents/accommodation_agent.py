import requests
from tavily import TavilyClient
import os

class AccommodationAgent:
    def __init__(self):
        self.tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    def run(self, destination, budget):
        query = f"Best accommodations in {destination} under {budget} budget"
        response = self.tavily_client.search(query)
        return response['results']
