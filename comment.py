import requests
from headers import *


def comment(tweetId,message):
    json_data = {
    'variables': '{"tweet_text":"'+message+'","reply":{"in_reply_to_tweet_id":"'+tweetId+'","exclude_reply_user_ids":[]},"media":{"media_entities":[],"possibly_sensitive":false},"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withSuperFollowsUserFields":true,"semantic_annotation_ids":[],"dark_request":false,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text_enabled":false,"__fs_responsive_web_uc_gql_enabled":false}',
    'queryId': '93lp5AgprJnHuDuGEY_Odg',
    }

    response = requests.post('https://twitter.com/i/api/graphql/93lp5AgprJnHuDuGEY_Odg/CreateTweet', headers=headers, json=json_data)
    return response.json()
