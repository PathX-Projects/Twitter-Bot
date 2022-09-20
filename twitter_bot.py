import tweepy
import time
from random import randint


class TwitterBot(tweepy.API):
    def __init__(self, twitter_api_key: str, twitter_api_secret_key: str, twitter_access_token: str, twitter_access_token_secret: str):
        # Authenticate to Twitter
        auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
        auth.set_access_token(twitter_access_token, twitter_access_token_secret)

        # Initialize Super Class
        super().__init__(auth)

    def post_tweet(self, post_text: str, tags: list[str], media_filepath: str = None) -> None:
        """
        The post_tweet function is used to post a tweet to the twitter account.
        It takes in 3 parameters: post_text, tags, and media_filepath
        The second parameter is . The third parameter is a list of strings containing hashtags that will be added at the end of your post.
        
        :param post_text:str: The caption/text for the Twitter post 
        :param tags:list[str]: A list of tags to append to the post
        :param media_filepath:str=None: Pass in a filepath to an image that will be uploaded and attached to the tweet
        """
        try:
            # Add tags to post:
            for i, tag in enumerate(tags):
                if len(post_text) <= (280 - len(tag) - 2):  # Subtract 2 to account for the space and hashtag
                    post_text += f"{' ' if i==0 else ''}#{tag}"

            # Check media and cooldown and post:
            if media_filepath:
                self._post_with_media(media_filepath, post_text)
            else:
                self._post_without_media(post_text)

            print(f"Tweet Posted: {post_text}")
        except Exception as e:
            raise Exception(f"Unable to post to twitter. Error Code:\n{e}")

    def _post_with_media(self, path_to_media: str, post: str):
        self.update_status_with_media(filename=path_to_media, status=post)

    def _post_without_media(self, post: str):
        self.update_status(status=post)