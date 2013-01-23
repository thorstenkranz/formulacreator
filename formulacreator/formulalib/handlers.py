# -*- coding: utf-8 -*-
"""
Main handlers for this app
"""

import webapp2
#import numpy as np
import cStringIO
import matplotlib.pyplot as plt

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
        plt.clf()
        plt.figure(figsize=(4,2))
        formula = self.request.get('formula') or "\sum_{i=1}^{10} i*(i+1)"
        mpl_text = r"$%s$" % formula
        fontsize = self.request.get('fontsize') or 12
        color = self.request.get('color') or "k"

        plt.figtext(0,0.5,mpl_text,va="center", ha="left", fontsize=fontsize, color=color)
        sio = cStringIO.StringIO()
        plt.savefig(sio, format="png")
        self.response.headers['Content-Type'] = 'image/png'

        self.response.out.write(sio.getvalue())

