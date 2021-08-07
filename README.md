## twitter-bot
* Fill in config.py with your api information and any other custom settings.

* If you want this to run on an Arduino or Raspberry Pi just use `crontab -e` and add `@reboot sleep 30 && (cd /home/path_to_script_folder && python3 twitter_bot.py)` or something similar.
* I run autofollow.py every 15 minutes using crontab -e and it seems to work well.
* [My Twitter](https://twitter.com/cardanokid)
