
# -- --------------------------------------------------------------------------------------------------- -- #
# -- MAF1731 - MICROSTRUCTURE AND TRADING SYSTEMS                                                        -- #
# -- conf.py: python configuration file to compile documentation                                         -- #
# -- Author: IFFranciscoME - if.francisco.me@gmail.com                                                   -- #
# -- License: MIT License                                                                                -- #
# -- Repository: https://github.com/iffranciscome/myst/                                                  -- #
# -- --------------------------------------------------------------------------------------------------- -- #

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
              'jupyter_sphinx']

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

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# List of directories, relative to source directories, that shouldn't be searched for source files.
exclude_dirs = ['images', 'scripts']

# The master toctree document..
master_doc = 'index'
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# ------------------------------------------------------------------------------ Options for HTML output -- #
# --------------------------------------------------------------------------------------------------------- #

# The theme to use for HTML and HTML Help pages. 
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# ----------------------------------------------------------------------------- Options for LaTeX output -- #
# --------------------------------------------------------------------------------------------------------- #

latex_elements = {
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
