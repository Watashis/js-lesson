from flask import Flask, render_template, request, send_file

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html', title='Home')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
