# tweetindex-schema

[![CircleCI](https://img.shields.io/circleci/project/suddi/tweetindex-schema.svg)](https://github.com/suddi/tweetindex-schema)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1744184bdad7481c9efc794874d2375f)](https://www.codacy.com/app/suddir/tweetindex-schema?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=suddi/tweetindex-schema&amp;utm_campaign=Badge_Grade)
[![license](https://img.shields.io/github/license/suddi/tweetindex-schema.svg?maxAge=2592000)](https://github.com/suddi/tweetindex-schema)

JSON schema used for request and response validation in AWS API Gateway for [tweetindex-lambda](https://github.com/suddi/tweetindex-lambda)

## Setup

````
pip install -r requirements.txt -r test_requirements.txt
````

## Testing

````
nosetests --verbose --config tests/setup.cfg
````
