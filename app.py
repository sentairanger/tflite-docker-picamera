from flask import Flask, request, render_template, Response, jsonify
from camera_setup import *
from classify_image import *
import logging
from time import sleep

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/capture", methods=['POST'])
def capture_image():
    try:
        take_photo()
        sleep(1)
        return jsonify(success=True, message="Photo captured successfully")
    except Exception as ex:
        return jsonify(success=False, message=str(ex))

@app.route("/videofeed")
def videofeed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/classify", methods=['POST'])
def classifing_image():
    try:
        classify_string = str(show_results())
        return jsonify(success=True, message=str(classify_string))
    except Exception as ex:
        return jsonify(success=False, message=str(ex))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_stream()
    app.run(host="0.0.0.0")