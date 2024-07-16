class ItineraryGenerationAgent:
    def run(self, attractions, accommodations, dining_options, travel_time):
        itinerary = f"Travel Itinerary for {travel_time}:\n\n"
        itinerary += "Attractions:\n"
        for attraction in attractions:
            itinerary += f"- {attraction['title']}: {attraction['snippet']}\n"
        itinerary += "\nAccommodations:\n"
        for accommodation in accommodations:
            itinerary += f"- {accommodation['title']}: {accommodation['snippet']}\n"
        itinerary += "\nDining Options:\n"
        for dining in dining_options:
            itinerary += f"- {dining['title']}: {dining['snippet']}\n"
        return itinerary
