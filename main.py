import os
import argparse
import requests

from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()


BASE_API_URL = "https://api-ssl.bitly.com/v4/"
HEADERS = {
    "Authorization": "Bearer {}".format(os.getenv("BITLY_TOKEN")),
}

class URLFormatError(TypeError):
    pass

def shorten_url_bitly(url):
    api_command = "bitlinks"
    json_data = {"long_url": url}

    response = requests.post(
        BASE_API_URL + api_command, headers=HEADERS, json=json_data)
    if response.ok:
        return response.json()['link']


def count_cliks(url):
    message = 'Количество переходов по ссылке bit.ly: '
    payload = {"units": "-1", "unit": "day"}
    api_command = "bitlinks/{}/clicks/summary".format(
        urlparse(url).netloc + urlparse(url).path)
    response = requests.get(
        BASE_API_URL + api_command, headers=HEADERS, params=payload)
    if response.ok:
        return message, response.json()['total_clicks']


def check_bitly_url(url):
    api_command = "bitlinks/{}".format(
        urlparse(url).netloc + urlparse(url).path)
    response = requests.get(BASE_API_URL + api_command, headers=HEADERS)
    if response.ok:
        return count_cliks(url)


def check_url(url):
    if urlparse(url).scheme == '':
        raise URLFormatError('Please provide the right scheme (http:// | https://) for URL!')
    elif urlparse(url).netloc == 'bit.ly':
        return check_bitly_url(url)
    else:
        return shorten_url_bitly(url)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Program for shorting url by bitly service'
    )
    parser.add_argument('url', help='URL for shorting')
    args = parser.parse_args()

    try:
        result = check_url(args.url)
        print(*result, sep="")
    except URLFormatError as error:
        exit(str(error))

