

[![Build Status](https://travis-ci.org/keyuls/DataIncubator.svg?branch=master)](https://travis-ci.org/keyuls/DataIncubator)

# Introduction
To run this project, follow below steps.
```
git clone https://github.com/keyuls/DataIncubator.git
cd DataIncubator
```
_(For localhost only)_
- Open DataIncubator.py file.
- Change host from 0.0.0.0 to 127.0.0.1

```
pip install -r requirements.txt
python DataIncubator.py
```
# Connect to Travis
 - Fork this repository
 - Signin to [TravisCI](travis-ci.org)
 - Flick the repository switch on
 
 .travis.yml is already included in repo. With a new git push, the new build will triggered. It will run testcases from _pytest_.  After successful integration testing, next step is to deploy on Heroku.
 
# Deploy to Heroku
- In  a current .tavis.yml file, it is mentioned about delopyment process. After successful passing of build, the code will push to Heroku to deployed with the app name _dataupload_

```
 deploy:
  provider: heroku
  api_key:
    secure: "API Key"
  app: dataupload
```

