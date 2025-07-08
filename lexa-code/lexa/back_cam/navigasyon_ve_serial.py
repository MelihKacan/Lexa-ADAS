import cv2
import serial
import serial.tools.list_ports
import requests
import json
import time
import math

image = cv2.imread("./back_cam/a.png")
height, width, _ = image.shape

visited_pixels = []

def find_mega2560_port():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if 'Arduino Mega' in port.description or '2560' in port.description:
            return port.device
    return None

port = find_mega2560_port()
arduino = serial.Serial(port, baudrate=9600, timeout=1)

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_pixel_loop(x, y, threshold=1.2):
    for px, py in visited_pixels:
        if distance((x, y), (px, py)) < threshold:
            return True
    return False

def clear_visited():
    global visited_pixels
    visited_pixels = []

def gen_frames():
    tur = 0
    box_size = 4

    while True:
        frame = image.copy()
        raw_line = arduino.readline().strip()
        json_str = raw_line.decode("utf-8", errors="ignore")
        
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError:
            continue

        enlem = data.get("enlem")
        boylam = data.get("boylam")

        if not enlem or not boylam:
            continue

        print(enlem, boylam)

        test_lat = float(enlem)
        test_lon = float(boylam)

        pixel_x = int(map_value(test_lon, 35.496466, 35.500816, 0, 810))
        pixel_y = int(map_value(test_lat, 38.734594, 38.733163, 0, 344))

        if check_pixel_loop(pixel_x, pixel_y):
            tur += 1
            print(f"Tur: {tur}")
            clear_visited()
        else:
            visited_pixels.append((pixel_x, pixel_y))

        requests.post('http://127.0.0.1:8000/back_cam/post_request', data={
            "hiz": data.get("hiz"),
            "sabitonoff": data.get("sabitonoff"),
            "far": data.get("far"),
            "gerivites": data.get("geri"),
            "tur": tur,
            "engelsolbir": data.get("engelsolbir"),
            "engelsoliki": data.get("engelsoliki"),
            "engelsoluc": data.get("engelsoluc"),
            "engelsagbir": data.get("engelsagbir"),
            "engelsagiki": data.get("engelsagiki"),
            "engelsaguc": data.get("engelsaguc"),
        })

        for i in range(1, len(visited_pixels)):
            cv2.line(frame, visited_pixels[i-1], visited_pixels[i], (125, 125, 125), 2)

        cv2.rectangle(frame, (pixel_x, pixel_y),
                      (pixel_x + box_size, pixel_y + box_size),
                      (255, 0, 0), -1)

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
