# Server side of the GHO App

[![Build Status](https://travis-ci.org/gamingh/ghoAepp-server-side.svg?branch=master)](https://travis-ci.org/gamingh/ghoAepp-server-side)

Depends on [pdf-table-extract](https://github.com/JBBgameich/pdf-table-extract) in a python3 version.

If you want to setup your own server, just copy this repository to the target folder, most likely `/var/www/html/gho`, and set up a cron job that executes `python3 update.py` in `/var/www/html/gho` at least every two hours. The url of your json files for the app will be `http://your-server.tld/gho/vertretungsplan.json`. To view it from a browser, open `http://your-server.tld/gho/vertretungsplan.html`

## Usage
`python3 update.py $USERNAME $PASSWORD`
