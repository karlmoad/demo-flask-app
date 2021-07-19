import threading
import time


class Process:
    def __init__(self):
        self._thread = threading.Thread(target=self.run)
        self._lock = threading.Lock()
        self._active = False
        self._counter = 0

    def run(self):
        while self._check():
            cur = self._increment()
            print("Iteration: {}".format(cur))
            time.sleep(5)
        print("thread stopped")

    def begin(self):
        with self._lock:
            self._active = True
        self._thread.start()
        return {"message": "Processing Thread Started"}

    def isAlive(self):
        with self._lock:
            return {"active": self._active}

    def _check(self):
        with self._lock:
            return self._active

    def stop(self):
        with self._lock:
            self._active = False
        print("Stopping")
        self._thread.join()
        return {"message": "Processing Thread Stopped"}

    def _increment(self):
        with self._lock:
            self._counter = self._counter + 1
            return self._counter
