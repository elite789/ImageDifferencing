import cv2

def image_differencing (cap):

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Total Frame: {frame_count} , FPS: {fps}")
    
    frame_start = int(frame_count/2)
    frame_end = frame_start + 5

    for frames in range(frame_end - frame_start):
        curr = frames + frame_start
        cap.set(cv2.CAP_PROP_POS_FRAMES, curr)
        ret, curr_frame = cap.read()

        cap.set(cv2.CAP_PROP_POS_FRAMES, curr+1)
        ret, next_frame = cap.read()


        #convert frames into grayscale for a better view of differences (reduce noises)
        curr_grey = cv2.cvtColor(curr_frame, cv2.COLOR_RGB2GRAY)
        next_grey = cv2.cvtColor(next_frame, cv2.COLOR_RGB2GRAY)
    
        frame_diff = cv2.absdiff(curr_grey, next_grey)
       
        cv2.imwrite(f"result {curr} and {curr+1}.png", frame_diff) 
        
    #closes video files to frees up memories
    cap.release()