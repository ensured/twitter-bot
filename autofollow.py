import tweepy
from time import sleep
# i created a new api app so I could have less limitations, not
# sure how much it helps though.
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
    sleep(5)
    for follower in tweepy.Cursor(api.followers).items():
        sleep(0.2)
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
    while True:
        autofollow()
        print("(sleeping 300 seconds)")
        import sys
        import time
        from os import system

        clear = lambda: system("clear")
        # Automatically follow everyone back who follows you every 15 minutes
        for i in range(900, 0, -1):
            sys.stdout.write(f"sleeping for {str(i)}")
            sys.stdout.flush()
            time.sleep(1)
            clear()
