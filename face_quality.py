import cv2


def calculate_blur_score(image):
    """
    Higher value generally means a sharper image.
    Lower value generally means a blurrier image.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()


def check_face_quality(image_path: str, face: dict):

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to read image")

    image_height, image_width = image.shape[:2]

    x = face["x"]
    y = face["y"]
    width = face["width"]
    height = face["height"]

    issues = []

    # --------------------------------
    # 1. Face size
    # --------------------------------

    face_area = width * height
    image_area = image_width * image_height

    face_ratio = face_area / image_area

    if face_ratio < 0.040:
        issues.append("Face is too small")

    # --------------------------------
    # 2. Face position
    # --------------------------------

    if x < 0 or y < 0:
        issues.append("Face is outside frame")

    if x + width > image_width:
        issues.append("Face is cut off on right side")

    if y + height > image_height:
        issues.append("Face is cut off at bottom")

    # --------------------------------
    # 3. Blur detection
    # --------------------------------

    blur_score = calculate_blur_score(image)

    if blur_score < 100:
        issues.append("Image may be blurry")

    # --------------------------------
    # Final result
    # --------------------------------

    return {
        "face_area_ratio": round(face_ratio, 4),
        "blur_score": round(blur_score, 2),
        "quality_ok": len(issues) == 0,
        "issues": issues
    }