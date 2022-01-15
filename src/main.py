# ref https://www.youtube.com/watch?v=wlVcso4Ut5o
import json


def lambda_handler(event, context):
    event_json = json.dumps(event)
    # context_json = json.dumps(context)
    # data = {'event': event_json, 'context': context_json}
    # data_json = json.dumps(event_json)
    return {
        "statusCode": 200,
        "body": event_json
    }
