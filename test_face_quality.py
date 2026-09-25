from app.face.face_detection import detect_faces
from app.face.face_quality import check_face_quality


IMAGE_PATH = "uploads/frames/frame_0.jpg"


print()
print("==============================")
print("FACE QUALITY TEST")
print("==============================")


faces = detect_faces(IMAGE_PATH)

print("Faces detected:", len(faces))


if len(faces) == 0:

    print("No face detected.")
    print("Cannot perform face quality check.")

elif len(faces) > 1:

    print("Multiple faces detected.")
    print("VIPV requires a single primary face.")

else:

    face = faces[0]

    quality = check_face_quality(
        IMAGE_PATH,
        face
    )

    print()
    print("FACE:")
    print(face)

    print()
    print("QUALITY:")
    print(quality)


print("==============================")
