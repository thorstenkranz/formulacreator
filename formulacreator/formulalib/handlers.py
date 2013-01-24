# -*- coding: utf-8 -*-
"""
Main handlers for this app
"""

import webapp2
#import numpy as np
import matplotlib.pyplot as plt

from formulalib.rendering import render_formula

class HomeHandler(webapp2.RequestHandler):
    site_html = """<html>
<head><title>FORMULA CREATOR</title></head>
<body><h1 align="center">Welcome!</h1></body>
</html>"""
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(self.site_html)

class FormulaHandler(webapp2.RequestHandler):
    def get(self):
        formula = self.request.get('formula') or "\sum_{i=1}^{10} i*(i+1)"
        fontsize = self.request.get('fontsize') or 12
        color = self.request.get('color') or "k"

        image_data = render_formula(formula, fontsize, color)

        self.response.headers['Content-Type'] = 'image/png'
        self.response.out.write(image_data)

