# 🎯 Head Pose & Gaze Tracking using MediaPipe

## 📌 Overview

This project implements a **real-time Head Pose Estimation and Gaze Tracking system** using **MediaPipe** and **OpenCV**.

It detects facial landmarks, estimates head orientation (yaw, pitch, roll), and determines gaze direction to analyze user attention.

Such systems are widely used in:

* Online interview monitoring
* Exam proctoring
* Driver attention tracking
* Human-computer interaction

---

## 🚀 Features

* 🎥 Real-time webcam processing
* 🧠 Face landmark detection (468 points using MediaPipe)
* 🎯 Head pose estimation (Yaw, Pitch, Roll)
* 👁️ Gaze direction tracking
* ⚠️ Basic suspicious behavior detection logic

---

## 🖥️ Demo

> Add your demo GIF or screenshot here

```
![Demo](demo.gif)
```

---

## 🧠 How It Works

### 1. Face Detection

* Uses MediaPipe Face Mesh
* Detects 468 facial landmarks

### 2. Head Pose Estimation

* Maps 2D landmarks to 3D model
* Calculates:

  * **Yaw** → Left/Right
  * **Pitch** → Up/Down
  * **Roll** → Tilt

### 3. Gaze Tracking

* Extracts eye region
* Detects iris position
* Determines gaze direction

---

## 📊 Sample Output

```json
{
  "yaw": 10,
  "pitch": -5,
  "roll": 2,
  "gaze_direction": "center",
  "suspicious": false
}
```

---

## ⚠️ Suspicious Behavior Detection

The system flags potential issues based on:

* Looking away for extended duration
* Excessive head rotation
* Continuous downward gaze
* Frequent movement

### Example Rule:

```python
if gaze_direction != "center" for 3 seconds:
    suspicious = True
```

---

## 🛠️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📦 Installation

```bash
git clone https://github.com/YOUR_USERNAME/HeadPose-GazeTracking.git
cd HeadPose-GazeTracking
pip install -r requirements.txt
python logic.py
```

---

## 📁 Project Structure

```
├── logic.py
├── README.md
├── requirements.txt
```

---

## 📌 Requirements

Create a `requirements.txt` file:

```
opencv-python
mediapipe
numpy
```

---

## 📈 Applications

* Online Interview Monitoring
* Exam Proctoring Systems
* Driver Drowsiness Detection
* Attention Tracking Systems

---

## 🧾 Future Improvements

* 🔊 Alert system for suspicious behavior
* 📊 Dashboard visualization
* 🧠 AI-based behavior classification
* 🎯 Improved gaze accuracy

---

## 🏁 Conclusion

This project demonstrates how **computer vision techniques** can be used to analyze human attention and behavior in real time.

By combining:

* Face landmark detection
* Head pose estimation
* Gaze tracking

we can build intelligent monitoring systems with real-world applications.

---

## 🙌 Acknowledgements

* MediaPipe by Google
* OpenCV community

---
T.KAVYA YADAV