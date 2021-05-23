# -- --------------------------------------------------------------------------------------------------- -- #
# -- MICROSTRUCTURE AND TRADING SYSTEMS                                                                  -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- License: GPL-3.0 License                                                                            -- #
# -- Repository: https://github.com/iffranciscome/MAF1731-MyST                                           -- #
# -- --------------------------------------------------------------------------------------------------- -- #

# -- Configuration file for the Sphinx documentation builder

# ------------------------------------------------------------------------------------------- Path setup -- # 
# --------------------------------------------------------------------------------------------------------- #

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# ---------------------------------------------------------------------------------- Project information -- #
# --------------------------------------------------------------------------------------------------------- #

project = 'MyST'
copyright = '2021, IFFranciscoME'
author = 'IFFranciscoME'
release = 'v0.0.1'
version = '0.0.1'

# -------------------------------------------------------------------------------- General configuration -- #
# --------------------------------------------------------------------------------------------------------- #

# Add any Sphinx extension module names here
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.doctest',
              'sphinx.ext.napoleon',
              'sphinx.ext.intersphinx']

todo_include_todos = True
napoleon_google_docstring = False
napoleon_include_special_with_doc = False

# To support multiple sphinx version without having warning.
try:
    from sphinx.ext import imgmath
    extensions.append('sphinx.ext.imgmath')
except ImportError:
    try:
        from sphinx.ext import pngmath
        extensions.append('sphinx.ext.pngmath')
    except ImportError:
        pass

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# List of directories, relative to source directories, that shouldn't be
# searched for source files.
exclude_dirs = ['images', 'scripts']

# The master toctree document..
master_doc = 'index'
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# ------------------------------------------------------------------------------ Options for HTML output -- #
# --------------------------------------------------------------------------------------------------------- #

# The theme to use for HTML and HTML Help pages
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets)
# html_static_path = ['_static']

# ----------------------------------------------------------------------------- Options for LaTeX output -- #
# --------------------------------------------------------------------------------------------------------- #

latex_elements = {
    # The paper size ('letter' or 'a4').
    'latex_paper_size': 'letter',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt',
}

# Important stuff for the LaTeX preamble.
latex_elements['preamble'] =  '\\usepackage{xcolor}\n'+\
                              '\\usepackage{amsmath}\n'+\
                              '\\usepackage{mathtools}\n'+\
                              '\\usepackage{amsfonts}\n'+\
                              '\\usepackage{amssymb}\n'+\
                              '\\usepackage{dsfont}\n'
