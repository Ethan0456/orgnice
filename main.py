import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file created: {event.src_path}")

observer = Observer()
observer.schedule(MyHandler(), path='.')
observer.start()

directories = sys.argv

try:
    while True:
        # Keep the program running until interrupted
        pass
except KeyboardInterrupt:
    # Stop the observer when the program is interrupted
    observer.stop()

observer.join()