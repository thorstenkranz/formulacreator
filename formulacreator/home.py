#! /usr/bin/python

import webapp2

from formulalib.handlers import HomeHandler

app = webapp2.WSGIApplication([('/.*', HomeHandler)],
                              debug=True)
