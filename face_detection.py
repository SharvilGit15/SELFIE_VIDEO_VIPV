import cv2
import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


MODEL_PATH = "blaze_face_short_range.tflite"


def detect_faces(image_path: str):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read image")

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb_image
    )

    # Load face detector model
    base_options = python.BaseOptions(
        model_asset_path=MODEL_PATH
    )

    options = vision.FaceDetectorOptions(
        base_options=base_options,
        min_detection_confidence=0.5
    )

    # Run face detection
    with vision.FaceDetector.create_from_options(options) as detector:

        result = detector.detect(mp_image)

    detected_faces = []

    if result.detections:

        for detection in result.detections:

            bounding_box = detection.bounding_box

            detected_faces.append({
                "x": bounding_box.origin_x,
                "y": bounding_box.origin_y,
                "width": bounding_box.width,
                "height": bounding_box.height,
                "confidence": round(
                    detection.categories[0].score,
                    3
                )
            })

    return detected_faces