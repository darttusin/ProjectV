from absl import app
import object_tracker as object_tracker

object_tracker.set_flags()

app.run(object_tracker.main)