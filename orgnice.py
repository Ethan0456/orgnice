import time
import sys
import os
import readConfig
import move
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import PatternMatchingEventHandler

# EventHandler
class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.skip_next = False
    
    # to handle new files
    def on_created(self, event):
        print(f"New File Found: {event.src_path}")
        if (os.path.exists(event.src_path)):
            move.decideAndMoveFile(event.src_path, groups)

    # to handle file rename
    def on_moved(self, event):
        if not self.skip_next:
            print(f"File Modification Found: {event.src_path} to {event.dest_path}")
            if (os.path.exists(event.dest_path)):
                move.decideAndMoveFile(event.dest_path, groups)
                self.skip_next = True
        else:
            self.skip_next = False
        

if __name__ == "__main__":
    # Get Directories argument list
    args = sys.argv
    print(args)
    if len(args) == 1:
        print("Resorting to default config...")
        config = readConfig.readConfigFile(os.path.expandvars("$HOME/.config/orgnice/config.yml"))

    # check for flags
    # types
    # -o = do it once
    # -c = config file
    options = {
        "once":False,
        "config":False,
    }

    # Handling options
    if ("-o" in args):
        options["once"] = True
        args.remove("-o")
    if ("-c" in args):
        options["config"] = args[args.index("-c")+1]
        args.remove("-c")
        config = readConfig.readConfigFile(options["config"])

    dirs = config["dirs"]
    groups = config["groups"]

    if (dirs is None):
        print("Specify atleast one 'dirs' key value in config !")
        sys.exit()
    
    # For running the program only once
    if (options["once"]):
        print("Running once")
        for dir in dirs:
            ls_dir = os.listdir(dir)
            for file in ls_dir:
                filename = os.path.join(dir,file)
                if (os.path.isfile(filename)):
                    if (filename[0] != "."):
                        move.decideAndMoveFile(filename, groups)

    # Observer and Scheduler for each directories
    else:
        observer = Observer()
        for dir in config["dirs"]:
            observer.schedule(EventHandler(), path=os.path.expandvars(dir))
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()