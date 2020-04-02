# tweetindex-schema

[![CircleCI](https://circleci.com/gh/suddi/tweetindex-schema.svg?style=svg)](https://circleci.com/gh/suddi/tweetindex-schema)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1744184bdad7481c9efc794874d2375f)](https://www.codacy.com/app/suddir/tweetindex-schema)
[![license](https://img.shields.io/github/license/suddi/tweetindex-schema.svg?maxAge=2592000)](https://github.com/suddi/tweetindex-schema)

JSON schema used for request and response validation in AWS API Gateway for [tweetindex-lambda](https://github.com/suddi/tweetindex-lambda)

## Setup

````sh
pip install virtualenvwrapper
````

````sh
mkvirtualenv tweetindex-schema

pip install --requirement requirements.txt --requirement test_requirements.txt
````

## Linting

````sh
python setup.py lint
````

## Testing

````sh
python setup.py test
````
