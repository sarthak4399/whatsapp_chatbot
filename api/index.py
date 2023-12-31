# app.py
from flask import Flask, request, jsonify
import cloudinary
from cloudinary.uploader import upload

app = Flask(__name__)
cloudinary.config(
    cloud_name='',
    api_key='',
    api_secret=''
)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo attached'}), 400
    photo = request.files['photo']
    if photo.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if photo and allowed_file(photo.filename):
        result = upload(photo)
        public_url = result['secure_url']
        return jsonify({'public_url': public_url}), 200
    return jsonify({'error': 'Invalid file format'}), 400


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=60000)
