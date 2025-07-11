import cv2
import os

"""
Assuming 30 FPS, 5 minute video will have 9000 image frames, use frame_interval = 10. Results in 900 images. 
"""

video_path = r"E:\Workdir\Projects\lane-detection-alert\data\test_jeep_night_1.mp4"
output_dir = r"E:\Workdir\Projects\lane-detection-alert\data\frames"
os.makedirs(output_dir, exist_ok=True)

# Create VideoCapture object, use it to open video
cap = cv2.VideoCapture(video_path)
frame_count = 0
frame_interval = 1

while True:
    # Read the next frame from the video
    # ret - boolean: True if the read frame success, False if video end or error
    # frame - numpy array: image contain pixel data of the frame
    ret, frame = cap.read()

    if not ret:
        break
    if frame_count % frame_interval == 0:
        cv2.imwrite(f"{output_dir}/frame_{frame_count:04d}.jpg", frame)
    frame_count += 1

cap.release() # Free the video resource, close the file

print(f"Extracted {frame_count} frames from {video_path} to {output_dir}")