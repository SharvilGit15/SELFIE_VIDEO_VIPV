from app.video.video_service import get_video_info
from app.video.frame_service import extract_frames



VIDEO_PATH = "uploads/person1.mp4"
FRAME_FOLDER = "uploads/frames"


print()
print("================================")
print("SELFIE VIDEO ANALYSIS")
print("================================")


# --------------------------------
# GET VIDEO INFORMATION
# --------------------------------

video_info = get_video_info(
    VIDEO_PATH
)


print()
print("VIDEO INFORMATION")
print("------------------")

print(
    "FPS:",
    video_info["fps"]
)

print(
    "Frame Count:",
    video_info["frame_count"]
)

print(
    "Width:",
    video_info["width"]
)

print(
    "Height:",
    video_info["height"]
)

print(
    "Duration:",
    video_info["duration_seconds"],
    "seconds"
)
# EXTRACT FRAMES
frames = extract_frames(
    VIDEO_PATH,
    FRAME_FOLDER,
    interval_seconds=1
)


print()
print("FRAME EXTRACTION")
print("----------------")

print(
    "Frames extracted:",
    len(frames)
)

for frame in frames:

    print(
        frame
    )

print()
print("================================")
print("VIDEO PROCESSING COMPLETED")
print("================================")