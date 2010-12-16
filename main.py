#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

from models import *
import os

class MainHandler(webapp.RequestHandler):

   def get(self):
      import random, time
      random.seed(time.time())
      img_idx = random.randint(1,11)
      
      quote = get_quote()
      # quote_idx
      iframe = self.request.get('iframe')
      w = self.request.get('w')
      template_values = {
         'iframe': iframe,
         'w': w,
         'image_num':img_idx, 
         'quote':quote 
      }
      path = os.path.join(os.path.dirname(__file__),
                            'templates/index.html')
      self.response.out.write(template.render(path, template_values))

#    function get_image () {
#        srand ((double) microtime() * 1000000);
#        $random_number = rand(1,11);
#        return "$random_number.png";
#    }

class QuoteHandler(webapp.RequestHandler):

   def get(self):
      format = self.request.get('format')
      callback = self.request.get('callback')
      
      if (format=='text'):
         self.response.out.write(get_quote())
      elif (format=='json'):
         if (callback):
            self.response.out.write(
               "%s ({'quote':'%s','linkback':'http://rem.wallrazer.com/'})" %
               (callback, get_quote()))
         else:
            self.response.out.write(
               "{'quote':'%s','linkback':'http://rem.wallrazer.com/'}" % 
               (get_quote()))
      else:
         self.response.out.write("%s (<a href='http://rem.wallrazer.com/'>via</a>)" % (get_quote()))

def main():
   application = webapp.WSGIApplication([('/', MainHandler),
                                        ('/say', QuoteHandler) ],
                                       debug=True)
   wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
   main()
