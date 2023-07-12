import os

from fastapi_poe import make_app
from modal import Image, Secret, Stub, asgi_app

from reddit_summary_bot import RedditSummaryBot

image = Image.debian_slim().pip_install_from_requirements("requirements.txt")
stub = Stub("reddit-summary-bot")


@stub.function(image=image, secret=Secret.from_name("reddit-summary-app"))
@asgi_app()
def fastapi_app():
    bot = RedditSummaryBot(
        reddit_client_id=os.environ["REDDIT_CLIENT_ID"],
        reddit_client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    )
    POE_API_KEY = "3BgqPu6jLwx9a78r2rWcuO8MARtt3hQO"
    app = make_app(bot, api_key=POE_API_KEY)
    return app
