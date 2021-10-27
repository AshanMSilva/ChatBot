from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from db.data import projects

class ActionProjectsSearch(Action):

    def name(self) -> Text:
        return "action_projects_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")
        size  = tracker.get_slot("size")
        land_type  = tracker.get_slot("land_type")
        projects_searched = []
        if not size:
            size = 0
        if land_type != 'නේවාසික' and land_type != 'ව්‍යාපාරික':
            dispatcher.utter_message(text="{} ප්‍රදේශයේ පර්චස් {}ට වැඩි ඉඩම් සොයමින් පවතී.".format(location, size))
            for i in projects:
                project = projects[i]
                if(project['location'] == location and project['size']>=int(size)):
                    projects_searched.append(project['project'])
            if(len(projects_searched) == 0):
                dispatcher.utter_message(text="කණගාටුයි, {} ප්‍රදේශයේ පර්චස් {}ට වැඩි ඉඩම් නොමැත.".format(location, size))
                return []
            return [SlotSet("projects", projects_searched)]    
        
        dispatcher.utter_message(text="{} ප්‍රදේශයේ පර්චස් {}ට වැඩි {} ඉඩම් සොයමින් පවතී.".format(location, size, land_type))

        for i in projects:
            project = projects[i]
            print(project)
            if(project['location'] == location and project['size']>=int(size) and project['type'] == land_type):
                projects_searched.append(project['project'])
        if(len(projects_searched) == 0):
            dispatcher.utter_message(text="කණගාටුයි, {} ප්‍රදේශයේ පර්චස් {}ට වැඩි {} ඉඩම් නොමැත.".format(location, size, land_type))
            return []
        return [SlotSet("projects", projects_searched)] 

class ActionProjectDetailsSearch(Action):

    def name(self) -> Text:
        return "action_project_details_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project = tracker.get_slot("project")

        project_searched = None
        dispatcher.utter_message(text="{} ව්‍යාපෘතිය පිළිබද විස්තර සොයමින් පවතී.".format(project))

        for i in projects:
            project_dict = projects[i]
            if(type != None):
                if(project_dict['project'] == project):
                    project_searched = project_dict
                    break
        if(project_searched == None):
            return []
        return [SlotSet("project_details", project_searched)] 
