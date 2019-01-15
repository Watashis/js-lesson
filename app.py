from flask import Flask, render_template, request, send_file
import requests, io

app = Flask(__name__, static_url_path='')
video = requests.get('https://r15---sn-gvnuxaxjvh-bvwz.googlevideo.com/videoplayback?source=youtube&nh=%2CIgpwcjAzLnN2bzAzKgkxMjcuMC4wLjE&requiressl=yes&mime=video%2Fmp4&ipbits=0&initcwndbps=920000&itag=22&lmt=1546305856255577&key=yt6&dur=567.217&txp=5535432&ip=109.169.201.172&sparams=dur%2Cei%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&ratebypass=yes&fvip=15&c=WEB&id=o-AOrNjTKkZNwWC6M0m4KwZafA6c1lcWSnDSdB-3FeGAD4&mm=31%2C26&mn=sn-gvnuxaxjvh-bvwz%2Csn-axq7sn7l&mt=1547560865&mv=m&pl=18&ei=zOo9XMOjLN3j7QTa17aIBA&ms=au%2Conr&expire=1547583276&signature=65D47FB35E7E9B96D59E766B09E1B317F77C2E21.0CB306912A25326FAA081330CA1DB2B364F87820&title=%D0%9F%D0%A0%D0%90%D0%92%D0%9E%20%D0%9D%D0%90%20%D0%9F%D0%A0%D0%90%D0%97%D0%94%D0%9D%D0%98%D0%9A%20-%20%D0%90%D0%9D%D0%98%D0%9C%D0%90%D0%A6%D0%98%D0%AF', stream=True).content
video = io.BytesIO(video)
@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/test.mp4')
def test():
    return send_file(video, mimetype='video/mp4')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
