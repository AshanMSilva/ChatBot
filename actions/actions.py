from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from db.data import projects
from db.data import agents

class ActionProjectsSearch(Action):

    def name(self) -> Text:
        return "action_projects_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot("location")
        size  = tracker.get_slot("size")
        land_type  = tracker.get_slot("land_type")
        inequality  = tracker.get_slot("inequality")
        projects_searched = []
        if not size:
            size = 0
        if land_type != 'නේවාසික' and land_type != 'ව්‍යාපාරික':
            dispatcher.utter_message(text="{} ප්‍රදේශයේ පර්චස් {}ට වැඩි ඉඩම් සොයමින් පවතී.".format(location, size))
            has_inequality = False
            if(inequality == 'වැඩි' or inequality == 'අඩු'):
                has_inequality = True
            for i in projects:
                project = projects[i]
                if(has_inequality == True):
                    if(inequality == 'වැඩි'):
                        if(project['location'] == location and project['size']>int(size)):
                            projects_searched.append(project['project'])
                    elif(inequality == 'අඩු'):
                        if(project['location'] == location and int(size)> project['size']):
                            projects_searched.append(project['project'])
                else:
                    if(project['location'] == location and project['size']>=int(size)):
                        projects_searched.append(project['project'])
            if(len(projects_searched) == 0):
                dispatcher.utter_message(text="කණගාටුයි, {} ප්‍රදේශයේ පර්චස් {}ට වැඩි ඉඩම් නොමැත.".format(location, size))
                return []
            return [SlotSet("projects", projects_searched)]    
        
        dispatcher.utter_message(text="{} ප්‍රදේශයේ පර්චස් {}ට වැඩි {} ඉඩම් සොයමින් පවතී.".format(location, size, land_type))

        for i in projects:
            project = projects[i]
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
        print(project)
        project_searched = None
        dispatcher.utter_message(text="{} ව්‍යාපෘතිය පිළිබද විස්තර සොයමින් පවතී.".format(project))

        for i in projects:
            project_dict = projects[i]
            if(project_dict['project'] == project):
                project_searched = project_dict
                break
        if(project_searched == None):
            return []
        dispatcher.utter_message(text="{}".format(project_searched))
        return [SlotSet("project_details", project_searched)] 

class ActionAgentDetailsSearch(Action):

    def name(self) -> Text:
        return "action_agent_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project = tracker.get_slot("project")
        location = tracker.get_slot("location")
        print(location)

        agent_searched = None
        dispatcher.utter_message(text="{} ව්‍යාපෘතියට අදාළ එජෙන්ට් පිළිබද විස්තර සොයමින් පවතී.".format(project))

        for i in agents:
            agent_dict = agents[i]
            
            if(location != None):
                if(agent_dict['location'] == location):
                    agent_searched = agent_dict
                    break
        if(agent_searched == None):
            return []
        dispatcher.utter_message(text="{}".format(agent_searched))
        return [SlotSet("agent_details", agent_searched)] 
