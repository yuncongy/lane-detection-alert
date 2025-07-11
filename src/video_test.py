import cv2

# Replace with your actual video path (can be .mp4, .avi, etc.)
video_path = 'data/sample_video.mkv'  # <- make sure this file exists

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Finished reading video or failed to read frame.")
        break

    cv2.imshow("Video Frame", frame)

    # Press 'q' to quit early
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
