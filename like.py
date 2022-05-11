import requests

from headers import *


def like(tweetId):
    json_data = {
    'variables': '{"tweet_id":"'+tweetId+'"}',
    'queryId': 'lI07N6Otwv1PhnEgXILM7A',
    }
    data = '{"variables":"{\\"tweet_id\\":\\"'+tweetId+'\\"}","queryId":"lI07N6Otwv1PhnEgXILM7A"}'
    #data = '{"variables":"{\\"tweet_id\\":\\"{tweetId}\\"}","queryId":"lI07N6Otwv1PhnEgXILM7A"}'
    response = requests.post('https://twitter.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet', headers=headers, json=json_data)
    return response.json()