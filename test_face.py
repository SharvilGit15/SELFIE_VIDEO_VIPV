from app.face.face_detection import detect_faces


IMAGE_PATH = "uploads/frames/frame_0.jpg"

faces = detect_faces(IMAGE_PATH)

print()
print("==============================")
print("FACE DETECTION TEST")
print("==============================")

print("Faces detected:", len(faces))

for face in faces:
    print(face)

print("==============================")
