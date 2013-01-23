#! /usr/bin/python

import webapp2

from formulalib.handlers import FormulaHandler

app = webapp2.WSGIApplication([('/formula/.*', FormulaHandler)],
                              debug=True)
