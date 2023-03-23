import tweepy
from twitter_configs.blacklisted_usernames_follow_unfollow_scripts import (
    blacklisted_usernames_follow_unfollow_scripts,
)
from twitter_configs.whitelisted_usernames_unfollow_script import (
    whitelisted_usernames_unfollow_script,
)
from twitter_configs import (
    api_key,
    api_secret,
    access_token,
    access_token_secret
)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

my_screen_name = api.me().screen_name
for friend in tweepy.Cursor(api.friends).items():
    status = api.show_friendship(
        source_screen_name=friend.screen_name, target_screen_name=my_screen_name
    )
    if status[0].following:
        print(f"{friend.screen_name} follows {my_screen_name}.")
    else:
        if friend.screen_name in whitelisted_usernames_unfollow_script:
            print(f"✓ @{friend.screen_name} whitelisted")
            continue  # ✓ whitelisted username
        my_input = input(
            f"{friend.screen_name} does not follow {my_screen_name}. Unfollow? (y/n): "
        )
        if my_input == "y":
            api.destroy_friendship(friend.id)
            print(f"Unfollowed {friend.screen_name}")
        else:
            print(f"Skipped {friend.screen_name}")
