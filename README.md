# Head Pose & Gaze Tracking - CV11

## 1. Introduction

Head pose estimation and gaze tracking are important techniques in computer vision that help determine where a person is looking. These methods are widely used in applications such as online interviews, virtual meetings, and security systems.

In interview monitoring systems, these techniques can help detect suspicious behavior like frequently looking away from the screen, which may indicate cheating or distraction.

This document explains the basic concepts of head pose estimation, gaze tracking, and how they can be used to detect suspicious behavior.

## Head Pose Angles Diagram

![Head Pose Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Head_pose_estimation_axes.png/512px-Head_pose_estimation_axes.png)

### Explanation:
- **Yaw** → Left / Right movement  
- **Pitch** → Up / Down movement  
- **Roll** → Tilt movement  

Note: This project is purely conceptual and does not include implementation. The values and outputs shown are illustrative examples of how a real system would behave.

## 2. Head Pose Estimation

Head pose estimation is the process of determining the orientation of a person's head in 3D space. It tells us whether a person is looking straight, left, right, up, or down.

This is done using facial landmarks, which are specific points on the face such as the eyes, nose, and mouth. Modern models like MediaPipe detect up to 468 facial landmarks.

Using these landmarks, the system maps 2D image points to a 3D model of the face and calculates the head orientation.

Head pose estimation is important because it helps in understanding user attention and behavior.


## 3. Euler Angles (Yaw, Pitch, Roll)

Euler angles describe head orientation in 3D space.

### 1. Yaw (Left–Right Rotation)

* Positive yaw → Head turned right
* Negative yaw → Head turned left

Example: yaw = 30° → looking right

---

### 2. Pitch (Up–Down Rotation)

* Positive pitch → Looking up
* Negative pitch → Looking down

Example: pitch = -10° → slightly looking down

---

### 3. Roll (Tilt Rotation)

* Positive roll → Tilt right
* Negative roll → Tilt left

Example: roll = 5° → slight tilt

---

### Sample Head Pose Output

```json
{
  "yaw": 15,
  "pitch": -5,
  "roll": 2
}
```

### Recommended Thresholds

| Angle | Normal Range | Suspicious |
| ----- | ------------ | ---------- |
| Yaw   | -20° to 20°  | > 25°      |
| Pitch | -15° to 15°  | > 20°      |
| Roll  | -10° to 10°  | > 15°      |

---

## 4. Gaze Tracking

Gaze tracking determines where a person is looking based on eye movement.

### How It Works

1. Detect facial landmarks (MediaPipe – 468 points)
2. Identify eye region
3. Locate iris center
4. Compare iris position
5. Determine gaze direction

---

### Gaze Direction Logic

| Iris Position | Gaze Direction |
| ------------- | -------------- |
| Center        | Forward        |
| Left          | Right          |
| Right         | Left           |
| Up            | Up             |
| Down          | Down           |

---

### Example Output

```json
{
  "gaze_direction": "left"
}
```

---

### Real-Life Example

Frame 1–30 → gaze = center
Frame 31–120 → gaze = left

If duration > 3 seconds → Suspicious

---

## 5. Suspicious Behavior Detection

This detects unusual actions during online interviews.

### Key Indicators

* Looking away for long duration
* Frequent head movement
* Continuous downward gaze
* Sudden direction changes

---

### Detection Rules

#### Gaze

* Not center for > 3 seconds → Suspicious

#### Yaw

* > 25° or < -25° → Looking away

#### Pitch

* > 20° or < -20° → Looking up/down

#### Movement

* > 5 changes in 10 seconds → Suspicious

---

### Combined Logic

* Head turned + gaze away → High suspicion
* Small movements → Normal

---

### Pseudo Code

```python
if gaze_direction != "center" for 3 seconds:
    suspicious = True
    reason = "Looking away"

elif yaw > 25 or yaw < -25:
    suspicious = True
    reason = "Head turned away"

elif pitch > 20 or pitch < -20:
    suspicious = True
    reason = "Looking up/down excessively"

elif movement_count > 5 in 10 seconds:
    suspicious = True
    reason = "Frequent movements"
```

---

### Suspicion Levels

| Condition              | Level    |
| ---------------------- | -------- |
| Looking away > 3 sec   | Medium   |
| Head turned > 25°      | Medium   |
| Multiple violations    | High     |
| Continuous distraction | Critical |

---

## 6. Input and Output

### Input

```json
{
  "face_landmarks": [468 points],
  "frame_id": 42
}
```

### Output

```json
{
  "yaw": 10,
  "pitch": -5,
  "roll": 2,
  "gaze_direction": "center",
  "suspicious": false
}
```
## Tools & Technologies

- MediaPipe (Face Landmark Detection)
- OpenCV (Image Processing)
- Python (Conceptual Implementation)
- Computer Vision Techniques
## Applications

- Online Interview Monitoring
- Exam Proctoring Systems
- Driver Attention Monitoring
- Human-Computer Interaction
## 7. Conclusion

Head pose estimation and gaze tracking are powerful computer vision techniques used to analyze user attention and behavior.

By combining:
- Facial landmark detection
- Euler angle computation
- Gaze direction analysis

we can build intelligent systems capable of detecting suspicious activities.

Although false positives may occur (e.g., thinking vs cheating), combining multiple signals improves system reliability.

This project provides a strong conceptual foundation for building real-time AI-based monitoring systems.