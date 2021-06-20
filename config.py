# your api details go here ↓↓↓
api_key = ""
api_secret = ""
access_token = ""
access_token_secret = ""

# amount of posts to get before rerunning the function 'fav_and_retweet()'
# the larger the number the farther back the tweets you get will be (time wise)
amount_of_posts_to_get = 15

# enter as many hashtags here as you want (may need to update twitter_bot.py with the added or removed values)
search_a = "#CardanoNFT"
search_b = "#ADA"
search_c = "#Cardano"
search_d = "#CardanoCommunity"
search_e = "#CardanoFamily"
search_f = "#CNTF"

# blacklisted people here
blacklisted_usernames = (
    "Nathan_Combs_",
    "LacedWhales",
    "adawow_io",
    "LacedWhales",
    "AdaDarkPool",
    "CardanoPriceUpdates",
)

# hashtags to blacklist
blacklisted_hashtags = (
    # "RT @",
    "#DOGE",
    "#doge",
)
