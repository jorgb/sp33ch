import os
import re
from uuid import uuid4
import sys

from flask import Flask, request, redirect, url_for, flash, abort, Response
from flask import render_template, jsonify
import wave
import requests
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['DEEPSPEECH_BASE'] = '/home/jorgb/deepspeech-0.5.1-models'

@app.route('/')
def index():
    return render_template('index.html', uuid=uuid4())

@app.route('/api/<id>/deepspeech')
def api_deepspeech(id):
    if not re.match("^[a-z0-9\-]+$", id):
        return abort(400)

    filename = os.path.join(app.config['UPLOAD_FOLDER'], '%s.wav' % id)
    args = "deepspeech --alphabet {0}/alphabet.txt --model {0}/output_graph.pbmm --lm {0}/lm.binary --trie {0}/trie --audio".format(app.config['DEEPSPEECH_BASE']).split(' ')
    args.append(filename)
    
    print("Running: " + args)
    
    result = subprocess.run(args, stdout=subprocess.PIPE)
    
    return jsonify({'text': str(result.stdout)})
    

@app.route('/upload', methods=['POST'])
def upload():
    if 'audio_file' not in request.files:
        return abort(400)
    
    file = request.files['audio_file']
    if file:
        id = uuid4()
        filename = "%s.wav" % id
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("Received: " + str(id))
        return str(id)
    
    return abort(400)


if __name__ == '__main__':
    #deep_model = load_model()   
    
    app.run(debug=True)
