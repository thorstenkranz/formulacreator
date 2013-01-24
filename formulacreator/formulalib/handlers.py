# -*- coding: utf-8 -*-
"""
Main handlers for this app
"""

import webapp2
import jinja2
import os
import urllib
import cgi
import random

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),
                                                "../html_templates")))

from formulalib.rendering import render_formula

class SiteHandler(webapp2.RequestHandler):
    menu_items = [("Home","index"),
                  ("Samples","samples"),
                  ("Interactive","interactive"),
                  ("About","about")]
                  
    def __init__(self, *args, **kwargs):
        super(SiteHandler, self).__init__(*args, **kwargs)
        self.template_values = {
                "title": "Formula Creator v0.1",
                "menu_items" : self.menu_items,
                "version": "0.1"}

class HomeHandler(SiteHandler):
    """Used for home page"""
    template = jinja_environment.get_template('home.html')    
    greetings = ["Welcome!",
                 "Willkommen!",
                 "Bienvenido!",
                 "Bien venue!",
                 "Welkom!",
                 "Benvenuto!"
                 ]
    
    def __init__(self, *args, **kwargs):
        super(HomeHandler, self).__init__(*args, **kwargs)
        self.template_values["greeting"] = random.choice(self.greetings)
        
    def get(self):
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.template.render(self.template_values))

class SamplesHandler(SiteHandler):    
    """Used to show samples"""
    template = jinja_environment.get_template('samples.html')
    
    query_dicts = [{"formula":r"\sum_{i=1}^n \, i = \frac{n(n+1)}{2}"},
                     {"formula":r"test2"},
                     {"formula":r"E=mc^2",
                      "fontsize":"30"},
                     {"formula":r"E=mc^2",
                      "color":"blue"},
                     {"formula":r"E=mc^2",
                      "fontsize":"80",
                      "color": "lightgray"}
                    ]
    queries_raw = [cgi.escape("&".join(["%s=%s"%(k,d[k]) for k in d])) for d in query_dicts]
    queries_encoded = [urllib.urlencode(d) for d in query_dicts] 
    
    def __init__(self, *args, **kwargs):
        super(SamplesHandler, self).__init__(*args, **kwargs)
        self.template_values["greeting"] = "Willkommen!"
        self.template_values["queries"] = zip(self.queries_raw, self.queries_encoded)
               
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.template.render(self.template_values))

class InteractiveHandler(SiteHandler):
    """Interactive designer."""
    template = jinja_environment.get_template('interactive.html')    
        
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.template.render(self.template_values))
        
class AboutHandler(SiteHandler):
    """Interactive designer."""
    template = jinja_environment.get_template('about.html')    
        
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

