# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'assignment_2_2023'
copyright = '2024, Emanuele Bua Odetti'
author = 'Emanuele Bua Odetti'
release = '1.0'

import os 
import subprocess 
import sys 
sys.path.insert(0, os.path.abspath('../'))
#subprocess.call('doxygen ../Doxyfile.in', shell=True)
show_authors = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [ 
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              "sphinx.ext.napoleon",
              'sphinx.ext.inheritance_diagram',
              'breathe' 
              ]

templates_path = ['_templates']
exclude_patterns = []

highlight_language = 'python3'
source_suffix = '.rst' 
master_doc = 'index' 
html_theme ='sphinx_rtd_theme'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
# intersphinx_mapping = {'python':('https://docs.python.org/3', None)}
# todo_include_todos = True
# breathe_projects = { "assignment_2_2023": "../build/xml/" }

# breathe_default_project = "assignment_2_2023"
# breathe_default_members = ('members', 'undoc-members')
