from flask import Flask, render_template, request, send_file
import requests, io

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/test')
def test():
    video = requests.get('https://vjs.zencdn.net/v/oceans.mp4', stream=True).content
    video = io.BytesIO(video)
    return send_file(video, mimetype='video/mp4')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
