import getopt
import re
import sys

import uiautomator2 as u2

import utils
from info import CPUInfo, MemInfo, FPSInfo, NetInfo
from info_task import InfoTask
from regular_task import RecordVideoTask, MainListScrollTask, DetailsListScrollTask, LoginTask, OpenPermissionsTask
from task import RandomTask


def main(task):
    task_name = None
    device = None
    applicationid = None
    interval = 1
    duration = 10
    info_names = []
    output = "."
    account = None
    password = None
    opts, args = getopt.getopt(sys.argv[1:], "t:s:a:f:d:i:o:u:p:")

    for opt, value in opts:
        if opt == "-t":
            task_name = value
        elif opt == "-s":
            device = value
        elif opt == "-a":
            applicationid = value
        elif opt == "-f":
            interval = float(value)
        elif opt == "-d":
            duration = float(value)
        elif opt == "-i":
            info_names = re.split("\s?,\s?", value)
        elif opt == "-o":
            if value is not None:
                output = value
        elif opt == "u":
            account = value
        elif opt == "p":
            password = value

    d = u2.connect(device)
    pid = utils.get_pid_by_applicationid(d, applicationid)
    version_name = utils.get_version_name_by_applicationid(d, applicationid)

    if task is None:
        if task_name == "RecordVideo":
            task = RecordVideoTask(task_name)
        elif task_name == "MainListScroll":
            task = MainListScrollTask(task_name)
        elif task_name == "DetailsListScroll":
            task = DetailsListScrollTask(task_name)
        elif task_name == "Login":
            task = LoginTask(task_name, account, password)
        elif task_name == "OpenPermissions":
            task = OpenPermissionsTask(task_name)
        else:
            task_name = "Random"
            task = RandomTask(task_name)

    if task_name == "RecordVideo" or task_name == "MainListScroll" or "DetailsListScroll":
        task.info_list.add(CPUInfo(task_name, d, device, applicationid, version_name, pid, interval, output))
        task.info_list.add(MemInfo(task_name, d, device, applicationid, version_name, pid, interval, output))

    for info in info_names:
        if info == "cpu":
            task.info_list.add(CPUInfo(task_name, d, device, applicationid, version_name, pid, interval, output))
        elif info == "mem":
            task.info_list.add(MemInfo(task_name, d, device, applicationid, version_name, pid, interval, output))
        elif info == "fps":
            task.info_list.add(FPSInfo(task_name, d, device, applicationid, version_name, pid, interval, output))
        elif info == "net":
            task.info_list.add(NetInfo(task_name, d, device, applicationid, version_name, pid, interval, output))

    task.set_device(d)
    if isinstance(task, RandomTask):
        task.duration = duration

    info_task = InfoTask(task)
    info_task.start()


if __name__ == '__main__':
    main(None)
