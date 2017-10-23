import threading


class Timer:
    stage = None

    def __init__(self, stage, count, finish):
        self.stage = stage
        self.count = count
        self.finish = finish

    def timer(self):
        timer = threading.Timer(1, self.timer)
        self.count -= 1
        timer.start()
        if self.count == 0 or self.finish:
            timer.cancel()

    def Return(self):
        return self.count
