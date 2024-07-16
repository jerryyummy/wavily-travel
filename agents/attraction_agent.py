import requests  # Library for making HTTP requests, not directly utilized in this snippet
from tavily import TavilyClient  # Importing TavilyClient for accessing Tavily API services
import os  # Operating system interfaces, used here to fetch environment variables securely


class AttractionAgent:
    """
    A class designed to fetch top attractions based on a specified destination and personal interests using the Tavily API.
    """

    def __init__(self):
        """
        Initializes the AttractionAgent with a TavilyClient instance, configuring it with the API key from the environment.
        """
        # Retrieves the Tavily API key from the environment variable 'TAVILY_API_KEY', ensuring secure management of API credentials
        self.tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    def run(self, destination, interests):
        """
        Executes a search for attractions tailored to the provided destination and interests.

        Parameters:
        - destination (str): The geographical location where attractions are being sought.
        - interests (str): User's specific areas of interest for filtering attraction recommendations.

        Returns:
        - list: A collection of attraction results matching the search criteria, as returned by the Tavily API.
        """
        # Constructs a query string to search for attractions fitting the user's destination and interests
        query = f"Best attractions in {destination} for people interested in {interests}"

        # Invokes the Tavily API's search functionality with the constructed query
        response = self.tavily_client.search(query)

        # Extracts and returns the 'results' portion of the API response, which contains the list of attractions
        return response['results']