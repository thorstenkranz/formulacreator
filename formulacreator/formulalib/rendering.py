# -*- coding: utf-8 -*-
"""
Method for rendering a latex-style formula string to an image
"""
import cStringIO
import re
try:
    import matplotlib.pyplot as plt
except AttributeError:
    plt = None #For testing app locally, won't plot anything

purger = None

def render_formula(formula, fontsize=12, color="k"):
    global purger
    if purger is None:
        purger = FormulaPurger()
    plt.clf()
    fig = plt.figure(figsize=(4,2))
    mpl_text = r"$%s$" % purger(formula)
    txt = plt.figtext(0.5,0.5,mpl_text,va="center", ha="center", fontsize=fontsize, color=color)
    fig.canvas.draw()
    bbox = txt.get_window_extent()
    fig.set_figheight( 1.1 * bbox.height / fig.dpi )
    fig.set_figwidth( 1.1* bbox.width / fig.dpi ) 
    sio = cStringIO.StringIO()
    plt.savefig(sio, format="png")
    return sio.getvalue()

class FormulaPurger(object):
    """Class for removing control characters from formulas.
    As re_control_characters is class-variable, it has to be compiled only once."""
    
    re_control_characters = re.compile("[\n|\t|\r]")
    
    def __call__(self, formula):
        return self.re_control_characters.sub("",formula)    
