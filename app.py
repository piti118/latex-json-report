
from latex_jinja import latex_jinja
import latex_compiler
from tempfile import TemporaryDirectory
from os import path
import tempfile
from flask import Flask
from flask import Flask, request, jsonify, send_file
import werkzeug
from templates import sample_template, ultimate_sample_template

basic_template = sample_template.SampleTemplate()
ultimate_template = ultimate_sample_template.UltimateSampleTemplate()

app = Flask(__name__)
app.debug = True
app.config.update(PROPAGATE_EXCEPTIONS=True, DEBUG=True)


@app.route('/basic', methods=['POST'])
def basic():
    if request.is_json:
        data = request.get_json()
        with TemporaryDirectory() as tempdir:
            app.logger.info('working on %s' % tempdir)
            pdf = basic_template.compile(data, tempdir)
            return send_file(pdf,
                             as_attachment=True,
                             attachment_filename='basic.pdf')
    else:
        return jsonify(error=400, message='Body is not valid json'), 400

@app.route('/ultimate', methods=['POST'])
def report():
    if request.is_json:
        data = request.get_json()
        with TemporaryDirectory() as tempdir:
            app.logger.info('working on %s' % tempdir)
            pdf = ultimate_template.compile(data, tempdir)
            return send_file(pdf,
                             as_attachment=True,
                             attachment_filename='ultimate.pdf')
    else:
        return jsonify(error=400, message='Body is not valid json'), 400
