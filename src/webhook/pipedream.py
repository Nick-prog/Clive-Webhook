import http.client
import json

import os
from dotenv import load_dotenv

class Pipedream:

    def __init__(self, doc_type: int):
        """Class created to house methods for Pipedream interactions. Pivotes on
        doc_type for all get, store, and delete calls.

        :param doc_type: document key indicater
        :type doc_type: int
        """

        self.conn = http.client.HTTPSConnection('api.pipedream.com')

        load_dotenv()

        if doc_type == 1:
            self.target = os.getenv("UPLOAD_KEY")
        elif doc_type == 2:
            self.target = os.getenv("FEE_KEY")
        elif doc_type == 3:
            self.target = os.getenv("TEST_KEY")

        self.auth = os.getenv("AUTH_KEY")

        self.IDs = []

    def get_events(self) -> list:
        """Method for getting all event summaries currently in our Pipedream webhook.

        :return: string of metadata stored in nested lists.
        :rtype: list
        """

        self.conn.request("GET", f'/v1/sources/{self.target}/event_summaries', '', {'Authorization': f'Bearer {self.auth}'})
        res = self.conn.getresponse()
        return res.read().decode("utf-8")
    
    def get_data(self) -> list:
        """Method for getting all event summaries currently in our Pipedream webhook,
        but in a more entry oriented way.

        :return: string of metadata stored in nested lists.
        :rtype: list
        """

        self.conn.request("GET", f'/v1/sources/{self.target}/event_summaries?expand=event', '', {'Authorization': f'Bearer {self.auth}'})
        res = self.conn.getresponse()
        return res.read().decode("utf-8")

    def store_data(self, idx: int) -> None:
        """Method for storing event id information as we work our way through each entry. Used for
        later deletion calls.

        :param idx: current index
        :type idx: int
        """

        metadata = json.loads(self.get_events())
        self.IDs.append(metadata["data"][idx]["id"])
    
    def delete_data(self) -> None:
        """Method for deleting stored events to prevent repeat download and store calls.
        """
        
        if(len(self.IDs) != 0):
            self.conn.request("DELETE", f'/v1/sources/{self.target}/events?start_id={self.IDs[(len(self.IDs))-1]}&end_id={self.IDs[0]}', '', {'Authorization': f'Bearer {self.auth}'})
            self.conn.getresponse()
            self.IDs.clear()