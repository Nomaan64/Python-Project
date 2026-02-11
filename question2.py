import cv2

# Load Haar Cascades
face_cascade = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    "haarcascade_eye.xml"
)

# Load input video
cap = cv2.VideoCapture("face_video.mp4")

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter (MP4)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    "output_face_blink.mp4",
    fourcc,
    fps,
    (width, height)
)

# Blink detection variables
no_eye_frames = 0
BLINK_THRESHOLD = 3

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    if len(faces) > 0:
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])

        face_gray = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(20, 20)
        )

        if len(eyes) >= 2:
            no_eye_frames = 0
            box_color = (0, 255, 0)
            status = "Eyes Open"
        else:
            no_eye_frames += 1
            if no_eye_frames >= BLINK_THRESHOLD:
                box_color = (0, 0, 255)
                status = "Eye Blink"
            else:
                box_color = (0, 255, 0)
                status = "Eyes Open"

        cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)
        cv2.putText(frame, status, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, box_color, 2)

    # SHOW video
    cv2.imshow("Driver Eye Blink Detection", frame)

    # SAVE video frame
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
