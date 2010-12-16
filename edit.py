import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from models import *
import os

class EditHandler(webapp.RequestHandler):

   def get(self):
      import random, time
      random.seed(time.time())
      img_idx = random.randint(1,11)
      
      # one record for quotes right now
      quotes = Quotes.get_or_insert('quotes_1');
      quotes_text = quotes.quotes
      # quote_idx
      template_values = {
         'quotes': quotes_text,
      }
      path = os.path.join(os.path.dirname(__file__),
                            'templates/edit.html')
      self.response.out.write(template.render(path, template_values))

   def post(self):
      quotes = Quotes.get_or_insert('quotes_1')
      quotes.quotes = self.request.get('quotes')
      quotes.save()
      template_values = {}
      path = os.path.join(os.path.dirname(__file__),
                            'templates/edit_done.html')
      self.response.out.write(template.render(path, template_values))

def main():
   application = webapp.WSGIApplication([('/edit', EditHandler)],
                                       debug=True)
   wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
   main()
