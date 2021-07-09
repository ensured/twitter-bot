import tweepy
from time import sleep

# from datetime import datetime, timedelta
from config import (
    whitelisted_usernames_unfollow_script,
    blacklisted_usernames_follow_unfollow_scripts,
    api_key, # may need to generate a new api app in case of any limitations, you don't have to
    api_secret,
    access_token,
    access_token_secret,
    twitter_username,
)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

followers = api.followers_ids(twitter_username)
friends = api.friends_ids(twitter_username)

def auto_unfollow():
    '''
    You can add '[:-50]' to end of friends if you want to start after first 50 people you follow.
    Make sure to whitelist the usernames you don't want this script to auto unfollow. Example: IOHK_Charles
    '''
    for friend in friends:
        try:
            if (
                api.get_user(friend).screen_name
                in whitelisted_usernames_unfollow_script
            ):
                print(f"🔴 Skipping @{api.get_user(friend).screen_name} (✓ whitelisted)")
                continue
            if (
                friend not in followers
                or api.get_user(friend).screen_name
                in blacklisted_usernames_follow_unfollow_scripts
            ):

                api.destroy_friendship(friend)
                print(
                    f"🟢 Unfollowed @{api.get_user(friend).screen_name}, in blacklist or not following"
                )
            else:
                print(f"🔴 Skipping {api.get_user(friend).screen_name}")

        except tweepy.TweepError as e:
            print(e)
    print("🟢 Finished")


while True:
    auto_unfollow()
    sleep(14400)  # 4 hours


