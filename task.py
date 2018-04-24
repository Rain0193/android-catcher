import time


class Task(object):
    def __init__(self, name):
        self.name = name
        self.period = None
        self.d = None
        self.device = None
        self.applicationid = None
        self.version_name = None
        self.pid = None
        self.interval = None
        self.output = None
        self.info_list = set([])

    def execute(self):
        pass

    def add_info(self, info):
        self.info_list.add(info)
        info.task = self

    def set_device(self, d):
        self.d = d


class RandomTask(Task):

    def __init__(self, name):
        super().__init__(name)
        self.duration = 0.0

    def execute(self):
        time.sleep(self.duration)
