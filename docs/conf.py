
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Project: Market Microstructure and Trading Systems Official Repository                              -- #
# -- File: config.py scritp for redthedocs process configuration and deploy                              -- #
# -- Author: IFFranciscoME - franciscome@iteso.mx                                                        -- #
# -- License: Private                                                                                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

# ------------------------------------------------------------------------------------------- Path setup -- # 
# --------------------------------------------------------------------------------------------------------- #

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Add the local code to the Python path, so docs are generated for current working copy
rundir = os.path.dirname(__file__)
sys.path.insert(0, rundir[:-4]) # remove '/doc' from end of path

# The master toctree document..
master_doc = 'index'
source_suffix = '.rst'

# ----------------------------------------------------------------- Local Debug or readthedocs.io deploy -- #
# --------------------------------------------------------------------------------------------------------- #

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# only import and set the theme if we're building docs locally
if not on_rtd:
    try:
        import sphinx_rtd_theme
        html_theme = 'sphinx_rtd_theme'
        html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    except:
        pass

# ---------------------------------------------------------------------------------- Project information -- #
# --------------------------------------------------------------------------------------------------------- #

project = 'MyST'
copyright = '2021, IFFranciscoME'
author = 'IFFranciscoME'
release = 'v0.1'
version = 'v0.1'

# -------------------------------------------------------------------------------- General configuration -- #
# --------------------------------------------------------------------------------------------------------- #

# Add any Sphinx extension module names here
extensions = ['sphinx.ext.autosummary',
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode']

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

# Hide the "Edit on GitHub" or "View page source" links
html_context = {'display_github': False, 'show_source': False, 'html_show_sourcelink': False}

# Options on rendering docstrings from functions
todo_include_todos = True
napoleon_google_docstring = False
napoleon_include_special_with_doc = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}


# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# ------------------------------------------------------------------------------ Options for HTML output -- #
# --------------------------------------------------------------------------------------------------------- #

# The theme to use for HTML and HTML Help pages. 
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# List of directories, relative to source directories, that shouldn't be searched for source files.
exclude_dirs = ['images', 'scripts']

# Layout base options for theme
html_theme_options = {'logo_only': True, 'display_version': False, 'style_nav_header_background': '#2bbcf3'}

# ----------------------------------------------------------------------------- Options for LaTeX output -- #
# --------------------------------------------------------------------------------------------------------- #

# The font size ('10pt', '11pt' or '12pt')
latex_elements = {'pointsize': '12pt'}

# Important stuff for the LaTeX preamble.
latex_elements['preamble'] =  '\\usepackage{xcolor}\n'+\
                              '\\usepackage{amsmath}\n'+\
                              '\\usepackage{mathtools}\n'+\
                              '\\usepackage{amsfonts}\n'+\
                              '\\usepackage{amssymb}\n'+\
                              '\\usepackage{dsfont}\n'
