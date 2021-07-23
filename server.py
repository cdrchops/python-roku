from flask import Flask, render_template, request, jsonify, json, make_response, Response, send_from_directory
# some code from https://www.pyimagesearch.com/2019/09/02/opencv-stream-video-to-web-browser-html-page/

from flask_cors import CORS, cross_origin

import jinja2

from roku import Roku

app = Flask(__name__)

roku = Roku('192.168.0.3')

appList = []

for appz in roku.apps:
    appList.append(appz.name)

@app.route('/')
def index():
    #send a list of apps to the page to be used in a dropdown
    return render_template('index.html', appList=appList)

@app.route("/keypress/<key>")
def keypress(key):
    pass

# @app.route("/launch/<code>")
# def launch(code):
#     request.args.get("contentID", None)

@app.route("/query/apps")
def list_apps():
    pass

@app.route("/query/active-app")
def active_app():
    pass

@app.route("/query/icon/<app_id>")
def app_icon(app_id):
    pass

@app.route("/launchApp")
def launchApp():
    appParameter = request.args.get('app_name')#, "", type=str)
    appToLaunch = roku[appParameter]
    appToLaunch.launch()

    return jsonify(result="success", status="success")

@app.route("/play")
def play():
    roku.play()
    return jsonify(result="success", status="success")

@app.route("/pause")
def pause():
    roku.select()
    return jsonify(result="success", status="success")

@app.route("/ffwd")
def ffwd():
    roku.forward()
    return jsonify(result="success", status="success")

@app.route("/rwd")
def rwd():
    roku.reverse()
    return jsonify(result="success", status="success")

@app.route("/back")
def back():
    roku.back()
    return jsonify(result="success", status="success")

@app.route("/home")
def home():
    roku.home()
    return jsonify(result="success", status="success")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
