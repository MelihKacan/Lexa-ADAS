import cv2
import numpy as np

def process_frame(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])  

    mask = cv2.inRange(hsv, lower_white, upper_white)
    blur = cv2.GaussianBlur(mask, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    return edges, mask

def main():
    cap = cv2.VideoCapture(0)

    screen_width, screen_height = 1280, 720

    roi_width = 400
    roi_height = 200
    roi_y = (screen_height + 500 - roi_height) // 2

    left_roi_x = 100
    right_roi_x = screen_width - roi_width - 100

    tolerance = 3000

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (screen_width, screen_height))

       
        left_roi = frame[roi_y:roi_y + roi_height, left_roi_x:left_roi_x + roi_width]
        right_roi = frame[roi_y:roi_y + roi_height, right_roi_x:right_roi_x + roi_width]

      
        left_edges, left_mask = process_frame(left_roi)
        right_edges, right_mask = process_frame(right_roi)

        
        left_white = cv2.countNonZero(left_mask)
        right_white = cv2.countNonZero(right_mask)

        
        if abs(left_white - right_white) > tolerance:
            if left_white > right_white:
                cv2.circle(frame, (640,360),125, (0, 0, 255), -1)
                cv2.arrowedLine(frame, (755,360), (525,360),(255, 255, 255), 10)

            else:
                cv2.circle(frame, (640,360),125,  (255, 0, 0), -1)
                cv2.arrowedLine(frame, (525,360), (755,360),(255, 255, 255), 10)

        
        left_contours, _ = cv2.findContours(left_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        right_contours, _ = cv2.findContours(right_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(left_roi, left_contours, -1, (0, 255, 0), 2)
        cv2.drawContours(right_roi, right_contours, -1, (0, 255, 0), 2)

        
        frame[roi_y:roi_y + roi_height, left_roi_x:left_roi_x + roi_width] = left_roi
        frame[roi_y:roi_y + roi_height, right_roi_x:right_roi_x + roi_width] = right_roi

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()