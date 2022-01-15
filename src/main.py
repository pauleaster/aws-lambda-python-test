# ref https://www.youtube.com/watch?v=wlVcso4Ut5o
import json

def lambda_handler(event, context):
    return {
        "status_code": 200,
        "body" : json.dumps(event["headers"]["X-forwarded-for"])
    }