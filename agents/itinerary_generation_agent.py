class ItineraryGenerationAgent:
    def run(self, attractions, accommodations, dining_options, travel_time):
        """
        Generates a formatted travel itinerary given lists of attractions, accommodations, and dining options, along with the travel time period.

        Parameters:
        - attractions (list): A list of dictionaries, each containing details about an attraction with keys like 'title' and 'snippet'.
        - accommodations (list): Similar to attractions, but for accommodation details.
        - dining_options (list): Likewise, a list of dictionaries detailing dining venues.
        - travel_time (str): A string representing the period of the trip (e.g., "2024-07-20 to 2024-07-25").

        Returns:
        - itinerary (str): A formatted string summarizing the travel itinerary including attractions, accommodations, and dining options.
        """

        # Start constructing the itinerary message with the travel period
        itinerary = f"Travel Itinerary for {travel_time}:\n\n"

        # Add attractions to the itinerary
        itinerary += "Attractions:\n"
        for attraction in attractions:
            # For each attraction, append its title and a brief snippet to the itinerary
            itinerary += f"- {attraction['title']}: {attraction['snippet']}\n"

        # Add accommodations to the itinerary
        itinerary += "\nAccommodations:\n"
        for accommodation in accommodations:
            # Similarly, add accommodation details
            itinerary += f"- {accommodation['title']}: {accommodation['snippet']}\n"

        # Include dining options in the itinerary
        itinerary += "\nDining Options:\n"
        for dining in dining_options:
            # Append dining venue details
            itinerary += f"- {dining['title']}: {dining['snippet']}\n"

        # Return the complete itinerary string
        return itinerary