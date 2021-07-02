from typing import Text, Dict, List, Any

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Action, Tracker


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")
        knowledge_base.set_representation_function_of_object(
            "plant", lambda obj: obj["name"] + " also known as " + obj["botanical_name"] + ": " + obj["description"]
        )
        super().__init__(knowledge_base)

    def object_name_is_present(self, name: Text):
        for obj in self.knowledge_base.data["plant"]:
            if obj["name"] == name:
                return True

        return False


class SearchObjects(Action):

    def name(self) -> Text:
        return "search_objects"

    async def run(self,
                  dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        knowledge_base_action = MyKnowledgeBaseAction()
        entity = next(tracker.get_latest_entity_values("plant"), None)
        if entity:
            if knowledge_base_action.object_name_is_present(entity):
                response = "Yes, I can answer questions about this plant."
                dispatcher.utter_message(text=response)
                return []

        response = "I'm sorry, I cannot help this time. " \
                   "Please ask me to list all the plants I have information on."
        dispatcher.utter_message(text=response)
        return []
