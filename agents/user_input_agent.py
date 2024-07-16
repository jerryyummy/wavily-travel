class UserInputAgent:
    def run(self):
        destination = input("Enter your travel destination: ")
        travel_time = input("Enter your travel dates (e.g., 2024-07-20 to 2024-07-25): ")
        budget = input("Enter your budget: ")
        interests = input("Enter your interests (e.g., museums, hiking, food): ")
        dietary_preferences = input("Enter your dietary preferences: ")
        return {
            "destination": destination,
            "travel_time": travel_time,
            "budget": budget,
            "interests": interests,
            "dietary_preferences": dietary_preferences
        }
