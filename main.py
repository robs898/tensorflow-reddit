import praw
import requests
import classify_image
import re
import argparse


def main():
    args = get_args()
    reddit = auth(args.id, args.secret)
    subreddit = reddit.subreddit(args.subreddit)
    for submission in subreddit.new(limit=10):
        if re.match('.*\.(jpg|png|gif)$', submission.url) is None:
            print("Image was not in a valid format: " + submission.url)
        else:
            download_image(submission.url)
            lookup_image()


def get_args():
    parser = argparse.ArgumentParser(description='Reddit details')
    parser.add_argument('--id', help='Reddit client ID')
    parser.add_argument('--secret', help='Reddit client secret')
    parser.add_argument('--subreddit', help='Subreddit name')
    return parser.parse_args()

def auth(client_id, client_secret):
    return praw.Reddit(client_id=client_id,
                       client_secret=client_secret,
                       user_agent='web:image_classifier:v0.0.1')


def download_image(url, image_file_path = 'image.jpg'):
    print(url)
    with open(image_file_path, "wb") as file:
        response = requests.get(url, stream=True)
        file.write(response.content) 


def lookup_image(image_file_path = 'image.jpg'):
    classify_image.maybe_download_and_extract()
    classify_image.run_inference_on_image(image_file_path) 


if __name__ == "__main__":
    main()
