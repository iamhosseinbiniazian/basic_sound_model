# This is a _very simple_ example of a web service that recognizes faces in uploaded images.
# Upload an image file and it will check if the image contains a picture of Barack Obama.
# The result is returned as json. For example:
#
# $ curl -F "file=@obama2.jpg" http://127.0.0.1:5001
#
# Returns:
#
# {
#  "face_found_in_image": true,
#  "is_picture_of_obama": true
# }
#
# This example is based on the Flask file upload example: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/

# NOTE: This example requires flask to be installed! You can install it with pip:
# $ pip3 install flask

from PyAudio import audioBasicIO as aIO
from PyAudio import audioTrainTest as aT
from PyAudio import audioSegmentation as aS
from flask import Flask, jsonify, request, redirect,json
import scipy
import cv2
import data
# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'WAV', 'mp3', 'wav'}

app = Flask(__name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return detect_faces_in_image(file)

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


def detect_faces_in_image(file_stream):
    # Load the uploaded image file
    #img = face_recognition.load_image_file(file_stream)
    #[Fs, x] = aIO.readAudioFile(file_stream)
    [Fs, x]=scipy.io.wavfile.read(file_stream)
    filename="h.WAV"
    scipy.io.wavfile.write(filename, Fs, x)
    # Get face encodings for any faces in the uploaded image
    #unknown_face_encodings = face_recognition.face_encodings(img)

    #face_found = False
    #is_obama = False

    #if len(unknown_face_encodings) > 0:
        #face_found = True
        # See if the first face in the uploaded image matches the known face of Obama
        #match_results = face_recognition.compare_faces([known_face_encoding], unknown_face_encodings[0])
        #if match_results[0]:
            #is_obama = True
    [flagsInd, classesAll, acc, CM] = aS.mtFileClassification(filename, "svmModel", "svm",True)
    # Return the result as json
    data=cv2.imread("Accplot.jpeg")
    result = {
        "flagsInd": str(flagsInd),
        "classesAll":str(classesAll),
        "accuracy":str(acc),
        "CM":str(CM),
        "Picture":str(data).encode('latin-1')
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)