"""
Stephen's Flask API.
"""
import os
import configparser
from flask import Flask, send_from_directory, send_file, abort

app = Flask(__name__)

# Stolen from project 0
def parse_config(config_paths):
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    config = configparser.ConfigParser()
    config.read(config_path)
    return config

@app.errorhandler(404)
def error404(error):
    return send_file('pages/404.html'), 404

@app.errorhandler(403)
def error403(error):
    return send_file('pages/403.html'), 403

@app.route("/<path:path>")
def hello(path):
    if ".." in path or '~' in path:
        abort(403)
    return send_from_directory('pages', path)

if __name__ == "__main__":
    config = parse_config(["credentials.ini", "default.ini"])
    app.run(debug=config["SERVER"]["DEBUG"], host='0.0.0.0', port=config["SERVER"]["PORT"])
