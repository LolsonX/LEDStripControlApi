import time
from threading import Thread


class ScriptThread(Thread):
    def __init__(self):
        self.running = False
        self.starting = True
        super().__init__(target=self.run_script)

    def start(self):
        self.stop()
        self.running = True
        if self.starting:
            super().start()
            self.starting = False

    def stop(self):
        self.running = False

    def run_script(self):
        while True:
            while self.running:
                time.sleep(1)
