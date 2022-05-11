import requests

from headers import *

def dataFun(userId):
    data = {
    'include_profile_interstitial_type': '1',
    'include_blocking': '1',
    'include_blocked_by': '1',
    'include_followed_by': '1',
    'include_want_retweets': '1',
    'include_mute_edge': '1',
    'include_can_dm': '1',
    'include_can_media_tag': '1',
    'include_ext_has_nft_avatar': '1',
    'skip_status': '1',
    'user_id': userId
    }
    
    return data
def Follow(userId):
    
    response = requests.post('https://twitter.com/i/api/1.1/friendships/create.json', headers=headers, data=dataFun(userId))
    return response