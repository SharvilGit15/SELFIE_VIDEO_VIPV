import cv2


def get_video_info(video_path: str):

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        raise ValueError("Unable to open video")

    fps = capture.get(cv2.CAP_PROP_FPS)
    frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

    duration = 0

    if fps > 0:
        duration = frame_count / fps

    capture.release()

    return {
        "fps": fps,
        "frame_count": int(frame_count),
        "width": int(width),
        "height": int(height),
        "duration_seconds": round(duration, 2)
    }