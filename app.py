from latex_jinja import latex_jinja
import latex_compiler
from tempfile import TemporaryDirectory
from os import path
import tempfile
from flask import Flask, request, jsonify, send_file
import werkzeug
from templates import basic_template, ultimate_template, shipping_label_template
from blueprint import make_blueprint

app = Flask(__name__)
app.config.update(PROPAGATE_EXCEPTIONS=True)


@app.route('/ping')
def ping():
    return jsonify("pong")

basic_blueprint = make_blueprint('sample', basic_template)
app.register_blueprint(basic_blueprint, url_prefix='/basic')

ultimate_blueprint = make_blueprint('ultimate', ultimate_template)
app.register_blueprint(ultimate_blueprint, url_prefix='/ultimate')

shipping_label_blueprint = make_blueprint('shipping_label', shipping_label_template)
app.register_blueprint(shipping_label_blueprint, url_prefix='/shipping-label')


@app.errorhandler(Exception)
def handle_invalid_usage(error):
    app.logger.error(error)
    return 'Something wrong', 400


app.run(host='0.0.0.0')
