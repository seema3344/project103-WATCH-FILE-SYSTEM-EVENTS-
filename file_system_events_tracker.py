import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Add the path of you "Downloads" folder.
from_dir = "C:/Users/SHIBU/Downloads"

class FileEventHandler(FileSystemEventHandler):

    def on_cerated(self,event):
        print(f"hey,{event.src_path} has been created!")

    def on_deleted(self,event):
        print(f"Oops! someone deleted {event.src_path}")
    
    def on_modified(self,event):
        print(f"yep,{event.src_path} has been modified!")

    def on_moved(self,event):
        print(f"Oops!,{event.src_path} has been moved ")

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
