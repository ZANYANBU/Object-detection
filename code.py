from flask import Flask, Response, render_template
import cv2
import numpy as np
import subprocess
import sys

# Ensure necessary dependencies are installed
required_packages = ['torch', 'ultralytics', 'flask', 'opencv-python']
for package in required_packages:
    try:
        __import__(package)
    except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import torch
from ultralytics import YOLO

app = Flask(__name__)
model = YOLO('yolov5s.pt')

cap = cv2.VideoCapture(0)

def generate_frames():
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        results = model(frame)[0]
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            label = f"{model.names[cls]} {conf:.2f}"
            
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>YOLOv5 Object Detection</title>
    </head>
    <body>
        <h1>Live Object Detection</h1>
        <img src="/video_feed" width="720"/>
    </body>
    </html>
    '''

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
