import time


class Task(object):
    def __init__(self, name):
        self.name = name
        self.d = None
        self.info_list = set([])

    def execute(self):
        pass

    def add_info(self, info):
        self.info_list.add(info)

    def set_device(self, d):
        self.d = d


class RandomTask(Task):

    def __init__(self, name):
        super().__init__(name)
        self.duration = 0.0

    def execute(self):
        time.sleep(self.duration)
