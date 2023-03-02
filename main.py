import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"New file created: {event.src_path}")

directories = sys.argv

observer = Observer()
for dirs in directories:
    observer.schedule(Handler(), path=dirs)
observer.start()


try:
    while True:
        # Keep the program running until interrupted
        pass
except KeyboardInterrupt:
    # Stop the observer when the program is interrupted
    observer.stop()

observer.join()