import cv2

def image_differencing (cap):

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Total Frame: {frame_count} , FPS: {fps}")
    
    #Retrieve the first frame of a video
    ret, prev_frame = cap.read()
    if not ret:
        print("Couldnt read the first frame from video")
        exit()
    
    #Determine which frames to be processed
    frame_start = int(input(f"Pilih frame awal between 0 - {frame_count-1}: "))
    frame_end = int(input(f"Pilih frame akhir between {frame_start+1} - {frame_count}: "))    
    
    for frames in range(int(frame_count)):
        ret, curr_frame = cap.read()

        if frames <= frame_start:
            continue
        
        if not ret or frames > frame_end:
            break

        #convert frames into grayscale for a better view of differences (reduce noises)
        prev_grey = cv2.cvtColor(prev_frame, cv2.COLOR_RGB2GRAY)
        curr_grey = cv2.cvtColor(curr_frame, cv2.COLOR_RGB2GRAY)
    
        frame_diff = cv2.absdiff(prev_grey, curr_grey)
       
        cv2.imwrite(f"result {frames-1} and {frames}.png", frame_diff) 
        prev_frame = curr_frame
        
    #closes video files to frees up memories
    cap.release()