# The requests library is imported but not directly used in this snippet; typically used for making HTTP requests.
import requests
# Importing the TavilyClient class to interact with the Tavily API for travel-related information.
from tavily import TavilyClient
# Importing the os module to access environment variables securely.
import os


class AccommodationAgent:
    """
    A class responsible for fetching accommodation options based on a destination and a budget limit.
    """

    def __init__(self):
        """
        Initializes the AccommodationAgent with a TavilyClient instance using the API key fetched from the environment.
        """
        # Retrieving the Tavily API key from the environment variable 'TAVILY_API_KEY'.
        # This approach keeps sensitive information like API keys out of the source code.
        self.tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    def run(self, destination, budget):
        """
        Executes a search for accommodations within the specified destination and budget constraints.

        Parameters:
        - destination (str): The location where accommodations are needed.
        - budget (str or int): The maximum budget for accommodations.

        Returns:
        - list: A list of accommodation results that fit the specified destination and budget, as provided by the Tavily API.
        """
        # Constructing a query to find the best accommodations under the given budget in the specified destination.
        query = f"Best accommodations in {destination} under {budget} budget"

        # Using the TavilyClient's search method to query the Tavily API with the constructed query string.
        response = self.tavily_client.search(query)

        # Returning the 'results' part of the API response, which contains the list of accommodations.
        return response['results']