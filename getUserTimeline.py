import requests
from headers import *


params = {
    'variables': '{"userId":"1516512264504893442","count":20,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withSuperFollowsUserFields":true,"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"withVoice":true,"withV2Timeline":true,"__fs_responsive_web_like_by_author_enabled":false,"__fs_dont_mention_me_view_api_enabled":true,"__fs_interactive_text_enabled":true,"__fs_responsive_web_uc_gql_enabled":false,"__fs_responsive_web_edit_tweet_api_enabled":false}',
}
def getUserTimeline():
    resp = requests.get('https://twitter.com/i/api/graphql/cHgRKiUCS0R9UF0Io63POQ/UserTweets', params=params,headers=headers)
    return resp.json()




