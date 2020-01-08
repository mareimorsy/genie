from app import app
from flask import render_template, jsonify, request
from app.helpers.k8s.deployment import get_pods, pod_cmd
import  json
from flask import session
from app.config import config

@app.route('/api/namespaces')
def namespaces():
    return render_template("index.html")

@app.route('/api/pod/exec', methods=['GET', 'POST'])
def pod_exec():

	pod = request.get_json()

	# return jsonify(request.get_json())
	return pod_cmd(pod["name"], pod["namespace"], pod["command"])


@app.route('/api/pod')
def pod():
    return render_template("mocks/pods.json")



@app.route('/api/pods')
def pods():
    return jsonify(get_pods(config))