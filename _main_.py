import getopt
import re
import sys

import uiautomator2 as u2

import utils
from info import CPUInfo, MemInfo, FPSInfo, NetInfo
from info_task import InfoTask
from task import RandomTask


# 命令行配置参数
# -s device 设备号
# -a applicationid 包名
# -f frequence 频率，即采样间隔，单位为秒
# -d duration 无自定义测试场景时，为RandomTask指定运行时间
# -i info 需要采集的信息
# -o output 输出目录，默认为"."
# -u user 账号
# -p password 密码
# -l url 需要安装app的url地址

def main(task):
    device = None
    applicationid = None
    interval = 1
    duration = 10
    info_names = []
    output = "."
    opts, args = getopt.getopt(sys.argv[1:], "s:a:f:d:i:o:t:u:p:l:")

    for opt, value in opts:
        if opt == "-s":
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

    d = u2.connect(device)
    d.app_start(applicationid)
    pid = utils.get_pid_by_applicationid(d, applicationid)
    version_name = utils.get_version_name_by_applicationid(d, applicationid)

    task.d = d
    task.device = device
    task.applicationid = applicationid
    task.version_name = version_name
    task.pid = pid
    task.interval = interval
    task.output = output

    for info in info_names:
        if info == "cpu":
            task.add_info(CPUInfo())
        elif info == "mem":
            task.add_info(MemInfo())
        elif info == "fps":
            task.add_info(FPSInfo())
        elif info == "net":
            task.add_info(NetInfo())

    if isinstance(task, RandomTask):
        task.duration = duration

    info_task = InfoTask(task)
    info_task.start()


if __name__ == '__main__':
    main(RandomTask("Random"))
