from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import io, os, functions, magic

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'processed/'
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024
os.makedirs(os.path.join(app.instance_path, 'processed'), exist_ok=True)

@app.route('/')
@app.route('/index/')
def hello():
    return render_template('index.html')


@app.route('/test')
def download_and_remove():
    filename = 'photo_2023-02-09_13-44-51.jpg'
    path = os.path.join('processed', filename)

    mime = magic.Magic(mime=True)
    mimeType = mime.from_file(path)

    return send_file(path, mimetype=mimeType, as_attachment=True, download_name=filename)

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        message = request.form['message']
        f = request.files['file']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join('processed', filename))
            filePath = os.path.join('processed', filename)

            newFile = functions.hide_the_message(message, filename, filePath)

            path = os.path.join('processed', newFile)
            with open(path, 'rb') as image:
                image_content = image.read()
            mime = magic.Magic(mime=True)
            mimeType = mime.from_file(path)

            os.remove(os.path.join('processed', filename))
            response = send_file(io.BytesIO(image_content), mimetype=mimeType, as_attachment=True, download_name=newFile)

            os.remove(os.path.join('processed', newFile))
            return response

        return render_template('encode.html', message='Please upload a valid image file')

    return render_template('encode.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if (request.method == 'POST'):

        f = request.files['file']
        
        if f.filename != '':
            filename = secure_filename(f.filename)
            f.save(os.path.join('processed', filename))
            file = os.path.join('processed', filename)

            message = functions.find_the_message(file)
            os.remove(os.path.join('processed', filename))
            return render_template('decode.html', decodedMessage=message)

    return render_template('decode.html', decodedMessage='')

if __name__ == '__main__':
    app.run(debug=True)
