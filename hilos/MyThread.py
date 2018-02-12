import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        time.sleep(self.delay)
        print("Exiting " + self.name)
