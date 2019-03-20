#!/bin/bash

heroku create slack-bot-platzi
heroku stack:set container
heroku config:set BOT_FICHA=$BOT_FICHA # Tras source .env
git push heroku master
heroku ps:scale worker=1
