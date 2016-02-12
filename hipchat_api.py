import requests
import json

API_URL = 'https://api.hipchat.com/v2/'
WEBHOOKS = {
    "dank": {
            "pattern" : "^/dank .+",
            "url" : "http://imgur-hipchat-dev.herokuapp.com",
            "event" : "room_message"
    },
    "dankdev": {
            "pattern" : "^/dankdev .+",
            "url" : "http://imgur-hipchat-dev.herokuapp.com",
            "event" : "room_message"
    },
    "jank" : {
            "pattern" : "^/jank .+",
            "url" : "http://imgur-hipchat-dev.herokuapp.com",
            "event" : "room_message"
    },
    "dankify": {
            "pattern" : "^/dankify .+",
            "url" : "http://imgur-hipchat-dev.herokuapp.com",
            "event" : "room_message"
    },
    "gank": {
            "pattern" : "^/gank .+",
            "url" : "http://imgur-hipchat-dev.herokuapp.com",
            "event" : "room_message"
    },
    "halp": {
            "pattern" : "^/halp",
            "url" : "http://imgur-hipchat-dev.herokuapp.com",
            "event" : "room_message"
    }
}


def setup_webhooks(room):
    hook_id = 0
    for hook in WEBHOOKS:
        requests.put(url=API_URL+'room/'+room+'/extension/webhook/'+hook_id, data=json.dumps(WEBHOOKS.get(hook)))
        hook_id += 1


def add_webhook(name, hook_id, pattern, url, event, room):
    # req = send_post_request(endpoint=API_URL+'room/'+room+'/extension/webhook/'+hook_id,
    #                            data=json.dumps(data),
    #                            headers={'Content-Length': ' 4'})
    data = {}
    requests.put(url=API_URL+'room/'+room+'/extension/webhook/'+hook_id, data="asd", kwargs=data)



if __name__=="__main__":

    setup_webhooks(1234,'asdf')