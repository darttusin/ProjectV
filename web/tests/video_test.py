import cv2

def test_input():
    vid = cv2.VideoCapture("filesrc location=./tracker/data/video/hype.mp4 ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    assert int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)) != 0
    assert int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)) != 0
    assert int(vid.get(cv2.CAP_PROP_FPS)) != 0
    assert vid != None
    vid.release()

def test_output():
    vid = cv2.VideoCapture("filesrc location=./tracker/data/video/hype.mp4 ! decodebin ! videoconvert ! appsink", cv2.CAP_GSTREAMER)
    pipe_out = 'appsrc ! videoconvert ! x264enc tune=zerolatency bitrate=700 speed-preset=superfast ! decodebin ! autovideoconvert ! theoraenc ! oggmux ! tcpserversink host=127.0.0.1 port=8080'
    out = cv2.VideoWriter(pipe_out, 0, 30, (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))), True)
    assert out != None
    vid.release()
    out.release()
