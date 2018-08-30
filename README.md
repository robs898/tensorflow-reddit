### Background
https://www.tensorflow.org/tutorials/images/image_recognition
Tensor flow uses a trained model to classify any images you provide.

### Setup
get a reddit account and add an app so you can get an id and secret
https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

### Install
pip install pipenv
pipenv install

### Run
pipenv run python main.py --id <reddit client ID> --secret <reddit client secret> --subreddit pics

### Notes
You need 200MB to download the inception model
Only deals with jpg images for now. Anything else is skipped from the subreddit.

