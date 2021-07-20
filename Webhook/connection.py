import http.client, Webhook, json

def id():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/dc_RWuzvge/event_summaries', '', {
        'Authorization': 'Bearer 36177d2bb78cbd5b4eacc90577ccc2d5'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def get():
    conn = http.client.HTTPSConnection('api.pipedream.com')
    conn.request("GET", '/v1/sources/dc_RWuzvge/event_summaries?expand=event', '', {
        'Authorization': 'Bearer 36177d2bb78cbd5b4eacc90577ccc2d5'})
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    return data

def delete():
    Data = Webhook.id()
    total = Webhook.total()
    dict = json.loads(Data)
    list = dict["data"]
    if(total > 100):
        index = total - 100
        end = list[index].get('id')
    elif(total != 0):
        end = list[0].get('id')
    else:
        end = 0

    if(end != 0):
        conn = http.client.HTTPSConnection('api.pipedream.com')
        conn.request("DELETE", '/v1/sources/dc_RWuzvge/events?end_id=%s' % end, '', {
            'Authorization': 'Bearer 36177d2bb78cbd5b4eacc90577ccc2d5'})
        conn.getresponse()