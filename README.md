# Multi-Agent Travel Plan Generator

## Project Overview
This project creates a team of AI agents that collaborate to generate a personalized travel itinerary based on user inputs.

## Agents
- **User Input Agent**: Collects user travel details such as destination, travel dates, budget, interests, and dietary preferences.
- **Attraction Recommendation Agent**: Recommends attractions based on the user's interests and destination.
- **Accommodation Recommendation Agent**: Suggests accommodations based on the user's budget and destination.
- **Dining Recommendation Agent**: Recommends dining options based on the user's dietary preferences and destination.
- **Itinerary Generation Agent**: Compiles all recommendations into a detailed travel itinerary.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/travel-planner.git
   cd travel-planner
   pip install -r requirements.txt
   python main.py
   

## architecture
- agents
  1. user_input_agent
  2. attraction_agent
  3. dining_agent
  4. accommodation_agent
  5. itinerary_generation_agent
- output
- .env
- workflow
- main
- requirements.txt

## API usage
Tavily API

## examples of generated outcomes
Enter your travel destination: Paris
Enter your travel dates (e.g., 2024-07-20 to 2024-07-25): 2024-07-20 to 2024-07-25
Enter your budget: 1000
Enter your interests (e.g., museums, hiking, food): museums, food
Enter your dietary preferences: vegetarian

Here is your personalized travel itinerary:

Travel Itinerary for 2024-07-20 to 2024-07-25:

Attractions:
- Louvre Museum: The world's largest art museum and a historic monument in Paris, France.
- Eiffel Tower: A wrought-iron lattice tower on the Champ de Mars in Paris, France.

Accommodations:
- Hotel Paris: A budget-friendly hotel located near the city center with free breakfast and Wi-Fi.

Dining Options:
- Le Jardin des Pâtes: A vegetarian restaurant offering a variety of pasta dishes made with organic ingredients.
