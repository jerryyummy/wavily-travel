class UserInputAgent:
    def run(self):
        # Prompt the user to enter their travel destination.
        destination = input("Enter your travel destination: ")

        # Ask the user to input their travel date range in the format of 'YYYY-MM-DD to YYYY-MM-DD'.
        travel_time = input("Enter your travel dates (e.g., 2024-07-20 to 2024-07-25): ")

        # Request the user to enter their budget amount for the trip.
        budget = input("Enter your budget: ")

        # Inquire about the user's interests, such as museums, hiking, or food, separated by commas if multiple.
        interests = input("Enter your interests (e.g., museums, hiking, food): ")

        # Ask the user to specify any dietary preferences they may have.
        dietary_preferences = input("Enter your dietary preferences: ")

        # Compile the collected information into a dictionary and return it.
        return {
            "destination": destination,  # The place the user intends to travel to
            "travel_time": travel_time,  # The period during which the user plans to travel
            "budget": budget,  # The financial limit set for the trip
            "interests": interests,  # Activities or attractions the user is interested in
            "dietary_preferences": dietary_preferences  # Food preferences or restrictions
        }