# -*- coding: utf-8 -*-
"""
Method for rendering a latex-style formula string to an image
"""
import cStringIO
import matplotlib.pyplot as plt

def render_formula(formula, fontsize=12, color="k"):
    plt.clf()
    fig = plt.figure(figsize=(4,2))
    mpl_text = r"$%s$" % formula
    txt = plt.figtext(0.5,0.5,mpl_text,va="center", ha="center", fontsize=fontsize, color=color)
    fig.canvas.draw()
    bbox = txt.get_window_extent()
    fig.set_figheight( 1.1 * bbox.height / fig.dpi )
    fig.set_figwidth( 1.1* bbox.width / fig.dpi ) 
    sio = cStringIO.StringIO()
    plt.savefig(sio, format="png")
    return sio.getvalue()
    
