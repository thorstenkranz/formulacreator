# -*- coding: utf-8 -*-
"""
Main handlers for this app
"""

import webapp2
import jinja2
import os
import urllib
import cgi

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),
                                                "../html_templates")))

from formulalib.rendering import render_formula

class HomeHandler(webapp2.RequestHandler):
    
    template = jinja_environment.get_template('home.html')
    template_values = {"title": "Formula Creator v0.1",
                       "version": "0.1",
                       "greeting" : "Willkommen!"}
    content_values = {}
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.template.render(self.template_values))

class SamplesHandler(webapp2.RequestHandler):    
    template = jinja_environment.get_template('samples.html')
    
    query_dicts = [{"formula":r"\sum_{i=1}^n \, i = \frac{n(n+1)}{2}"},
                     {"formula":r"test2"},
                     {"formula":r"E=mc^2",
                      "fontsize":"30"}
                    ]
    queries_raw = [cgi.escape("&".join(["%s=%s"%(k,d[k]) for k in d])) for d in query_dicts]
    queries_encoded = [urllib.urlencode(d) for d in query_dicts] 
    
    template_values = {"queries" : zip(queries_raw, queries_encoded),
                       "title": "Formula Creator v0.1",
                       "version": "0.1"}
               
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.template.render(self.template_values))

class FormulaHandler(webapp2.RequestHandler):
    def get(self):
        formula = self.request.get('formula') or "\sum_{i=1}^{10} i*(i+1)"
        fontsize = self.request.get('fontsize') or 12
        color = self.request.get('color') or "k"

        image_data = render_formula(formula, fontsize, color)

        self.response.headers['Content-Type'] = 'image/png'
        self.response.out.write(image_data)

