import threading


class Timer:
    stage = None

    def __init__(self, stage, count):
        self.stage = stage
        self.count = count

    def timer(self):
        time = threading.Timer(1, self.timer)
        self.count -= 1
        time.start()
        if self.count == 0:
            time.cancel()

    def Return(self):
        return self.count
