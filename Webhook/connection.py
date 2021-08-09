import http.client
import Webhook

def id():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/<webhook_1>/event_summaries', '', {
        'Authorization': 'Bearer <api_key>'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data #Returns id metadata for every entry

def get():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/<webhook_1>/event_summaries?expand=event', '', {
        'Authorization': 'Bearer <api_key>'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data #Returns JSON Snipper metadata for every entry

def delete(dept):
    dept_id = {}
    dept_id = Webhook.current_id #Grab the currently stored ids of the entries just pulled

    if(dept == "All" and len(dept_id) != 0): #If pulling from All departments, delete everything pulled between the first and last entry
        end = dept_id[0]
        start = dept_id[len(dept_id)-1]
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("DELETE", '/v1/sources/<webhook_1>/events?start_id=%s&end_id=%s' % (start, end), '', {
        'Authorization': 'Bearer <api_key>'})
        conn.getresponse() 
        dept_id.clear()
        
    elif(dept != "All" and len(dept_id) != 0): #If pulling from a specific department, delete only the items pulled for that entries id
        for x in range (len(dept_id)):
            end = dept_id[x]
            conn = http.client.HTTPSConnection('api.pipedream.com')
            conn.request("DELETE", '/v1/sources/<webhook_1>/events?start_id=%s&end_id=%s' % (end, end), '', {
            'Authorization': 'Bearer <api_key>'})
            conn.getresponse()
        dept_id.clear()

def id_Fee():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/<webhook_2>/event_summaries', '', {
        'Authorization': 'Bearer <api_key>'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data #Returns id metadata for every entry

def get_Fee():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/<webhook_2>/event_summaries?expand=event', '', {
        'Authorization': 'Bearer <api_key>'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data #Returns JSON Snipper metadata for every entry

def delete_Fee():
    id = {}
    id = Webhook.current_id #Grab the currently stored ids of the entries just pulled

    if(len(id) != 0): #If something is there to pull, delete everything pulled between the first and last entry
        end = id[0]
        start = id[len(id)-1]
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("DELETE", '/v1/sources/<webhook_2>/events?start_id=%s&end_id=%s' % (start, end), '', {
        'Authorization': 'Bearer <api_key>'})
        conn.getresponse()
        id.clear()
