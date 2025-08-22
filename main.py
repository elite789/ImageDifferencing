import cv2
import numpy

video_input = input("Enter Video Path: ")
cap = cv2.VideoCapture(video_input)

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Total Frame: {frame_count} , FPS: {fps}")

ret, prev_frame = cap.read()
if not ret:
    print("Couldnt read the first frame from video")
    exit()    

for i in range(int(frame_count)):
    ret, curr_frame = cap.read()
    if not ret:
        break
    
    frame_diff = cv2.absdiff(prev_frame, curr_frame)
    cv2.imshow("Current Frame", curr_frame)
    cv2.imshow("Frame Difference", frame_diff)

    cv2.imwrite(f"result{i}.png", frame_diff)

    prev_frame = curr_frame
    i+=30

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



