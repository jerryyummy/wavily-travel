# Import necessary libraries and modules
from langgraph.graph import StateGraph, END  # For constructing state graphs
from langgraph.checkpoint.sqlite import SqliteSaver  # For saving workflow states to SQLite
import sqlite3  # Database library for SQLite connections
from agents.user_input_agent import UserInputAgent  # Handles user input for travel plans
from agents.attraction_agent import AttractionAgent  # Finds attractions based on user preferences
from agents.accommodation_agent import AccommodationAgent  # Searches for accommodations within budget
from agents.dining_agent import DiningAgent  # Recommends dining options per dietary preferences
from agents.itinerary_generation_agent import ItineraryGenerationAgent  # Assembles the final travel itinerary


# Define the structure of the state that each node in the graph will hold
class TravelPlanState(TypedDict):
    user_input: dict  # User-provided details like destination, dates, budget, interests
    attractions: list  # List of recommended attractions
    accommodations: list  # List of suitable accommodations
    dining_options: list  # List of dining recommendations
    itinerary: str  # Final assembled travel itinerary
    lnode: str  # Identifier for the current node in the workflow
    count: Annotated[int, operator.add]  # Counter with an additive behavior


def create_workflow():
    # Initialize a state graph with the TravelPlanState as its state type
    graph = StateGraph(TravelPlanState)

    # Define nodes for each planning stage with their respective agent's run methods
    user_input_node = graph.add_node("user_input", UserInputAgent().run)
    attraction_node = graph.add_node("attractions", AttractionAgent().run)
    accommodation_node = graph.add_node("accommodations", AccommodationAgent().run)
    dining_node = graph.add_node("dining", DiningAgent().run)
    itinerary_node = graph.add_node("itinerary", ItineraryGenerationAgent().run)

    # Configure transitions between nodes with conditions based on state data
    graph.add_edge(user_input_node, attraction_node,
                   lambda state: (state['user_input']['destination'], state['user_input']['interests']))
    graph.add_edge(user_input_node, accommodation_node,
                   lambda state: (state['user_input']['destination'], state['user_input']['budget']))
    graph.add_edge(user_input_node, dining_node,
                   lambda state: (state['user_input']['destination'], state['user_input']['dietary_preferences']))
    graph.add_edge(attraction_node, itinerary_node, lambda state: (
    state['attractions'], state['accommodations'], state['dining_options'], state['user_input']['travel_time']))
    graph.add_edge(accommodation_node, itinerary_node, lambda state: (
    state['attractions'], state['accommodations'], state['dining_options'], state['user_input']['travel_time']))
    graph.add_edge(dining_node, itinerary_node, lambda state: (
    state['attractions'], state['accommodations'], state['dining_options'], state['user_input']['travel_time']))
    graph.add_edge(user_input_node, itinerary_node,
                   lambda state: state['user_input']['travel_time'])  # Direct edge for travel time

    # Set the starting point of the workflow
    graph.set_entry_point(user_input_node)

    # Setup an in-memory SQLite database for saving workflow states
    memory = SqliteSaver(conn=sqlite3.connect(":memory:", check_same_thread=False))

    # Compile the graph, enabling it for execution with checkpointing support
    return graph.compile(checkpointer=memory)