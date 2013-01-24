#! /usr/bin/python

import webapp2

from formulalib.handlers import (HomeHandler, 
                                 SamplesHandler, 
                                 InteractiveHandler,
                                 AboutHandler)

app = webapp2.WSGIApplication([('/samples', SamplesHandler),
                               ('/interactive', InteractiveHandler),
                               ('/about', AboutHandler),
                               ('/.*', HomeHandler)],
                              debug=True)
