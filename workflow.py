from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from agents.user_input_agent import UserInputAgent
from agents.attraction_agent import AttractionAgent
from agents.accommodation_agent import AccommodationAgent
from agents.dining_agent import DiningAgent
from agents.itinerary_generation_agent import ItineraryGenerationAgent

class TravelPlanState(TypedDict):
    user_input: dict
    attractions: list
    accommodations: list
    dining_options: list
    itinerary: str
    lnode: str
    count: Annotated[int, operator.add]

def create_workflow():
    graph = StateGraph(TravelPlanState)

    user_input_node = graph.add_node("user_input", UserInputAgent().run)
    attraction_node = graph.add_node("attractions", AttractionAgent().run)
    accommodation_node = graph.add_node("accommodations", AccommodationAgent().run)
    dining_node = graph.add_node("dining", DiningAgent().run)
    itinerary_node = graph.add_node("itinerary", ItineraryGenerationAgent().run)

    graph.add_edge(user_input_node, attraction_node, lambda state: (state['user_input']['destination'], state['user_input']['interests']))
    graph.add_edge(user_input_node, accommodation_node, lambda state: (state['user_input']['destination'], state['user_input']['budget']))
    graph.add_edge(user_input_node, dining_node, lambda state: (state['user_input']['destination'], state['user_input']['dietary_preferences']))
    graph.add_edge(attraction_node, itinerary_node, lambda state: (state['attractions'], state['accommodations'], state['dining_options'], state['user_input']['travel_time']))
    graph.add_edge(accommodation_node, itinerary_node, lambda state: (state['attractions'], state['accommodations'], state['dining_options'], state['user_input']['travel_time']))
    graph.add_edge(dining_node, itinerary_node, lambda state: (state['attractions'], state['accommodations'], state['dining_options'], state['user_input']['travel_time']))
    graph.add_edge(user_input_node, itinerary_node, lambda state: state['user_input']['travel_time'])

    graph.set_entry_point(user_input_node)
    memory = SqliteSaver(conn=sqlite3.connect(":memory:", check_same_thread=False))
    return graph.compile(checkpointer=memory)
