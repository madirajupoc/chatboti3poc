# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime
from elasticsearch import Elasticsearch
import requests
import json

class  ActionQueryResponse(Action):
    def name(self):
        return 'action_query_response'

    def run(self, dispatcher, tracker, domain): 
        #context can be used to narrow down to the correct set of data
        context = tracker.get_slot('environment')
        querytosend=(tracker.latest_message)['text'] 
        print(context)
        es = Elasticsearch()
        
        res = es.search(index="_all", body={'size':1,'query':{'match':{'Question':querytosend}}})
        List_length = len(res['hits']['hits'])
        if List_length > 0:
            score =  res['hits']['hits'][0]['_score']
            response1=(res['hits']['hits'][0]['_source']['Answer'])
            if score > 6: 
                dispatcher.utter_message(response1)
            else:
                dispatcher.utter_message(response1)
                dispatcher.utter_message("Score for this is  %s"%score)
        else:
            dispatcher.utter_message("No result fetched, Please rephrase your Query. For support contact qnabotsupport@spglobal.com ")
        
     