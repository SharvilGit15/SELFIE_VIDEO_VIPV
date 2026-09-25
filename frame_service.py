import cv2
import os


def extract_frames(
    video_path: str,
    output_folder: str,
    interval_seconds: float = 1.0
):

    os.makedirs(output_folder, exist_ok=True)

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        raise ValueError("Unable to open video")

    fps = capture.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    frame_interval = int(fps * interval_seconds)

    frame_number = 0
    saved_frames = []

    while True:

        success, frame = capture.read()

        if not success:
            break

        if frame_number % frame_interval == 0:

            frame_path = os.path.join(
                output_folder,
                f"frame_{frame_number}.jpg"
            )

            cv2.imwrite(frame_path, frame)

            saved_frames.append(frame_path)

        frame_number += 1

    capture.release()

    return saved_frames