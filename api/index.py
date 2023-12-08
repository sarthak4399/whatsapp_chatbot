# app.py
from flask import Flask, request, jsonify
import cloudinary
from cloudinary.uploader import upload

app = Flask(__name__)


cloudinary.config(
    cloud_name='doerkgxce',
    api_key='166618279153227',
    api_secret='R2f4f3IH1U0nmsZ5iKrzUX6EGTM'
)


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'photo' not in request.files:
        return jsonify({'error': 'No photo attached'}), 400

    photo = request.files['photo']

    if photo.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if photo and allowed_file(photo.filename):
        # Upload the photo to Cloudinary
        result = upload(photo)
        public_url = result['secure_url']
        return jsonify({'public_url': public_url}), 200

    return jsonify({'error': 'Invalid file format'}), 400


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}


if __name__ == '__main__':
    app.run(host='0.0.0.0')
