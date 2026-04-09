import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

model = YOLO("yolov8m.pt") # better accuracy than yolov8n.pt, and yolov8l.pt

st.title("Real - Time Object Detection App")
st.write("Upload an image or use webcam for detection")

option = st.radio("Choose Input Type:", ("Image Upload", "Webcam"))

# img upload
if option == "Image Upload":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        img_array = np.array(image)

        results = model(img_array)
        annotated = results[0].plot()

        st.image(annotated, caption="Detected Image", use_container_width=True)

        st.subheader("Detected Objects:")
        counts = {}

        for r in results:
            for box in r.boxes:
                cls = model.names[int(box.cls[0])]
                counts[cls] = counts.get(cls, 0) + 1

        st.write(counts)

# webcam
elif option == "Webcam":
    run = st.checkbox("Start Webcam")

    FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.write("Error accessing webcam")
            break

        frame = cv2.flip(frame, 1)  # mirror view
        
        results = model(frame, conf = 0.5)
        annotated = results[0].plot()

        FRAME_WINDOW.image(annotated)

    cap.release()