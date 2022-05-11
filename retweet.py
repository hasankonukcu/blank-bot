import requests
from headers import *

def retweet(tweetId):
    json_data = {
        'variables': '{"tweet_id":"' + tweetId + '","dark_request":false}',
        'queryId': 'ojPdsZsimiJrUGLR1sjUtA',
    }

    response = requests.post('https://twitter.com/i/api/graphql/ojPdsZsimiJrUGLR1sjUtA/CreateRetweet', headers=headers,
                             json=json_data)
    return response.json()
