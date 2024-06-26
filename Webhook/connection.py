import Webhook
import http.client
import json

IDs = {}

def id(method):

    if(method == 1):
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("GET", '/v1/sources/%s/event_summaries' %(Webhook.__sourceUpload__), '', {
            'Authorization': '%s' %(Webhook.__authorization__)})
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return data #Returns id metadata for every entry
    else:
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("GET", '/v1/sources/%s/event_summaries' %(Webhook.__sourceFee__), '', {
            'Authorization': '%s' %(Webhook.__authorization__)})
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return data #Returns id metadata for every entry

def get(method):

    if(method == 1):
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("GET", '/v1/sources/%s/event_summaries?expand=event' %(Webhook.__sourceUpload__), '', {
            'Authorization': '%s' %(Webhook.__authorization__)})
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return data #Returns JSON Snipper metadata for every entry
    else:
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("GET", '/v1/sources/%s/event_summaries?expand=event' %(Webhook.__sourceFee__), '', {
            'Authorization': '%s' %(Webhook.__authorization__)})
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return data #Returns JSON Snipper metadata for every entry

def store(total, method):
    dict = json.loads(Webhook.id(method))
    IDs[total] = dict["data"][total]["id"]
    return IDs

def delete(method):
    
    if(method == 1):
        conn = http.client.HTTPSConnection('api.pipedream.com')
        if(len(IDs) != 0):
            end = IDs[0]
            start = IDs[len(IDs)-1]
            conn.request("DELETE", '/v1/sources/%s/events?start_id=%s&end_id=%s' %(Webhook.__sourceUpload__, start, end), '', {
                    'Authorization': '%s' %(Webhook.__authorization__)})
            conn.getresponse()
            IDs.clear()
    else:
        conn = http.client.HTTPSConnection('api.pipedream.com')
        if(len(IDs) != 0):
            end = IDs[0]
            start = IDs[len(IDs)-1]
            conn.request("DELETE", '/v1/sources/%s/events?start_id=%s&end_id=%s' %(Webhook.__sourceFee__, start, end), '', {
                    'Authorization': '%s' %(Webhook.__authorization__)})
            conn.getresponse()
            IDs.clear()