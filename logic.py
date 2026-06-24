def detect_suspicious(gaze, yaw, pitch, time_away):
    if gaze != "center" and time_away > 3:
        return True, "Looking away"

    if yaw > 25 or yaw < -25:
        return True, "Head turned"

    if pitch > 20 or pitch < -20:
        return True, "Looking up/down"

    return False, "Normal"