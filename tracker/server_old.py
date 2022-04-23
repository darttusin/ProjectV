import cv2

cap = cv2.VideoCapture("filesrc location=./data/video/iwearamaskwithasmileforhours.mp4 ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
pipe_out = 'appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=700 speed-preset=superfast ! decodebin ! autovideoconvert ! theoraenc ! oggmux ! tcpserversink host=127.0.0.1 port=8080'
# pipe_out = 'appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! rtspclientsink location=rtsp://0.0.0.0:8554/mystream'

out = cv2.VideoWriter(pipe_out, 0, int(cap.get(cv2.CAP_PROP_FPS))-15, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))), True)
print(cap)

frame_num = 0
while True:
    # Get the frame
    return_value, frame = cap.read()
    if return_value:
        frame_num+=1
        out.write(frame)
        #cv2.imshow("Output Video", frame)
        print(frame_num)

cap.release()
out.release()