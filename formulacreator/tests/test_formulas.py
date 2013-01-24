# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:26:26 2013

@author: thorsten
"""

import sys
from os.path import dirname, abspath, join
module_dir = dirname(__file__)
sys.path.append(abspath(dirname(module_dir)))
import matplotlib
matplotlib.use("Agg")

from formulalib.rendering import render_formula

def test_simpleformula():
    formulas = [
		r"\sum_{i=1}^{n}\, i = \frac{n(n+1)}{2}",
		r"\int_x^X f(t)dt",
		r"E = mc^2"]
    for i, formula in enumerate(formulas):
        yield _render_formula_to_file, i, formula
        
def _render_formula_to_file(idx, formula):
    img_data = render_formula(formula)
    with open(join(module_dir, "output/result%i.png"%idx), "wb") as f:
        f.write(img_data)    
    
