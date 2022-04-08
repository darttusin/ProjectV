from threading import Thread
from threading import Thread
from time import sleep
import sys

import pgi

pgi.install_as_gi()

from gi.repository import Gst, GLib


Gst.init(sys.argv) 

main_loop = GLib.MainLoop()
thread = Thread(target=main_loop.run)
thread.start()

pipeline = Gst.parse_launch("v4l2src ! decodebin ! videoconvert ! autovideosink")
pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()