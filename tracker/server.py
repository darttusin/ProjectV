from fastapi import FastAPI
import traceback
import object_tracker as object_tracker

fapp = FastAPI()
is_running=False

@fapp.get('/start/')
def get_schedule() -> dict:
    global is_running
    try:
        print('Before app run')
        #app.run(object_tracker.main)
        if not is_running:
            is_running=True
            object_tracker.main()
            is_running=False
            return 'Ok'
        else:
            return 'Already running!'
    except Exception as e:
        print(f'Error {e} {traceback.format_exc()}')
        return 'Error'