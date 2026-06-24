# Head Pose & Gaze Tracking - CV11

## 1. Introduction
Head pose estimation and gaze tracking are important techniques in computer vision that help determine where a person is looking. These methods are widely used in applications such as online interviews, virtual meetings, and security systems. In interview monitoring systems, these techniques can help detect suspicious behavior like frequently looking away from the screen, which may indicate cheating or distraction.

This document explains the basic concepts of head pose estimation, gaze tracking, and how they can be used to detect suspicious behavior.

---

## 2. Head Pose Estimation
Head pose estimation is the process of determining the orientation of a person's head in 3D space. It tells us whether a person is looking straight, left, right, up, or down.

This is done using facial landmarks, which are specific points on the face such as the eyes, nose, and mouth. Modern models like MediaPipe detect up to 468 facial landmarks.

Using these landmarks, the system maps 2D image points to a 3D model of the face and calculates the head orientation.

Head pose estimation is important because it helps in understanding user attention and behavior.

---

## 3. Euler Angles (Yaw, Pitch, Roll)
Euler angles are used to describe the orientation of the head in 3D space. They represent rotation along three different axes and are essential for head pose estimation.

### 1. Yaw (Left–Right Rotation)
Yaw represents the horizontal movement of the head.
- Positive yaw → Head turned to the right
- Negative yaw → Head turned to the left

Example:
If yaw = 30°, the person is looking towards the right side.

---

### 2. Pitch (Up–Down Rotation)
Pitch represents the vertical movement of the head.
- Positive pitch → Looking up
- Negative pitch → Looking down

Example:
If pitch = -10°, the person is slightly looking down.

---

### 3. Roll (Tilt Rotation)
Roll represents the tilt of the head sideways.
- Positive roll → Tilted to the right
- Negative roll → Tilted to the left

Example:
If roll = 5°, the head is slightly tilted.

---

### Importance in Interview Monitoring
These angles help detect whether a person is focusing on the screen or looking away.

For example:
- High yaw value → Looking away sideways
- High pitch value → Looking down (possibly checking notes)
- High roll value → Unnatural head tilt

---

### Sample Head Pose Output
```json
{
  "yaw": 15,
  "pitch": -5,
  "roll": 2
}
### Recommended Thresholds

| Angle | Normal Range | Suspicious |
|------|-------------|-----------|
| Yaw  | -20° to 20° | > 25° |
| Pitch| -15° to 15° | > 20° |
| Roll | -10° to 10° | > 15° |

## 4. Gaze Tracking

Gaze tracking is the process of determining where a person is looking based on eye movement. Unlike head pose estimation, which tracks the entire head, gaze tracking focuses specifically on the eyes.

It is mainly used to understand user attention and detect whether a person is focused on the screen.

### How Gaze Tracking Works

1. Detect facial landmarks using models like MediaPipe (468 points)
2. Identify eye region landmarks
3. Locate the iris (center of the eye)
4. Compare iris position within the eye boundaries
5. Determine gaze direction
## Gaze Direction Logic

The position of the iris inside the eye helps determine the direction:

- Iris in center → Looking forward
- Iris shifted left → Looking right
- Iris shifted right → Looking left
- Iris up → Looking up
- Iris down → Looking down

# Simple Representation

| Iris Position | Gaze Direction |
|--------------|---------------|
| Center       | Forward       |
| Left         | Right         |
| Right        | Left          |
| Up           | Up            |
| Down         | Down          |

## Gaze Tracking in Interview Monitoring

In online interviews, gaze tracking helps detect whether a candidate is maintaining eye contact with the screen.

Examples:
- Looking away frequently → Possible distraction or cheating
- Looking down continuously → May indicate reading notes
- Looking sideways → May indicate using another device
# Example Output

```json
{
  "gaze_direction": "left"
}
### Real-Life Example

Frame 1–30: gaze = center  
Frame 31–120: gaze = left  

If total time > 3 seconds:
→ System flags: "Suspicious behavior detected"

## 5. Suspicious Behavior Detection

Suspicious behavior detection is the process of identifying unusual actions during an online interview using head pose and gaze tracking.

The system analyzes head movement and eye direction over time to determine whether the candidate is focused or distracted.

---

### Key Indicators of Suspicious Behavior

1. Looking away from the screen for a long duration  
2. Frequent head movements  
3. Continuous downward gaze (possible reading)  
4. Sudden and repeated direction changes  

---

### Threshold-Based Detection Rules

The system uses predefined thresholds to classify behavior as normal or suspicious.

#### 1. Gaze Threshold
- If gaze is not "center" for more than **3 seconds**  
→ Mark as suspicious

#### 2. Head Pose Threshold (Yaw)
- If yaw angle > 25° or < -25°  
→ Person is looking away

#### 3. Pitch Threshold
- If pitch > 20° or < -20°  
→ Looking too much up or down

#### 4. Movement Frequency
- If head/gaze changes more than **5 times in 10 seconds**  
→ Suspicious behavior
## Combined Detection Logic

The system should not rely on a single condition. Instead, multiple signals should be combined:

- Head turned + gaze away → High suspicion  
- Only slight movement → Normal behavior  

# Pseudo Code

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

### Suspicion Levels

| Condition | Level |
|----------|------|
| Looking away > 3 sec | Medium |
| Head turned > 25° | Medium |
| Multiple violations | High |
| Continuous distraction | Critical |

## 6. Input and Output JSON
The system takes input in the form of facial landmark data.

### Input:
```json
{
  "face_landmarks": [468 points],
  "frame_id": 42
}
## 8. Conclusion

Head pose estimation and gaze tracking are powerful computer vision techniques used to analyze user attention and behavior. These methods play an important role in online interview monitoring systems by helping detect suspicious activities.

By using facial landmarks, Euler angles, and gaze direction, the system can estimate where a person is looking and identify unusual patterns. Threshold-based detection and time analysis improve the reliability of the system.

However, these techniques are not perfect and may produce false positives in real-world situations. Therefore, it is important to design the system carefully and consider human behavior before making decisions.

Overall, combining head pose estimation with gaze tracking provides an effective approach for monitoring attention while maintaining fairness.