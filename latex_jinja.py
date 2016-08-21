__all__ = ['latex_jinja']

import jinja2
import os
import re

LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"'), r"''"),
    (re.compile(r'\.\.\.+'), r'\\ldots'),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval

def latex_jinja(template_path):
    latex_jinja_env = jinja2.Environment(
        block_start_string='((*',
        block_end_string='*))',
        variable_start_string='(((',
        variable_end_string=')))',
        comment_start_string='((=',
        comment_end_string='=))',
        line_statement_prefix='%%',
        line_comment_prefix='%#',
        trim_blocks=True,
        autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.abspath(template_path))
    )
    
    latex_jinja_env.filters['escape_tex'] = escape_tex
    return latex_jinja_env
