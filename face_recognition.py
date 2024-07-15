import cv2
import threading
from deepface import DeepFace
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
reference_img = cv2.imread("afss.jpg")
reference_img = cv2.imread("roger2.jpg")
reference_img = cv2.imread("roger3.jpg")
reference_img = cv2.imread("TheGod1.jpg")
reference_img = cv2.imread("TheGod.jpg")
reference_img = cv2.imread("surya.jpg")
reference_img = cv2.imread("surya3.jpg")
reference_img = cv2.imread("surya2.jpg")
reference_img = cv2.imread("surya4.jpg")


if reference_img is None:
    print("Error: Reference image not loaded. Check the path.")
    exit()

def check_face(frame):
    global face_match
    try:
        print("Checking face...")
        result = DeepFace.verify(frame, reference_img.copy())
        print("DeepFace result:", result)
        if result['verified']:
            face_match = True
        else:
            face_match = False
    except Exception as e:
        print("Error in face verification:", e)
        face_match = False

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                check_face(frame.copy())
            except Exception as e:
                print("Error starting thread:", e)
        counter += 1

        if face_match:
            print("match")
            cv2.putText(frame, "MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        else:
            print("no match")
            cv2.putText(frame, "NO MATCH", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        cv2.imshow("video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
