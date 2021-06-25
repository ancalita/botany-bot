# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")
        knowledge_base.set_representation_function_of_object(
            "plant", lambda obj: obj["name"] + " also known as " + obj["botanical_name"] + ": " + obj["description"]
        )
        super().__init__(knowledge_base)
