import http.client, Webhook

def id():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/<webhook>/event_summaries', '', {
        'Authorization': 'Bearer <api_key>'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def get():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/<webhook>/event_summaries?expand=event', '', {
        'Authorization': 'Bearer <api_key>'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def delete():
    dept_id = {}
    dept_id = Webhook.current_id

    if(len(dept_id) != 0):
        end = dept_id[len(dept_id)-1]
        start = dept_id[0]
        print(end, start)
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("DELETE", '/v1/sources/<webhook>/events?start_id=%s&end_id=%s' % (start, end), '', {
        'Authorization': 'Bearer <api_key>'})
        conn.getresponse() 

def delete_current():
    dept_id = {}
    dept_id = Webhook.current_id

    if(len(dept_id) != 0):
        for x in range (len(dept_id)):
            end = dept_id[x]
            conn = http.client.HTTPSConnection('api.pipedream.com')
            conn.request("DELETE", '/v1/sources/<webhook>/events?start_id=%s&end_id=%s' % (end, end), '', {
            'Authorization': 'Bearer <api_key'})
            conn.getresponse()
