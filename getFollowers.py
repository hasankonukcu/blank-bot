import requests

from headers import *



params = (
    ('variables', '{"userId":"1489566101428125698","count":400,"includePromotedContent":false,"withSuperFollowsUserFields":true,"withDownvotePerspective":true,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true,"__fs_dont_mention_me_view_api_enabled":false,"__fs_interactive_text":false,"__fs_responsive_web_uc_gql_enabled":false}'),
)
def getFollowers():
    
    response = requests.get('https://twitter.com/i/api/graphql/1JUN1SoMOh6UA7bT3Gpumg/Following', headers=headers, params=params)
    return response.json()
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://twitter.com/i/api/graphql/1JUN1SoMOh6UA7bT3Gpumg/Following?variables=%7B%22userId%22%3A%221489566101428125698%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Afalse%2C%22withSuperFollowsUserFields%22%3Atrue%2C%22withDownvotePerspective%22%3Atrue%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%2C%22withSuperFollowsTweetFields%22%3Atrue%2C%22__fs_dont_mention_me_view_api_enabled%22%3Afalse%2C%22__fs_interactive_text%22%3Afalse%2C%22__fs_responsive_web_uc_gql_enabled%22%3Afalse%7D', headers=headers)
