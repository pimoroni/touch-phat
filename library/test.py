import signal
import touchphat

@touchphat.on_touch(['A','B','C','D'])
def handle_touch(event):
    print(event.name)

signal.pause()
