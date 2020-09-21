import os
from app import app
from flask import render_template, make_response
from flask import Flask, flash, request, redirect, url_for
import librosa

import matplotlib.pyplot as plt
import librosa.display

UPLOAD_FOLDER = 'temp/'
ALLOWED_EXTENSIONS = {'mp3'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def uploaded_file():
    r1 = make_response(render_template('index.html'))
    r1.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r1.headers["Pragma"] = "no-cache"
    r1.headers["Expires"] = "0"
    r1.headers['Cache-Control'] = 'public, max-age=0'
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename 
            # if os.path.exists("graph_temp.png"):
            #     os.remove("graph_temp.png")
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            audio_data = UPLOAD_FOLDER + filename
            x , sr = librosa.load(audio_data)
            plt.figure(figsize=(14, 2))
            librosa.display.waveplot(x, sr=sr)
            plt.savefig('static/graph_temp.png')
            plt.close()
            os.remove(f"temp/{filename}")
            print("new")
            return render_template('graph.html', fn=filename)

    return r1

