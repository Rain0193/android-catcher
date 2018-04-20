import csv
import os
import re
import time


def get_csv_writer(dirs, file_name, field_names):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    file_path = dirs + file_name + "_" + format(time.time(), ".0f") + ".csv"
    mem_csv = open(file_path, 'w', newline='', encoding="GBK")
    writer = csv.DictWriter(mem_csv, fieldnames=field_names)
    writer.writeheader()
    return writer


def get_applicationid_by_pid(d, pid):
    ps_info = re.findall("\S+", d.adb_shell("ps | grep " + pid))
    return ps_info[len(ps_info) - 1]


def get_pid_by_applicationid(d, applicationid):
    ps_info = re.findall("\S+", d.adb_shell("ps | grep " + applicationid + "$"))
    return ps_info[1]


def get_version_name_by_applicationid(d, applicationid):
    version_info = d.adb_shell("dumpsys package " + applicationid + " | grep versionName")
    return re.findall("\d+.+\d", version_info)[0]
