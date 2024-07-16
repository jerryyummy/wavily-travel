import requests  # For making HTTP requests, though not directly used in this snippet
from tavily import TavilyClient  # Importing the TavilyClient class for accessing Tavily API
import os  # To access environment variables securely


class DiningAgent:
    """
    A class to fetch dining options based on destination and dietary preferences using the Tavily API.
    """

    def __init__(self):
        """
        Initializes the DiningAgent with a TavilyClient instance configured using the API key from environment variables.
        """
        # Retrieving the Tavily API key from an environment variable for secure handling of credentials
        self.tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    def run(self, destination, dietary_preferences):
        """
        Searches for and returns the best dining options based on the provided destination and dietary preferences.

        Parameters:
        - destination (str): The location where dining options are sought.
        - dietary_preferences (str): Specific dietary requirements or preferences for filtering the results.

        Returns:
        - list: A list of dining options that match the search criteria, as returned by the Tavily API.
        """
        # Formulating a search query combining destination and dietary preferences
        query = f"Best dining options in {destination} for {dietary_preferences}"

        # Using the TavilyClient to execute a search with the constructed query
        response = self.tavily_client.search(query)

        # Returning the 'results' section of the API response, which contains the dining options
        return response['results']