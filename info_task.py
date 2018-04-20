class InfoTask(object):

    def __init__(self, task):
        self.task = task

    def start(self):
        for info in self.task.info_list:
            info.get_start_info()

        if self.task is not None:
            self.task.execute()

        for info in self.task.info_list:
            info.get_end_info()
