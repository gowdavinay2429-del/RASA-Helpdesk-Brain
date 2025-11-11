from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCreateTicket(Action):

    def name(self) -> Text:
        # This name MUST match the one in domain.yml
        return "action_create_ticket"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the user's last message (the problem description)
        problem_details = tracker.latest_message.get('text')

        # --- THIS IS WHERE YOU WOULD ADD API CODE ---
        # For now, we will just pretend.
        ticket_id = "TICKET-12345"
        
        # This is how the bot replies
        dispatcher.utter_message(text=f"OK. I have created {ticket_id} for your problem: '{problem_details}'")

        return []