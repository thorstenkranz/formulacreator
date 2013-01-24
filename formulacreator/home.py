#! /usr/bin/python

import webapp2

from formulalib.handlers import HomeHandler, SamplesHandler

app = webapp2.WSGIApplication([('/samples', SamplesHandler),('/.*', HomeHandler)],
                              debug=True)
