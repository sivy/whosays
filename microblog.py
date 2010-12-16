import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from models import *
import os

import twitter

API_ACCOUNT = "remsays";
API_PWD = "worldleaderpretend";

class TwitterHandler(webapp.RequestHandler):

   def get(self):
      quote = get_quote()
      # quote_idx
      api = twitter.Api(username=API_ACCOUNT, password=API_PWD)
      status = api.PostUpdate(quote)


def main():
   application = webapp.WSGIApplication([('/post_as_tweet', TwitterHandler)],
                                       debug=True)
   wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
   main()
