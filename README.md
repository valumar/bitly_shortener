# Bitly url shorterer

Program for shorting the URL with Bitly service.
Has an additional option for counting cliks on Bitly links you have created.

### How to install

For proper use you have to get token from Bitly service.
Please see [API Bitly](https://dev.bitly.com/get_started.html).
You need `GENERIC ACCESS TOKEN`.

After receiving the token rename the file `.env-example` to `.env` and paste your token.
You should get something like this:

```
BITLY_TOKEN=17c09e20ad155405123ac1977542fecf00231da7
```

Python3 should be already installed. 
It is strictly recommended that you use [virtual environment](https://docs.python.org/3/library/venv.html) for project isolation. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
