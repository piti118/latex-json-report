import jinja2
import os
import re
import subprocess
from tempfile import TemporaryDirectory
from os import path
import tempfile
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
    loader=jinja2.FileSystemLoader(os.path.abspath('.'))
)



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

latex_jinja_env.filters['escape_tex'] = escape_tex

template = latex_jinja_env.get_template('template.tex')
output = template.render(name="Piti")

#with TemporaryDirectory() as tempdir:
tempdir = tempfile.mkdtemp()
driver_file = path.join(tempdir,'template.tex')
print(driver_file)
with open(driver_file, 'w') as f:
    f.write(output)
subprocess.run(['xelatex', driver_file], cwd=tempdir)
print(tempdir)

#make temp dir
#write the file
#compile with xelatex
#get pdf
