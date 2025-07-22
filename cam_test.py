from flask import Flask, Response
from picamera2 import Picamera2
import time

app = Flask(__name__)
camera = Picamera2()
camera.configure(camera.create_video_configuration(main={"size": (640, 480)}))
camera.start()

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>Raspberry Pi Camera Stream</h1>
            <img src="/video_feed">
        </body>
    </html>
    '''

def gen():
    while True:
        frame = camera.capture_array()
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001, threaded=True)
