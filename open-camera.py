import cv2

cap_video = cv2.VideoCapture(0)
cap_video.set(3,200)
cap_video.set(4,200)

if not cap_video.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap_video.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap_video.release()
cv2.destroyAllWindows()