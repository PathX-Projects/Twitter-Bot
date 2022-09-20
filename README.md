# How to Create Developer Credentials for the Twitter API:

1. Go to https://developer.twitter.com/en/portal/projects-and-apps

2. Create a new project:
    <a href="https://ibb.co/gDTgWmd"><img src="https://i.ibb.co/64Pstr8/Screen-Shot-2022-09-20-at-1-10-48-PM.png" alt="Screen-Shot-2022-09-20-at-1-10-48-PM" border="0" /></a>

3. Once you enter the app screen, create a new "development" app:
    <a href="https://ibb.co/tKSHGRS"><img src="https://i.ibb.co/H40KSZ0/Screen-Shot-2022-09-20-at-1-12-29-PM.png" alt="Screen-Shot-2022-09-20-at-1-12-29-PM" border="0" /></a>

4. Once you get to the "Keys & Tokens" section, make sure that you copy and store the __*API Key*__ and __*API Secret Key*__ in a safe place. You will need them to authenticate with the TwitterBot class.

    <a href="https://ibb.co/mFcGNf4"><img src="https://i.ibb.co/S73PfFB/Screen-Shot-2022-09-20-at-1-17-18-PM.png" alt="Screen-Shot-2022-09-20-at-1-17-18-PM" border="0" /></a>

5. Then click "App Settings" -> then "Keys and Tokens." On this page you will need to generate an access token and access token secret. You will need these as well to authenticate with the TwitterBot class.
    <a href="https://ibb.co/WVrZPqf"><img src="https://i.ibb.co/TWQ6bpt/Screen-Shot-2022-09-20-at-1-20-54-PM.png" alt="Screen-Shot-2022-09-20-at-1-20-54-PM" border="0" /></a>

# How to Use These Credentials to Authenticate the TwitterBot Class:

```python
from twitter_bot import TwitterBot

# Create a TwitterBot object
bot = TwitterBot(
    api_key="YOUR_TWITTER_API_KEY",
    api_secret_key="YOUR_TWITTER_API_SECRET_KEY",
    access_token="YOUR_TWITTER_ACCESS_TOKEN",
    access_token_secret="YOUR_TWITTER_ACCESS_TOKEN_SECRET"
)
```

# How to Use the TwitterBot Class:

```python
# Post a tweet
bot.post_tweet("Hello World!")

# Post a tweet with tags:
bot.post_tweet("Hello World!", tags=["bot", "python"])

# Post a tweet with an image:
bot.post_tweet("Hello World!", media_filepath="path/to/image.jpg")
```