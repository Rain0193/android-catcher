import getopt
import re
import sys

import uiautomator2 as u2

import utils
from info import CPUInfo, MemInfo, FPSInfo, NetInfo
from info_task import InfoTask
from task import RandomTask


def main(task):
    device = None
    applicationid = None
    interval = 1
    duration = 10
    info_names = None
    output = None
    opts, args = getopt.getopt(sys.argv[1:], "d:p:f:t:i:o:")

    for opt, value in opts:
        if opt == "-d":
            device = value
        elif opt == "-p":
            applicationid = value
        elif opt == "-f":
            interval = float(value)
        elif opt == "-t":
            duration = float(value)
        elif opt == "-i":
            info_names = re.split("\s?,\s?", value)
        elif opt == "-o":
            if value is None:
                output = "."
            else:
                output = value

    d = u2.connect(device)
    pid = utils.get_pid_by_applicationid(d, applicationid)
    version_name = utils.get_version_name_by_applicationid(d, applicationid)

    for info in info_names:
        if info == "cpu":
            task.info_list.add(CPUInfo(task, d, device, applicationid, version_name, pid, interval, output))
        elif info == "mem":
            task.info_list.add(MemInfo(task, d, device, applicationid, version_name, pid, interval, output))
        elif info == "fps":
            task.info_list.add(FPSInfo(task, d, device, applicationid, version_name, pid, interval, output))
        elif info == "net":
            task.info_list.add(NetInfo(task, d, device, applicationid, version_name, pid, interval, output))

    task.set_device(d)
    if isinstance(task, RandomTask):
        task.duration = duration

    info_task = InfoTask(task)
    info_task.start()


if __name__ == '__main__':
    main(RandomTask("Random"))
