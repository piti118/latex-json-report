
from latex_jinja import latex_jinja
import latex_compiler
from tempfile import TemporaryDirectory
from os import path
import tempfile
from flask import Flask
from flask import Flask, request, jsonify, send_file
import werkzeug
from templates import sample_template

def make_pdf(data, tempdir):
    t = sample_template.SampleTemplate()
    return t.compile(data, tempdir)

app = Flask(__name__)
app.debug = True
app.config.update(PROPAGATE_EXCEPTIONS=True, DEBUG=True)
@app.route('/report', methods=['POST'])
def report():
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
