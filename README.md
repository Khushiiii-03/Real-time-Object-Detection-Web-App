# Real-time-Object-Detection-Web-App
An interactive web application for real-time object detection using YOLOv8 and Streamlit. The app supports image upload and live webcam detection.

DEMO:-

1) **Image upload**
   <img width="1141" height="799" alt="Screenshot 2026-04-09 at 3 13 43 PM" src="https://github.com/user-attachments/assets/9f11429e-f4da-47a8-9dc6-ac6c70cf2ced" />
<img width="1092" height="786" alt="Screenshot 2026-04-09 at 3 14 04 PM" src="https://github.com/user-attachments/assets/48d54c46-317c-4907-8007-fd9718f36370" />

2) **Webcam**
 
   <img width="896" height="730" alt="Screenshot 2026-04-09 at 4 31 18 PM" src="https://github.com/user-attachments/assets/c1cb1277-3cfe-4ea8-b09f-8c0d2c3a61ac" />

---
Features

- Detect 80+ object classes (COCO dataset)
- Image upload detection
- Real-time webcam detection

---
Tech Stack

- **Python**
- **YOLOv8 (Ultralytics)**
- **Streamlit**
- **OpenCV**
- **NumPy**
- **Pillow**

---
How It Works

The application uses YOLOv8 (You Only Look Once), a deep learning-based object detection model, to identify and classify objects in images and real-time video streams.

1. Model Loading
The YOLOv8 model (yolov8m.pt) is loaded using the Ultralytics library.
This is a pre-trained model trained on the COCO dataset (80 object classes).
Purpose: Enables detection without needing custom training

2. Image Input Pipeline
When a user uploads an image: The image is loaded using PIL
Converted into a NumPy array for processing
Passed to the YOLO model for inference
The model detects objects, Draws bounding boxes, Assigns labels and confidence scores and Output is displayed using Streamlit

3. Real-Time Webcam Detection
When webcam mode is enabled, OpenCV captures frames continuously, Each frame is Flipped for mirror view
Passed into the YOLO model
YOLO processes each frame in real time
Detected objects are drawn on the frame and displayed live

4. Object Counting
The model returns detected bounding boxes, Each detected object is classified.

---
Use Cases

- Smart surveillance systems
- Traffic monitoring
- Retail analytics
- Assistive vision systems
