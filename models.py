from google.appengine.ext import db

class Quotes(db.Model):
   """
   Represents a line from an R.E.M. song.
   """
   quotes = db.TextProperty(default='')
   enabled = db.BooleanProperty()

def get_quote():
   quote_text = Quotes.get_by_key_name('quotes_1').quotes
   quote_lines = quote_text.split("\r\n")
   quotes = [quote for quote in quote_lines if not (quote.startswith('#') or len(quote)==0)]

   import random, time
   random.seed(time.time())
   quote_idx = random.randint(0,len(quotes)-1)
   return quotes[quote_idx]