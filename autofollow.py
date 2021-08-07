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
                    continue
                else:
                    follower.follow()
                    print(f"🟢 Followed @{follower.screen_name}")
                    try:
                        media = api.media_upload(filename="your_media_goes_here.gif")
                        api.send_direct_message(
                            follower.id,
                            f"[Automated Message]\n\nThanks for the follow @{follower.screen_name}!\nwrite whatever you want",
                            attachment_type="media",
                            attachment_media_id=media.media_id,
                        )
                    except:
                        print("something is not working as expected.")
                    with open("autofollowed.txt", "a+") as f:
                        f.write(f"{follower.screen_name}\n")
            else:
                continue
        except tweepy.TweepError as e:
            print(e)

if __name__ == "__main__":
  autofollow()
