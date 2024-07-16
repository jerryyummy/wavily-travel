import os
from dotenv import load_dotenv

load_dotenv()

from workflow import create_workflow
import gradio as gr


def generate_itinerary(destination, travel_time, budget, interests, dietary_preferences):
    user_input = {
        "destination": destination,
        "travel_time": travel_time,
        "budget": budget,
        "interests": interests,
        "dietary_preferences": dietary_preferences
    }
    graph = create_workflow()
    state = graph.run({"count": 0, "user_input": user_input})
    return state['itinerary']


def main():
    with gr.Blocks() as demo:
        with gr.Tab("Travel Planner"):
            destination = gr.Textbox(label="Destination")
            travel_time = gr.Textbox(label="Travel Dates")
            budget = gr.Textbox(label="Budget")
            interests = gr.Textbox(label="Interests")
            dietary_preferences = gr.Textbox(label="Dietary Preferences")
            output = gr.Textbox(label="Itinerary", lines=10)

            btn = gr.Button("Generate Itinerary")
            btn.click(fn=generate_itinerary,
                      inputs=[destination, travel_time, budget, interests, dietary_preferences],
                      outputs=output)
        demo.launch()


if __name__ == "__main__":
    main()
