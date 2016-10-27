# <img src="http://www.freeiconspng.com/uploads/twitter-icon--basic-round-social-iconset--s-icons-0.png" width="48">Pytweet
Small python program using twitter API to send tweets.
This program will be improved with new features. please check To Do List

**Todo list**
- [x] send tweets.
- [ ] send images.
- [ ] get user object like (Nickname, Number of followers, followers list).
- [ ] working with followers api.

**Installation:**

- python2.7 [Download link](https://www.python.org/download/releases/2.7/)
- You will need to install Python's tweepy library:

Tweepy library
```
pip install tweepy
```
You may also use Git to clone the repository from Github and install it manually:
```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
python setup.py install
```

**How to use?**

1. [Download](https://github.com/magic-coding/pytweet/archive/master.zip) & Extract `Pytweet.zip` file.
2. Edit `tweet.py` file using any code editor.
3. You will need to create an app account on https://dev.twitter.com/apps
	1. Sign in with Twitter account (Don't use your own account)
	2. Create a new app account
	3. Modify the settings for that app account to allow read & write
	4. Generate a new OAuth token with those permissions

4. Following these steps will create 4 tokens that you will need to place in the `tweet.py` file:
```
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
API_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxx-xxxxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxx'

```

5.Save `tweet.py` file and enjoy.

**Example (Video)**

[![ScreenShot](http://s21.postimg.org/mu9976f07/2016_10_27_14_16_01.jpg)](https://player.vimeo.com/video/189128054)

**Have a problem?**

If you're having issues with or have questions about the program Please open new issue or contact with me via Twitter [@magic_coding](http://www.twitter.com/magic_coding)


**Conclusion**

In Conclusion hope you enjoy with this small programe and don't forget to follow me to get more free open source programes.

**License:**

As of October 27, 2016 Pytweet is licensed under the GPLv3+: http://choosealicense.com/licenses/gpl-3.0
