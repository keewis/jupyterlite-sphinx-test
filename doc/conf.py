# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'example'
copyright = '2026, devs'
author = 'devs'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "jupyterlite_sphinx",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "_contents"]
root_doc = "index"

autosummary_generate = True
napoleon_google_docstring = False
napoleon_numpy_docstring = True

global_enable_try_examples = True
try_examples_global_button_text = "Try it in your browser!"
try_examples_global_warning_text = "Interactive examples are experimental and may not always work as expected."

try_examples_preamble = """
import numpy as np

np.random.seed(0)
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
