# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys
sys.path.insert(0, os.path.abspath('..'))
autodoc_mock_imports = ["aiohttp"]

# -- Project information -----------------------------------------------------

project = 'Antiland'
copyright = '2023, TheUnsocialEngineer'
author = 'TheUnsocialEngineer'

# The full version, including alpha/beta/rc tags
release = '0.94'

autodoc_member_order = 'groupwise'
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]
version = ''
with open('../Antiland/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
# This assumes a tag is available for final releases
branch = 'master' if version.endswith('a') else 'v' + version
resource_links = {
  'issues': 'https://github.com/TheUnsocialEngineer/Antiland/issues',   
  'discussions': 'https://github.com/TheUnsocialEngineer/Antiland/discussions',
  'examples': f'https://github.com/TheUnsocialEngineer/Antiland/tree/{branch}/examples',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_favicon = 'antiland_logo.ico'

import sys; sys.setrecursionlimit(5000)

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']