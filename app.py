import jinja2
import os
import re
import subprocess
from tempfile import TemporaryDirectory
from os import path
import tempfile
from flask import Flask
from flask import Flask, request, jsonify, send_file
import werkzeug

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

def make_pdf(data, tempdir):
    # evaluate template
    template = latex_jinja_env.get_template('template.tex')
    output = template.render(**data)

    # write output to file ready to compile
    driver_file = path.join(tempdir, 'template.tex')
    with open(driver_file, 'w') as f:
        f.write(output)

    # compile
    out = subprocess.run(['xelatex', driver_file],
                         cwd=tempdir,
                         stdout=subprocess.PIPE)

    if out.returncode == 0:
        return path.join(tempdir, 'template.pdf')
    else:
        raise Exception('Fail to compile: ' + out.stdout.decode('utf-8'))

app = Flask(__name__)
app.config.update(PROPAGATE_EXCEPTIONS=True, DEBUG=True)
@app.route('/report', methods=['POST'])
def report():
    print('helllllo', request.is_json)
    if request.is_json:
        data = request.get_json()
        with TemporaryDirectory() as tempdir:
            app.logger.info('working on %s' % tempdir)
            pdf = make_pdf(data, tempdir)
            return send_file(pdf,
                as_attachment=True,
                attachment_filename='report.pdf')
    else:
        return jsonify(error=400, message='Body is not valid json'), 400

# template = latex_jinja_env.get_template('template.tex')
# output = template.render(name="Piti")
#
# #with TemporaryDirectory() as tempdir:
# tempdir = tempfile.mkdtemp()
# driver_file = path.join(tempdir,'template.tex')
# print(driver_file)
# with open(driver_file, 'w') as f:
#     f.write(output)
# subprocess.run(['xelatex', driver_file], cwd=tempdir)
# print(tempdir)

#make temp dir
#write the file
#compile with xelatex
#get pdf
