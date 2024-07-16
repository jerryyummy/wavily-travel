# Import necessary libraries and modules
import os  # Provides a way of interacting with the operating system
from dotenv import load_dotenv  # Loads environment variables from a .env file

# Load environment variables from a .env file located in the same directory
load_dotenv()

# Importing custom workflow creation function from a local module named 'workflow'
from workflow import create_workflow

# Import Gradio library as 'gr' to build interactive UI for the application
import gradio as gr


# Function to generate a travel itinerary based on user inputs
def generate_itinerary(destination, travel_time, budget, interests, dietary_preferences):
    """
    Generates a travel itinerary given user inputs including destination, travel dates, budget, interests, and dietary preferences.

    Parameters:
    destination (str): The desired travel destination.
    travel_time (str): The period of the trip, typically formatted as start and end dates.
    budget (str): The financial limit for the trip.
    interests (str): User's areas of interest for activities during the trip.
    dietary_preferences (str): Dietary requirements or restrictions for meal planning.

    Returns:
    str: A detailed itinerary planned according to the user's inputs.
    """
    # Prepare the user input data in a dictionary format
    user_input = {
        "destination": destination,
        "travel_time": travel_time,
        "budget": budget,
        "interests": interests,
        "dietary_preferences": dietary_preferences
    }

    # Initialize and run the workflow with the user's input to get the itinerary
    graph = create_workflow()
    state = graph.run({"count": 0, "user_input": user_input})

    # Return the generated itinerary from the workflow's output state
    return state['itinerary']


# The main function to set up and launch the Gradio interface
def main():
    # Define the Gradio interface with a single tab for travel planning
    with gr.Blocks() as demo:
        with gr.Tab("Travel Planner"):  # Create a tab named "Travel Planner"
            # Define input components for the Gradio interface
            destination = gr.Textbox(label="Destination")  # Text entry for destination
            travel_time = gr.Textbox(label="Travel Dates")  # Text entry for travel date range
            budget = gr.Textbox(label="Budget")  # Text entry for budget
            interests = gr.Textbox(label="Interests")  # Text entry for interests
            dietary_preferences = gr.Textbox(label="Dietary Preferences")  # Text entry for dietary needs

            # Output component to display the generated itinerary
            output = gr.Textbox(label="Itinerary", lines=10)  # Multi-line text box for itinerary display

            # Button to trigger itinerary generation
            btn = gr.Button("Generate Itinerary")

            # Link the button click event to the itinerary generation function
            btn.click(fn=generate_itinerary,
                      inputs=[destination, travel_time, budget, interests, dietary_preferences],
                      outputs=output)  # Specify inputs and output for the function call

        # Launch the Gradio interface
        demo.launch()


# Entry point of the script
if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly