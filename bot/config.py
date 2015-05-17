import os

app_name = "ROVERLAPSE"

consumer_key = os.environ.get(app_name + '_CONSUMER_KEY')
consumer_secret = os.environ.get(app_name + '_CONSUMER_SECRET')
access_token = os.environ.get(app_name + '_ACCESS_TOKEN')
access_token_secret = os.environ.get(app_name + '_ACCESS_TOKEN_SECRET')

app_screen_name  = os.environ.get(app_name + '_SCREEN_NAME')
