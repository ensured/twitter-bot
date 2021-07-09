import tweepy
from time import sleep
from config import (
  blacklisted_usernames_follow_unfollow_scripts,
  api_key,
  api_secret,
  access_token,
  access_token_secret,
)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def autofollow():
    for follower in tweepy.Cursor(api.followers).items():
        try:
            if not follower.following:
                if (
                    follower.screen_name
                    in blacklisted_usernames_follow_unfollow_scripts
                ):
                    print(f"🔴 @{follower.screen_name} in the blacklist")
                else:
                    follower.follow()
                    print(f"🟢 Followed @{follower.screen_name}")
            else:
                print(f"🔴 @{follower.screen_name} already following me")
        except tweepy.TweepError as e:
            print(e)


if __name__ == "__main__":
  autofollow()
