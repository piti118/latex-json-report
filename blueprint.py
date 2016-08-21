from jinja2 import TemplateNotFound
from flask import Flask, Blueprint, request, jsonify, send_file, current_app
from tempfile import TemporaryDirectory


def make_blueprint(name, module):

    ret = Blueprint(name, module.__name__)
    template = module.template()

    def compile_with_data(data):
        with TemporaryDirectory() as tempdir:
            current_app.logger.info('Working on %s' % tempdir)
            pdf = template.compile(data, tempdir)
            return send_file(pdf,
                             as_attachment=False,
                             attachment_filename='basic.pdf')

    @ret.route('/')
    def show_report():
        if request.is_json:
            data = request.get_json()
            return compile_with_data(data)
        else:
            return jsonify(error=400, message='Body is not valid json'), 400

    @ret.route('/sample')
    def show_sample():
        return compile_with_data(template.sample_data())

    return ret
