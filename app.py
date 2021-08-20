from flask import Flask 
import speechbrain as sb
from speechbrain.dataio.dataio import read_audio
from IPython.display import Audio

from speechbrain.pretrained import SpeakerRecognition
import os
import wave
from scipy.io import wavfile
from pydub import AudioSegment

import os
from flask import Flask, render_template, session, request, redirect, flash, Response
from werkzeug.utils import secure_filename
import tempfile
import base64
from werkzeug.utils import secure_filename
import chardet
import json
import requests

app = Flask(__name__)
uploads_dir = os.path.join(app.instance_path, 'uploaded')
os.makedirs(uploads_dir, exist_ok=True)




def savefiletolocal(uploaded_file,some_bytes):
    binary_file = open(uploaded_file, "wb")
  
    # Write bytes to file
    binary_file.write(some_bytes)
  
    # Close file
    binary_file.close()

@app.route('/')
def upload_file():
   return render_template('home.html')


@app.route('/uploader',methods=['POST'])
def verification():
    verification = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
    audioFile1 = request.files['file1']
    audioFile1.save(os.path.join(uploads_dir, secure_filename(audioFile1.filename)))
    audioFile2 = request.files['file2']
    
    audioFile2.save(os.path.join(uploads_dir, secure_filename(audioFile2.filename)))

    score, prediction = verification.verify_files(os.path.join(uploads_dir, secure_filename(audioFile1.filename)), os.path.join(uploads_dir, secure_filename(audioFile2.filename)))
    score = str(score)
    prediction = str(prediction)
    print(prediction)
    return prediction 
   
    





if __name__ == '__main__':
    app.debug = True
    app.run()
