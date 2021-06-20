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

# for people who don't follow you back but you don't want to unfollow
whitelisted_usernames_unfollow_script = (
    "CardanoMonsters",
    "adapools_org",
    "cardano_updates",
    "_mermada",
    "CardanoStiftung",
    "YoroiWallet",
    "cardacitynft",
)
# for people who you want nothing to do with :)
blacklisted_usernames_follow_unfollow_scripts = (
    "NewCryptoBonus1",
    "DesireRugema",
    "doctorkevin",
)

# hashtags to blacklist (doesn't have to be hashtag, can be keyword)
blacklisted_hashtags_for_twitter_bot = (
    "fiewin.com",
    "#Corona",
    "Price:",
    "#SAFEMOON",
    "Change in 1hr",
    "Market cap:",
    "#studyplus",
    "#COVID",
    "#Trending",
    "#Newsnight",
    "#BreakingNews",
    "#Rajouri",
    "#JJK",
    "#Kishtwar",
    "#Covid_19",
    "#Covid19",
    "#Vaccine",
    "#Poonch",
    "#IndianArmy",
    "#JK",
    "#Blood",
    "ADA Compliant",
    "#Disability",
    "#disability",
    "#Defund",
    "no one uses #Cardano",
    "no one uses Cardano",
    "no one uses cardano",
    "#websiteaccessability",
    "#americanswithdisabilitiesact",
    "#Binance",
    "#BNB",
    "#DOGE",
)

# blacklisted people here
blacklisted_usernames_for_twitter_bot = (
    "topstonks",
    "chaintoday1",
    "CardanoPoolPeek",
    "adawow_io",
    "LacedWhales",
    "Nathan_Combs_",
    "AdaDarkPool",
    "CardanoPriceUpdates",
    "BalanceOt",
    "LacedWhales",
    "topcryptostats",
)
