import validators
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def root():
    return ''


@app.route('/<shortened_url>', methods=['GET'])
def get_shortened_url(shortened_url):
    return ''


@app.route('/shorten_url', methods=['POST'])
def shorten_url():
    is_valid, error_response = is_valid_post_request(request)

    if not is_valid:
        return error_response

    return jsonify({"shortened_url": "placeholder"}), 201


def is_valid_post_request(request):
    # Make sure that the request header was set correctly and
    # that the request contains json body
    if not request.is_json or request.get_json(False, True, True) is None:
        return False, generate_error_msg("Your request should contain valid json body")

    url = request.get_json().get('url', '')

    if url == '':
        return False, generate_error_msg("Please provide a url to be shortened")

    if not validators.url(url):
        return False, generate_error_msg("Please provide a valid url")

    return True, None


def generate_error_msg(msg):
    return jsonify({"error_message": msg}), 400
