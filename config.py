# your twitter username
twitter_username = ""

# your api details 
api_key = ""
api_secret = ""
access_token = ""
access_token_secret = ""

# usually the higher this number is the farther back in time it will pull tweets from
amount_of_posts_to_get = 15

# Like and Retweet tweets that are replies to tweets
like_and_retweet_replies = False

# enter as many hashtags here as you want
hashtags = [
    "#CardanoNFT",
    "#ADA",
    "#CardanoCommunity",
    "#CardanoFamily",
    "#CNTF",
]
search = " OR ".join(hashtags)  # ignore this

# for people who don't follow you back but you don't want to unfollow
whitelisted_usernames_unfollow_script = {
    "CardanoMonsters",
    "adapools_org",
    "cardano_updates",
    "_mermada",
    "CardanoStiftung",
    "YoroiWallet",
    "cardacitynft",
}
# for people who you want nothing to do with :)
blacklisted_usernames_follow_unfollow_scripts = {
    "NewCryptoBonus1",
    "DesireRugema",
    "doctorkevin",
}

# they don't have to be hashtags, can be keywords too
blacklisted_hashtags_for_twitter_bot = {
    "Price:",
    "#SAFEMOON",
    "Change in 1hr",
    "Market cap:",
    "Price:",
    "Price -",
    "#Binance",
    "#BNB",
    "#DOGE",
}

# blacklisted people
blacklisted_usernames_for_twitter_bot = {
    "topstonks",
    "chaintoday1",
    "adawow_io",
    "LacedWhales",
    "Nathan_Combs_",
    "AdaDarkPool",
    "CardanoPriceUpdates",
    "BalanceOt",
    "LacedWhales",
    "topcryptostats",
}
