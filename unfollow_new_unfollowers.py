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
)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# ------> change this to your twitter username <-------------
followers = api.followers_ids("cardanokid")
friends = api.friends_ids("cardanokid")

# # datetime stuff
# dt_now = datetime.today().strftime("%Y-%m-%d-%H:%M:%S")
# dt_yesterday = datetime.today() - timedelta(days=1)
# dt_now = str(dt_now)[0:10]
# dt_yesterday = str(dt_yesterday)[0:14]
# tweet = f"""Unfollowers {dt_yesterday[:-4]} - {dt_now}"""


# unfollow those who don't follow me back
def auto_unfollow():
    # todays_unfollowers = []
    '''
    this basically tells twitter I want to get all users after the first 50, 
    you can remove this index if you want and just whitelist everyone you don't 
    want to unfollow if they aren't following you.
    '''
    for friend in friends[:-50]:
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
                # if friend not in friends:
                #     continue
                # else:

                # todays_unfollowers.append(friend)
                api.destroy_friendship(friend)
                print(
                    f"🟢 Unfollowed @{api.get_user(friend).screen_name}, in blacklist or not following"
                )
                # tweet += f"\nUnfollowed @{api.get_user(friend).screen_name} ✓"
            else:
                print(f"🔴 Skipping {api.get_user(friend).screen_name}")

        except tweepy.TweepError as e:
            print(e)
    print("🟢 Finished")


while True:
    auto_unfollow()
    # if len(todays_unfollowers) == 0:
    #     print("No one to unfollow, so skipping Twitter status update today")
    # else:
    #     try:
    #         api.update_status(tweet)
    #         print("Daily Twitter status update complete ✓")
    #     except tweepy.TweepError as e:
    #         print(e)
    sleep(14400)  # 4 hours

